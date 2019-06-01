
import mysql.connector

def testlogs():
    mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS logs")
    mydb.commit()
    mycursor.execute("CREATE TABLE IF NOT EXISTS  logs (id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255), user_id  VARCHAR(255),timestamp VARCHAR(255), status VARCHAR(255), punch VARCHAR(255))")
    # payload = {"ATT":counter, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
    sql = "INSERT INTO logs (uid, user_id,status,timestamp,punch) VALUES (%s, %s,%s, %s,%s)"
    val = ("cc", "cc","cc", "ccs","ccd")
    try:
        v = mycursor.execute(sql, val)
        mydb.commit()
        print v
    except Exception as ex:
        print ex

def test():
    mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS logs")
    mydb.commit()
    mycursor.execute("CREATE TABLE IF NOT EXISTS  users_bio (id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255), user_id  VARCHAR(255),timestamp VARCHAR(255), status VARCHAR(255), punch VARCHAR(255))")
    # payload = {"ATT":counter, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
    sql = "INSERT INTO users_bio (uid, user_id,status,timestamp,punch) VALUES (%s, %s,%s, %s,%s)"
    val = ("cc", "cc","cc", "ccs","ccd")
    try:
        v = mycursor.execute(sql, val)
        mydb.commit()
        print v
    except Exception as ex:
        print ex
test()
testlogs()
