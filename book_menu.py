from emoji import emojize as e
import getconn


def book_m():
    while True:
        print("_" * 130)
        print(e("\t\t\t:books: Our Collections :books:"))

        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")

        print("\n1.  Alphabet And Number Books \n2.  Storybooks For Toddlers \n3.  Fairy Tales \n4.  Indian Classics \n5.  Books By Roald Dahl \n6.  Books By Enid Blyton \n7.  The Nancy Drew Series By Carolyn Keene \n8.  The Hardy Boys Series By Franklin W. Dixon \n9.  The Harry Potter Series By J. K. Rowling")
        ch_3 = int(input("\nPlease Enter Your Choice: "))

        
        if ch_3 == 1:
            import alphabet_books 
            
            break
        elif ch_3 == 2:
            import storybooks
            
            break
        elif ch_3 == 3:
            import fairytales
            
        elif ch_3 == 4:
            import ind_classics
            
        elif ch_3 == 5:
            import roald_dahl
            
        elif ch_3 == 6:
            import enid_blyton
            
        elif ch_3 == 7:
            import nancy_drew
            
        elif ch_3 == 8:
            import hardy_boys
            
        elif ch_3 == 9:
            import harry_potter
    
        else:
            print("Invalid Input. Please Try Again")
book_m()
    
        
