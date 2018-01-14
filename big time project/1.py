'''
import mysql.connector
conn=mysql.connector.connect(user='root',password='developer17',host='localhost',database='Users')
cursor=conn.cursor()
cursor.execute('create table masteruser(username varchar(30),password varchar(30),emailid varchar(50),dateofbirth varchar(20),mobile varchar(10),nationality varchar(80),permanentaddress varchar(200),securityquestion varchar(100),answer varchar(12),creditcardno varchar(12));')
conn.commit()
'''
