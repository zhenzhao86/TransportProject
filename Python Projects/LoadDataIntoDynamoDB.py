import boto3
import boto.dynamodb2
import json
import pypyodbc as pyodbc
import collections

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='ap-northeast-1'
)

connection_string = r'' #for using windows auth
db = pyodbc.connect(connection_string)
cursor = db.cursor()

# Create BusstopInfo
cursor.execute(
    """select a.stop, a.dayofweek, a.totalboard, b.totalalight, a.description from
(select stop, sum(pax) totalboard, dayofweek, description from (select [stop], description, b.pax, b.dayofweek from [D_BusStops] a left join F_Service b on a.stop = b.src) T1 group by stop, dayofweek, description) a
   inner join
(select stop, sum(pax) totalalight, dayofweek, description from (select [stop], description, b.pax, b.dayofweek from [D_BusStops] a left join F_Service b on a.stop = b.dst) T1 group by stop, dayofweek, description) b
on a.stop = b.stop and a.dayofweek = b.dayofweek
""")

rows = cursor.fetchall()
table = dynamodb.Table('BusStopInfo')
for row in rows:
    t = (row["stop"], row["totalboard"],row["totalalight"],row["dayofweek"],row["description"])
    #print(t)
    table.put_item(
       Item={
           'stop': row["stop"],
           'dayofweek': row["dayofweek"],
           'totalboard': row["totalboard"],
           'totalalight':row["totalalight"],
            'description': row["description"]
        }
    )

# Create NetOnBoard
cursor.execute(
    """
select ROW_NUMBER() OVER (ORDER BY a.seq) as id, a.seq, a.direction, a.stop, b.personboard, c.personalight, b.dayofweek from
  (select seq, direction, stop from D_BusRoute) a
  left join
  ( select src, sum(pax) personboard, dayofweek from F_SERVICE where src is not null  group by src, dayofweek ) b
  on a.stop = b.src /*no of people boarding at this stop*/
  left join
  ( select dst, sum(pax) personalight, dayofweek from F_SERVICE where dst is not null group by dst, dayofweek ) c
  on a.stop = c.dst and b.dayofweek = c.dayofweek /*no of people alighting at this stop*/
   order by dayofweek, direction, seq
""")

rows = cursor.fetchall()

## Example: Passed in value , direction: 1 and day flag = SUNDAY
table = dynamodb.Table('NetOnBoard')
for row in rows:
    table.put_item(
       Item={
           'id': row["id"],
           'direction': row["direction"],
           'seq': row["seq"],
           'dayofweek': row["dayofweek"],
           'stop': row["stop"],
           'personboard': row["personboard"],
           'personalight': row["personalight"]
        }
    )

cursor.close()