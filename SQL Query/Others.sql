select sum(pax) as totalboard, src as BusStop from F_Service group by src order by src /*Number of people boarding at each bus stop*/
select sum(pax) as totalalight, dst as BusStop from F_Service group by dst order by dst /*Number of people alighting at each bus stop*/

/*Task 3a: For populating BusStopInfo. Key is stop and dayofweek*/
select a.stop, a.dayofweek, a.totalboard, b.totalalight, a.description from
(select stop, sum(pax) totalboard, dayofweek, description from (select [stop], description, b.pax, b.dayofweek from [D_BusStops] a left join F_Service b on a.stop = b.src) T1 group by stop, dayofweek, description) a
   inner join
(select stop, sum(pax) totalalight, dayofweek, description from (select [stop], description, b.pax, b.dayofweek from [D_BusStops] a left join F_Service b on a.stop = b.dst) T1 group by stop, dayofweek, description) b
on a.stop = b.stop and a.dayofweek = b.dayofweek

/*src=dst pairs for dayofweek, ignoring all time*/
select src, dst, sum(pax) NoPersons, dayofweek from F_SERVICE where src is not null and dst is not null group by src, dst, dayofweek 

/*Bus stops in sequence*/
select seq, direction, stop from D_BusRoute order by direction, seq

/*Task 3b: No of passengers board/alight at each stop*/
select ROW_NUMBER() OVER (ORDER BY a.seq) as id, a.seq, a.direction, a.stop, b.personboard, c.personalight, b.dayofweek from
(select seq, direction, stop from D_BusRoute) a
left join
( select src, sum(pax) personboard, dayofweek from F_SERVICE where src is not null  group by src, dayofweek ) b
on a.stop = b.src /*no of people boarding at this stop*/
left join
( select dst, sum(pax) personalight, dayofweek from F_SERVICE where dst is not null group by dst, dayofweek ) c
on a.stop = c.dst and b.dayofweek = c.dayofweek /*no of people alighting at this stop*/
order by dayofweek, direction, seq