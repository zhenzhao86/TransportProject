import urllib.request #https://docs.python.org/3/library/urllib.request.html#module-urllib.request
import shutil

#  saved the zip file on my own google drive and set it to publicI
url = 'https://drive.google.com/file/d/0B2wTn6Lhv6Q4SFAybGh2cXVCYTQ/view?usp=sharing'
url = 'http://gdurl.com/jrXP' #permanent link to file hosted on google drive
file_name = 'C:/Users/Administrator/Desktop/ida-dataset/IDADataVisProjectDataSet.zip' #location to download to

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

##------------------------------------UNZIP THE FILE-----------------------------------------

import zipfile,os.path

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)

source_filename = "C:/Users/Administrator/Desktop/ida-dataset/IDADataVisProjectDataSet.zip";
dest_dir = "C:/Users/Administrator/Desktop/ida-dataset/DataSet";

unzip(source_filename, dest_dir)


##------------------------------------FORMAT THE FILES-----------------------------------------
##There are formatting problems only with the Sun and Weekday files
import csv

output = open('C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Weekday_formatted.csv','w')
with open('C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Weekday.csv', 'r') as f: #Don't open file as text, http://stackoverflow.com/questions/8515053/csv-error-iterator-should-return-strings-not-bytes
    reader = csv.reader(f)
    for row in reader:
        #for i in row:
        #    row[i].strip()
        #print (row)
        output.write(",".join(row) + "\n")
        # cursor.execute("INSERT INTO STAGING_D_WEEKDAY([src],[dst],[hr] ,[min],[km],[pax])" "VALUES (?, ?, ?, ?, ?, ?)", row) #Tried but takes too long

output = open('C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Sun_formatted.csv', 'w')
with open('C:/Users/Administrator/Desktop/ida-dataset/DataSet/12_Sun.csv',
          'r') as f:  # Don't open file as text, http://stackoverflow.com/questions/8515053/csv-error-iterator-should-return-strings-not-bytes
    reader = csv.reader(f)
    for row in reader:
        print(row)
        output.write(",".join(row) + "\n")


##------------------------------------INSERT TO DB---------------------------------

#use InsertToDb.py