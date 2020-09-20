import time
from emoji import emojize as e

def roald_d():
    while True:
        print("_" * 130)
        print(e(":bookmark: Books By Roald Dahl:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nBooks By Roald Dahl:")

        print("\n1. Charlie And The Chocolate Factory \n2. Charlie And The Great Glass Elevator \n3. Matilda \n4. The BFG \n5. The Witches")
        print("6. James And The Giant Peach")
        E1 = "Charlie And The Chocolate Factory"
        E2 = "Charlie And The Great Glass Elevator"
        E3 = "Matilda"
        E4 = "The BFG"
        E5 = "The Witches"
        E6 = "James And The Giant Peach"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = E1
            print("\n",E1)
            print("\nRoald Dahl has been widely acclaimed for his portrayal of children and their ability of acting as adults. This book captures the adventures of Charlie bucket, who is a poor kid living with his family. Charlie is one of the five kids who gets a golden ticket inside the company, 'Wonka chocolate' owned by Willy Wonka. Those five kids get an entry inside the Wonka factory. Charlie visits the factory along with his grandfather and gets to experience a lot of adventures inside. The other four kids are later eliminated through hilarious, but painful ways. Will Charlie survive the test? Will he be able to see everything that is to be seen? Readers get a taste of an unusual relationship between a shrewd businessman and a kind kid. In the end, the truth about Wonka is revealed. Why did he host such a competition among kids? The book has all the answers.")
            break
        elif ch_7 == 2:
            book = E2
            print("\n",E2)
            print("\nLast seen flying through the sky in a giant elevator in Charlie and the Chocolate Factory, Charlie Bucket's back for another adventure. When the giant elevator picks up speed, Charlie, Willy Wonka, and the gang are sent hurtling through space and time. Visiting the world’' first space hotel, battling the dreaded Vermicious Knids, and saving the world are only a few stops along this remarkable, intergalactic joyride.")
            break
        elif ch_7 == 3:
            book = E3
            print("\n",E3)
            print("\nA very popular story in Children’s Literature of all times, ‘Matilda’ introduces the readers to the universe of Matilda Wormwood, the main female protagonist in this masterpiece. In spite of having special abilities and being more intelligent than others of her age, she was necessarily overlooked by her lazy brother and torturous parents who constantly humiliated her for pursuing educational activities. \nThe only person who loves and adores this little girl with extraordinary telekinetic powers and intellect is Mr. Honey, her teacher and her friends at school. Even her school’s headmistress Miss Trunchball does not keep a good faith in Matilda and never leaves an opportunity to punish her. Thanks to Matilda’s inner resources, she is able to deal with one and all. In this hilarious tale of child simplicity and magic, will Matilda be able to fight the demons? \nAppreciated by critics and readers alike, Matilda is a fun-filled tale that will take the readers on a hilarious ride to the inner world of a simple child with extraordinary powers and towering intellect.")
            break
        elif ch_7 == 4:
            book = E4
            print("\n",E4)
            print("\nThe BFG is no ordinary bone-crunching giant. He is far too nice and jumbly. It's lucky for Sophie that he is. Had she been carried off in the middle of the night by the Bloodbottler, or any of the other giants—rather than the BFG—she would have soon become breakfast. When Sophie hears that the giants are flush-bunking off to England to swollomp a few nice little chiddlers, she decides she must stop them once and for all. And the BFG is going to help her!")
            break
        elif ch_7 == 5:
            book = E5
            print("\n",E5)
            print("\nThis is not a fairy-tale. This is about real witches. Real witches don't ride around on broomsticks. They don't even wear black cloaks and hats. They are vile, cunning, detestable creatures who disguise themselves as nice, ordinary ladies. So how can you tell when you're face to face with one? Well, if you don't know yet you'd better find out quickly-because there's nothing a witch loathes quite as much as children and she'll wield all kinds of terrifying powers to get rid of them.")
            break
        elif ch_7 == 6:
            book = E6
            print("\n",E6)
            print("\nWhen James accidentally drops some magic crystals by the old peach tree, strange things start to happen. The peach at the top of the tree begins to grow, and before long it's as big as a house. When James discovers a secret entranceway into the fruit and crawls inside, he meets wonderful new friends--the Old-Green-Grasshopper, the dainty Ladybug, and the Centipede of the multiple boots. After years of feeling like an outsider in his aunts' house, James finally found a place where he belongs. With a snip of the stem, the peach household starts rolling away--and the adventure begins!")
            break

    book_list = []
        
    print("\nWould You Like To: ")
    print("1. Borrow This Book (Please Note: You Can Borrow Only One Book At A Time) \n2. Keep Browsing \n3. Go To Home")
    con = int(input("Your Choice: "))
    if con == 1: 
        book_list.append(book)
        print(f"\nAdded To Your Booklist: {book}")
        print("\nWould You like to: \n1. Proceed With Logout \n2. Exchange Book")
        c = int(input("\nYour Choice: "))
        if c == 1:
            print(f"\nYou Have Successfully Borrowed {book}! \nYour book will be delivered to you within 36 hours.")
            print("\nLogging Out...")
            time.sleep(2)
            print("\nLogged Out.")
            import menu_1
            
        else:
            print("Invalid input")
            import book_menu
            
            
            
    elif con == 2:
        import book_menu
    elif con == 3:
        import menu_2
    elif con == 1 and len(book_list) >= 1:
        print(f"Sorry, You Must First Return {b}.")
        options()
    else:
        print("Invalid Input.")
roald_d()
