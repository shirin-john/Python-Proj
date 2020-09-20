import time
from emoji import emojize as e

def classics():
    while True:
        print("_" * 130)
        print(e(":bookmark: Indian Classics:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nIndian Classics:")

        print("\n1. The Best Of Akbar-Birbal \n2. The fabulous Sheikh Chilli \n3. Moral Stories \n4. 101 Panchatantra Stories \n5. Grandma's Bag Of Stories By Sudha Murthy")
        print("6. The Best Of Mulla Nasruddin \n7. The Best Of Tenali Rama")
        D1 = "The Best Of Akbar-Birbal"
        D2 = "The fabulous Sheikh Chilli"
        D3 = "Moral Stories"
        D4 = "101 Panchatantra Stories"
        D5 = "Grandma's Bag Of Stories By Sudha Murthy"
        D6 = "The Best Of Mulla Nasruddin"
        D7 = "The Best Of Tenali Rama"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = D1
            print("\n",D1)
            print("\nThe best of akbar-birbal is a collection of short, vividly illustrated stories of akbar-birbal, whose relationship had many a tale to share. Akbar-birbal stories are an integral part of rich Indian heritage. These stories are not only entertaining but also contain lots of lessons.")
            break
        elif ch_7 == 2:
            book = D2
            print("\n",D2)
            print("\nSheikh Chilli is often named when talking about fools and daydreamers. His tales have been popular among people of different nationalities and classes. His casual attitude and a fondness for building air castles have not just entertained people for centuries, but have also been inspiration for many other stories and characters. Here are a few fabulous stories of Sheikh Chilli, who can be easily termed as the biggest fool of all. Indeed, the book would prove to be not an easy task to turn down until it is read completely.")
            break
        elif ch_7 == 3:
            book = D3
            print("\n",D3)
            print("\nThis book encloses in its pages poignant stories with relevant moral messages for the young readers. The friendly people and vivacious animal characters in these stories help us to learn important life lessons through their own examples of success or defeat, selfless help or selfish vile and through the twists and turns in the situations that present themselves. There is a moral to every story with a positive lesson, told in a friendly, subtle way to touch the young hearts and tickle the curious minds.")
            break
        elif ch_7 == 4:
            book = D4
            print("\n",D4)
            print("\n101 Panchatantra Stories- a collection of all-time favourite stories written for children. These stories teach us lessons about wisdom, courage, bravery, wickedness and so on. Compiled in simple language, supported by beautiful illustrations each story of this book makes the reading on enjoyable experience.")
            break
        elif ch_7 == 5:
            book = D5
            print("\n",D5)
            print("\nMemories of a grandparent spinning tales around animals and mysterious characters have kept many of us rapt till date. Sudha Murty's Grandma’s Bag of Stories is simply delightful. The story starts with Anand, Krishna, Raghu and Meena arriving at their grandparents’ house in Shiggaon. Overjoyed Ajji and Ajja(Grandmother and grandfather in Kannada) get the house ready, while Ajji prepares delicious snacks for children. Finally, times comes when everyone gathers around Ajji, as she opens her big bag of stories. She tells stories of kings and cheats, princesses and onions, monkeys and mice and scorpions and hidden treasures.")
            break
        elif ch_7 == 6:
            book = D6
            print("\n",D6)
            print("\nThe Best of Mulla Nasruddin by Mrs Rungeen Singh is a prominent compilation of interesting, treasured and entertaining stories of Mulla Nasruddin who is believed to have lived during the thirteenth century. He is considered to be a populist philosopher remembered for his funny stories and anecdotes. This compilation has some of these stories and anecdotes written in simple language.")
            break
        elif ch_7 == 7:
            book = D7
            print("\n",D7)
            print("\nSri Krishna Deva rayalu, one of the rulers of the ancient Indian kingdom of Vijayanagar, had transformed his regime into a golden era. His Court poet, named Tenali Rama, added to the reputation of the kingdom. Rayalu’s Court hosted discussions, arguments, and competitions of the learned men. Thus, were born the stories of Tenali Rama. These lively stories spread the message of wit and intellect, through the sharp humour of Tenali Rama, puncturing the pride of people, including his own king.")
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
            import book_menu
            
            
            
    elif con == 2:
        import book_menu
    elif con == 3:
        import menu_2
    
    else:
        print("Invalid Input.")
classics()
