import getconn
from datetime import date
from emoji import emojize as e

class n_member:
    def __init__(self):
        self.mydb = getconn.getconn()
        self.mycur = self.mydb.cursor()

        

    def add_member(self):
        while True:
            try:
                print("_" * 130)
                print(e(":bookmark: Make Your Child A Little Reader!"))
                f_name = input("\nFirst Name Of Child: ")
                l_name = input("Last Name Of Child: ")
                self.usern = f_name + "_" + l_name
                print(f"Please Note: '{self.usern}' Will Be Your Username.")
                
                dob_y = int(input("\nDate Of Birth - Year: ")) #date of birth: day
                dob_m = int(input("               Month: ")) #date of birth: month
                dob_d = int(input("                 Day: ")) #date of birth: year

                self.dob = "{}-{}-{}".format(dob_y,dob_m,dob_d)

                d = date.today()
                self.d = d
                
            
                if (d.year - dob_y) <= 13:
                    self.age = (d.year - dob_y) 
            
                elif (d.year - dob_y) > 13:
                    print("\nWe Are So Sorry! \nIn Order To Be A Little Reader, Your Child Must Not Be More Than Thirteen Years Of Age.")
                    print("\nWould You Like To:")
                    print("1. Add Another Member \n2. Go Back To Home \n3. Exit")
                    c = int(input("Your Choice: "))
                    if c == 1:
                        continue
                    elif c == 2:
                        pass
                    elif c == 3:
                        print("\nThank You For Visiting Little Readers!")
                        pass
                
                
                self.par = input("\nEnter Parent/Guardian Name: ") #name of parent/guardian
                
                self.email = input("Enter Email ID: ")
                
                n_pass = int(input("Enter A 4-Digit Password: ")) #new password
                
                
                #password must be 4 digits only
                if n_pass < 1000 or n_pass > 9999:
                    print("Invalid Input. Password Must Be 4 Digits. Please Try Again.")
                    continue
                n_pass1 = int(input("Confirm Password: ")) #password confirmation
                
                
                if n_pass1 < 1000 or n_pass1 > 9999:
                    print("Invalid Input. Password Must Be 4 Digits. Please Try Again.")
                    continue
                
                #password match
                if n_pass == n_pass1:
                    self.passw = n_pass
                    
                else:
                    print("Your Passwords Don't Seem To Match. Please Try Again.")
                    continue

                print("\nPlease Select A Membership.")
                print("\n   MEMBERSHIP     PRICE")
                print("\n1. Monthly        Rs.400 \n2. Bi-Monthly     Rs.700 \n3. Quarterly      Rs.1000 \n4. Half-Yearly    Rs.1400 \n5. Yearly         Rs.2400")
                ch_2 = int(input("\nEnter your Choice: ")) 

                if ch_2 == 1:
                    self.validity = "Monthly"
                    print("You Have Chosen: ",self.validity)
                    fee = 400 #monthly membership fee
                    pass
                elif ch_2 == 2:
                    self.validity = "Bi-Monthly"
                    print("You Have Chosen: ",self.validity)
                    fee = 700 #bi-monthly membership fee 
                    pass
                elif ch_2 == 3:
                    self.validity = "Quarterly"
                    print("You Have Chosen: ",self.validity)
                    fee = 1000 #quarterly membership fee 
                    pass
                elif ch_2 == 4:
                    self.validity = "Half-Yearly"
                    print("You Have Chosen: ",self.validity)
                    fee = 1400 #half-yearly membership fee
                    pass
                elif ch_2 == 5:
                    self.validity = "Yearly"
                    print("You Have Chosen: ",self.validity)
                    fee = 2400 #yearly membership fee
                    pass
                else:
                    print("Invalid Input. Please Try Again.")
                    continue
                
                print("\nPayment Method:")
                print("1. Credit \n2. Debit")
                pay = int(input("\nYour Choice: "))
                if pay == 1:
                    while True:
                        cr_no = int(input("\nCredit Card No.: "))
                        cr_n = input("Name On Credit Card: ")
                        exp_y = input("Card Expiry - Year:")
                        exp_m = input("             Month:")
                        cvv = int(input("CVV Number: "))
                        if len(str(cvv)) > 3:
                            print("Error. 3-Digit Value Required.")
                        else:
                            print(f"\nThank You. \nYour Payment Of Rs.{fee} Was Successful.")
                            break
                if pay == 2:
                    while True:
                        deb_no = int(input("\nDebit Card No.: "))
                        deb_n = input("Name On Debit Card: ")
                        ex_y = input("Card Expiry - Year: ")
                        ex_m = input("             Month: ")
                        cvv = int(input("CVV Number: "))
                        if len(str(cvv)) > 3:
                            print("Error. 3-Digit Value Required.")
                        else:
                            print(f"\nThank You. \nYour Payment Of Rs.{fee} Was Successful.")
                            break
                    else:
                        print("Payment Unsuccessful. Please Try Again.")
                        continue
                
                        
                    
                self.add = input("\nEnter Your Postal Address: ")
                self.code = int(input("Enter Your Postal Code: "))

                
                
            
                sql = "insert into readers values('{}','{}',{},'{}','{}',{},'{}','{}','{}',{})".format(self.usern,
                                                                                                       self.dob,
                                                                                                       self.age,
                                                                                                       self.par,
                                                                                                       self.email,
                                                                                                       self.passw,
                                                                                                       self.validity,
                                                                                                       self.d,
                                                                                                       self.add,
                                                                                                       self.code)                                                                                                                   
                                                                              
                self.mycur.execute(sql)
                
                if self.mycur.rowcount > 0:
                    self.mydb.commit()
                    print(e("\nCongratulations! \nYour Child is now a Little Reader."))
                    break
                else:
                    print("Error While Adding Details")
                    self.mydb.rollback
                    break
                
            except Exception as err:
                print(err)
                print("Failed")

            except:
                print("Please Enter Valid Details")
                break

            

    
            

    

if __name__ == '__main__':
    n = n_member()
    n.add_member()

    


    

    

