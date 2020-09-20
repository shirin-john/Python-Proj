import mysql.connector as my

def getconn():
    mydb = my.connect(host ="localhost",
                      user = "root",
                      passwd = "",
                      database = "little_reader")

    if mydb:
        print("\nConnected To Server")
    else:
        print("\nFailed To Connect")
        
    return mydb
                      
    







    




    


