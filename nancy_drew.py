import time
from emoji import emojize as e

def enid_b():
    while True:
        print("_" * 130)
        print(e(":bookmark: The Nancy Drew Series By Carolyn Keene:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nThe Nancy Drew Series By Carolyn Keene:")

        print("\n1. The Secret Of The Old Clock \n2. The Hidden Staircase \n3. The Bungalow Mystery \n4. The Mystery At Lilac Inn \n5. The Secret Of Shadow Ranch")

        G1 = "The Secret Of The Old Clock"
        G2 = "The Hidden Staircase"
        G3 = "The Bungalow Mystery"
        G4 = "The Mystery At Lilac Inn"
        G5 = "The Secret Of Shadow Ranch"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = G1
            print("\n",G1)
            print("\nThe Secret of the Old Clock is the mystery that began it all for America's favorite teenaged slueth. The accidental rescue of a little girl who lives with her two great-aunts leads to an adventurous search for a missing will.")
            break
        elif ch_7 == 2:
            book = G2
            print("\n",G2)
            print("\nAfter receiving a call from her friend Helen Corning, Nancy agrees to help solve a baffling mystery. Helen's Aunt Rosemary has been living with her mother at the old family mansion, and they have noticed many strange things. They have heard music, thumps, and creaking noises at night, and seen eerie shadows on the walls. Could the house be haunted? \nJust as soon as she hangs up the phone, a strange man visits Nancy's house to warn her and her father that they are in danger because of a case he is working on buying property for a railroad company. This warning leads Nancy and  her father Carson to search for the missing Willie Wharton, a landowner, who can prove he signed away his land to the railroad and save the railroad from a lawsuit. Will Nancy be able to find the missing landowner and discover how these mysteries are related?")
            break
        elif ch_7 == 3:
            book = G3
            print("\n",G3)
            print("\nWhile driving a motorboat around the Twin Lakes, Nancy and her friend Helen get caught in a dangerous storm. Luckily, they are rescued by another teenage girl in a rowboat. They soon learn that their rescuer is Laura Pendleton, whose mother has recently having passed away. Laura has come to meet up with her new guardians, but something isn't quite right about them. Nancy investigates the situation, and soon she stumbles upon a shocking surprise in the cellar of a bungalow!")
            break
        elif ch_7 == 4:
            book = G4
            print("\n",G4)
            print("\nNancy and her friend Helen visit their friend Emily Willouby at the Lilac Inn, which Emily now owns, to help her plan her wedding. Emily plans on selling inherited diamonds in order to help fix up the Lilac Inn. However, Nancy soon learns that someone has been impersonating her and making expensive purchases under her name. Soon after, Emily's diamonds are stolen! Can Nancy find the thieves and recover the missing diamonds?")
            break
        elif ch_7 == 5:
            book = G5
            print("\n",G5)
            print("\nA special treat for Nancy Drew fans and any reader who's new to the series! We're releasing a stunning new edition of an old favorite: The Secret of Shadow Ranch, the fifth book in the incredibly popular, long-running series. It's the same exciting mystery that readers have fallen in love with more than 80 years--Nancy is looking forward to a fun-filled vacation at Shadow Ranch, but she soon finds herself involved in solving a baffling mystery. Now with a brand-new look, this is an edition not to miss!")
            break

    book_list = []
        
    print("\nWould You Like To: ")
    print("1. Borrow This Book (Please Note: You Can Borrow Only One Book At A Time) \n2. Keep Browsing \n3. Go To Home")
    con = int(input("Your Choice: "))
    if con == 1: 
        
        print(f"\nAdded To Your Booklist: {book}")
        print("\nWould You like to: \n1. Proceed With Logout \n2. Exchange Book")
        c = int(input("\nYour Choice: "))
        if c == 1:
            book_list.append(book)
            print(f"\nYou Have Successfully Borrowed {book}! \nYour book will be delivered to you within 36 hours.")
            print("\nLogging Out...")
            time.sleep(2)
            print("\nLogged Out.")
            import menu_1
        elif c == 2:
            import book_menu
            
        else:
            print("Invalid input")
            import menu_2
            
            
            
    elif con == 2:
        import book_menu
    elif con == 3:
        import menu_2
    elif con == 1 and len(book_list) >= 1:
        print(f"Sorry, You Must First Return {b}.")
        options()
    else:
        print("Invalid Input.")
enid_b()
