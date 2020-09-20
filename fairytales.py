import time
from emoji import emojize as e

def fairytale():
    while True:
        print("_" * 130)
        print(e(":bookmark: Fairytales:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nFairytales:")

        print("\n1. Beauty And The Beast \n2. Cinderella \n3. The Little Mermaid \n4. Sleeping Beauty \n5. Snow White")
        print("6. Lady And The Tramp")
        C1 = "Beauty And The Beast"
        C2 = "Cinderella"
        C3 = "The Little Mermaid"
        C4 = "Sleeping Beauty"
        C5 = "Snow White"
        C6 = "Lady And The Tramp"


        ch_6 = int(input("\nPlease Enter Your Choice: "))

        if ch_6 == 1:
            book = C1
            print("\n",C1)
            print("\nCome be our guest in the Beast’s castle where teapots talk, spoons dance, and beautiful Belle discovers that things are never quite as they seem. Disney’s Beauty and the Beast is retold in the classic Little Golden Book format.")
            break
        elif ch_6 == 2:
            book = C2
            print("\n",C2)
            print("\nThe most beloved princess movie of all time—Disney's Cinderella—is retold in the classic Little Golden Book format. It's perfect for Disney Princess fans ages 2-5.")
            break
        elif ch_6 == 3:
            book = C3
            print("\n",C3)
            print("\nMore than anything else, Princess Ariel longs to visit the world of humans. She even falls in love with a human named Prince Eric But will the Little Mermaid remain with the prince of her dreams without losing everything she loves?")
            break
        elif ch_6 == 4:
            book = C4
            print("\n",C4)
            print("\nWhen Briar Rose turns 16, she learns that she is actually Princess Aurora—and that an evil fairy cast a spell on her! Children ages 3 to 7 and all Disney Princess fans will love this beautiful hardcover storybook retelling of Disney's beloved classic Sleeping Beauty!")
            break
        elif ch_6 == 5:
            book = C5
            print("\n",C5)
            print("\nNow new and old fans can relive the magic of this beloved film as it is retold in a beautiful full-color Little Golden Book!")
            break
        elif ch_6 == 6:
            book = C6
            print("\n",C6)
            print("\nWhat do you get when you combine a dog from the wrong side of the tracks with a pampered pooch? One of the most beloved animated films of all time! Disney's Lady and the Tramp is being rereleased as a Diamond Edition Blu-Ray and DVD in spring 2012. New and old fans of the movie will love the full-color Little Golden Book retelling of this delightful doggie tale.")
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
            
        else:
            print("Invalid Input")
            import menu_2            
            
    elif con == 2:
        import book_menu
        
    elif con == 3:
        import menu_2
    else:
        print("Invalid Input.")
        import menu_2
        
fairytale()
