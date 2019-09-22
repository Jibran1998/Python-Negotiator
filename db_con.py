#For Database Connection
import mysql.connector

# for making the connection
def db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Alliswell",
        database="bot"
    )
    mydb.autocommit
    return mydb
# for seting the values to the columns
def setData(name,value):
    mydb=db()
    cursor=mydb.cursor()
    sql = "UPDATE info SET value = %s WHERE context = %s"
    val = (value, name)
    cursor.execute(sql, val)
    mydb.commit()

# for fetching the table data
def fetchData(name):
    mydb = db()
    cursor = mydb.cursor()
    sql = f"select * from {name}"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    return myresult
#for inserting the images table values
def insertImages(name,path):
    mydb = db()
    cursor = mydb.cursor()
    sql = "insert into images (name,path) values (%s,%s)"
    val = (name,path)
    cursor.execute(sql, val)
    mydb.commit()

#for deteting the data from a table
def delete(tblename,value):
    mydb=db()
    cursor=mydb.cursor()
    sql="delete from %s where id=%s"
    val = (tblename, value)
    cursor.execute(sql,val)
    print("deleted")
    mydb.commit()



