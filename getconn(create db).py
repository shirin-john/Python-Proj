import mysql.connector as my


mydb = my.connect(host ="localhost",
                  user = "root",
                  passwd = "")
                  #database = "little_readers")
                      
if mydb:
    print("\nConnected To Server")
else:
    print("\nFailed To Connect")


mycur = mydb.cursor()
mycur.execute("Create Database readers")
#mycur.execute("Create Table readers (user varchar(50), dob varchar(15), age int(2), parent varchar(50), email varchar(50), password int(4), valifity varchar (15), join_date varchar(15), address varchar(120), postal_code int(6))")
mydb.close



    




    


