import time
from emoji import emojize as e

def enid_b():
    while True:
        print("_" * 130)
        print(e(":bookmark: The Hardy Boys Series By Franklin W. Dixon:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nThe Hardy Boys Series By Franklin W. Dixon:")

        print("\n1. The Tower Treasure \n2. The House On The Cliff \n3. The Secret Of The Old Mill \n4. The Missing Chums \n5. Hunting For Hidden Gold")

        H1 = "The Tower Treasure"
        H2 = "The House On The Cliff"
        H3 = "The Secret Of The Old Mill"
        H4 = "The Missing Chums"
        H5 = "Hunting For Hidden Gold"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = H1
            print("\n",H1)
            print("\nA dying criminal confesses that his loot has been stored 'in the tower.' Both towers of the looted mansion are searched in vain. It remains for the Hardy boys to make an astonishing discovery that clears up the mystery and clears the name of a friend’s father.")
            break
        elif ch_7 == 2:
            book = H2
            print("\n",H2)
            print("\nFrank and Joe Hardy are investigating a mysterious old house high on the cliffs above Barmet Bay when they are frightened off by a scream. The boys return to the apparently haunted house when they make a connection between the place and a smuggling case their father is working on. When their father goes missing, they have to investigate the caves beneath the house and confront the smugglers.")
            break
        elif ch_7 == 3:
            book = H3
            print("\n",H3)
            print("\nWith two cases in tow, the Hardy boys look to Turner mill for clues. Determined to learn the secret of the old mill, Frank and Joe employ a clever ruse to gain entrance, only to find themselves trapped. How the young detectives extricate themselves from this dangerous situation and unravel mysteries will keep readers tense with suspense!")
            break
        elif ch_7 == 4:
            book = H4
            print("\n",H4)
            print("\nNot only is the local bank robbed, but two of the Hardy boys' pals mysteriously disappear after a masquerade party. Are the events related? How the Hardy boys use all their courage and skill to outwit the criminals provides an exciting climax to one of the most baffling mysteries the young detectives have ever encountered.")
            break
        elif ch_7 == 5:
            book = H5
            print("\n",H5)
            print("\nTimber wolves, a Rocky Mountain blizzard, and a mine cave-in are only a few of the perils Frank and Joe Hardy encounter during their search for the principal members of a notorious gang responsible for a payroll robbery. Clue by clue, Frank and Joe cleverly fit into place the scattered pieces of this dangerous puzzle and come up with the astonishing solution.")
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
