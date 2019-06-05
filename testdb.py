
import mysql.connector

def testlogs():
    mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS bio_logs")
    mydb.commit()
    mycursor.execute("CREATE TABLE IF NOT EXISTS  bio_logs (id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255),user_id int,timestamp TIMESTAMP unique , status VARCHAR(255), punch VARCHAR(255))")
    # payload = {"ATT":counter, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
    sql = "INSERT INTO bio_logs (uid, user_id,status,timestamp,punch) VALUES (%s, %s,%s, %s,%s)"
    val = ("cc", 1,"cc", "ccs","ccd")
    try:
        pass
        # v = mycursor.execute(sql, val)
        # mydb.commit()
        # print v
    except Exception as ex:
        print ex

def test():
    mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS users_bio")
    mydb.commit()
    mycursor.execute("CREATE TABLE IF NOT EXISTS  users_bio (id INT AUTO_INCREMENT PRIMARY KEY, user_id  int,timestamp VARCHAR(255), employee_no VARCHAR(255))")
    # payload = {"ATT":counter, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
    sql = "INSERT INTO users_bio (user_id,employee_no,timestamp) VALUES (%s, %s,%s)"
    val = (1, "cc","cc")
    try:
        v = mycursor.execute(sql, val)
        # mydb.commit()
        print v
    except Exception as ex:
        print ex
test()
testlogs()
