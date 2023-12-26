import csv
import pymysql

db = pymysql.connect(host = "127.0.0.1", user = "root", password = "6836", db = "ksie", charset = "utf8mb4")
cursor = db.cursor()
count = 0
f = open('KSIE_keyword_no_overlap.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)
for line in rdr:
    try:
        cursor.execute("INSERT INTO ksie_tf_df values (%s, %s, %s);", (line[0],line[1],line[2]))
        db.commit()
        count += 1
        if count%100 == 0:
            print(count)
    except:
        pass
f.close()
print(count)