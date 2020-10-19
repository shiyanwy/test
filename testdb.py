import mariadb
import sys
import youdao

#connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="test"
    )
except mariadb.Error as e:
    print("Error connection to MariaDB Platform: {}".format(e))
    sys.exit(1)

#Get Cursor
cur = conn.cursor()

#Retrieving informat
try:
    cur.execute("select wname, wpartofspeech, wannotation from words where wbook=? and wunit=?", ('090','4'))
except mariadb.Error as e:
    print("Error: {}".format(e))

#Commit data
#conn.commit()

#Output
for r in cur:
    sp = youdao.youdao()
    sp.down(r[0])
    print(r)

#Close connection
cur.close()
conn.close()