import time
from emoji import emojize as e

def enid_b():
    while True:
        print("_" * 130)
        print(e(":bookmark: Books By Enid Blyton:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nBooks By Enid Blyton:")

        print("\n1. Five On A Treasure Island \n2. Five Go Adventuring Again \n3. Five Go To Smuggler's Top \n4. Five Go Off In A Caravan \n5. Five On Kirrin Island Again")
        print("6. The Enchanted Wood \n7. The Magic Faraway Tree \n8. The Folk Of The Faraway Tree")
        F1 = "Five On A Treasure Island"
        F2 = "Five Go Adventuring Again"
        F3 = "Five Go To Smuggler's Top"
        F4 = "Five Go Off In A Caravan"
        F5 = "Five On Kirrin Island Again"
        F6 = "The Enchanted Wood"
        F7 = "The Magic Faraway Tree"
        F8 = "The Folk Of The Faraway Tree"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = F1
            print("\n",F1)
            print("\nMeet Julian, Dick, Anne, George and Timothy. Together they are THE FAMOUS FIVE - in Enid Blyton's most popular adventure series. \n'There was something else out on the sea by the rocks - something dark that seemed to lurch out of the waves . . . What could it be?' \nJulian, Dick and Anne are spending the holidays with their tomboy cousin George and her dog, Timothy. One day, George takes them to explore nearby Kirrin Island, with its rocky little coast and old ruined castle on the top. \nOver on the island, they make a thrilling discovery, which leads them deep into the dungeons of Kirrin Castle on a dangerous adventure. Who - and what - will they find there?")
            break
        elif ch_7 == 2:
            book = F2
            print("\n",F2)
            print("\nMeet Julian, Dick, Anne, George and Timothy. Together they are THE FAMOUS FIVE - Enid Blyton's most popular adventure series. \nIn their second adventure, the Famous Five find a thief at Kirrin Cottage. They think they know who it is, but need to prove it. \nWill the discovery of a very old map help uncover the true culprit?")
            break
        elif ch_7 == 3:
            book = F3
            print("\n",F3)
            print("\nMeet Julian, Dick, Anne, George and Timothy. Together they are THE FAMOUS FIVE - Enid Blyton's most popular adventure series. \nIn book four, the Famous Five stay at the large old house at Smuggler's Top. They discover secret hiding places, underground tunnels, and one night they catch people signalling out to sea! \nAre there still smugglers at Smuggler's Top?")
            break
        elif ch_7 == 4:
            book = F4
            print("\n",F4)
            print("\nMeet Julian, Dick, Anne, George and Timothy. Together they are THE FAMOUS FIVE - Enid Blyton's most popular adventure series. \nIn book five, the Famous Five go on a caravan holiday. When they stumble across a circus troupe, the gang are thrilled. \nBut some of the circus people have more sinister plans than just clowning around...")
            break
        elif ch_7 == 5:
            book = F5
            print("\n",F5)
            print("\nMeet Julian, Dick, Anne, George and Timothy. Together they are THE FAMOUS FIVE - Enid Blyton's most popular adventure series. \nIn book six, Uncle Quentin has locked himself away on Kirrin Island. What's he up to and why won't he let anyone visit? Then the Famous Five discover that a suspicious stranger is watching Uncle Quentin's every move. \nCan the Famous Five warn Uncle Quentin in time?")
            break
        elif ch_7 == 6:
            book = F6
            print("\n",F6)
            print("\nCome on a journey full of magic and adventure in THE MAGIC FARAWAY TREE! \nWhen Joe, Beth and Frannie move to a new home, an Enchanted Wood is on their doorstep. And when they discover the Faraway Tree, that is the beginning of many magical adventures! Join them and their friends Moonface, Saucepan Man and Silky the fairy as they discover which new land is at the top of the Faraway Tree. Will it be the Land of Birthdays, the Land of Toys, or even the Land of Ice and Snow with its magic snowman?")
            break
        elif ch_7 == 7:
            book = F7
            print("\n",F7)
            print("\nCome on a journey full of magic and adventure! \nJoin Joe, Beth and Fannie as they take their cousin Rick on a an adventure he’ll never forget up the Magic Faraway Tree! Along with their friends Moon-Face, Saucepan Man and Silky the fairy, the children tumble from the fun of the Land of Toys to the thrill of trying to escape the Land of Dreams. Will they ever make it home for tea? \nAnything's possible in THE MAGIC FARAWAY TREE!")
            break
        elif ch_7 == 8:
            book = F8
            print("\n",F8)
            print("\n'A land at the top of a tree!' said Connie. 'I don't believe a word of it.' \nJo, Bessie and Fanny are fed up when Connie comes to stay - she's so stuck-up and bossy. But they don't let her stop them having fun with their tree-friends, Silky, Moon-Face and the Saucepan Man. Together they climb through the cloud at the top of the Faraway Tree and visit the wonderful places there, the Land of Secrets and the Land of Treats - and Connie learns to behave herself!")
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
