import time
from emoji import emojize as e

 
    
        
def stories():
    while True:
        print("_" * 130,)
        print(e(":bookmark: Storybooks For Toddlers:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\n1. 101 Bedtime Stories By Dreamland Publications \n2. Escargot By Dashka Slater \n3. What Are Stars By Katie Daynes \n4. Black Bird Yellow Sun By Steve Light")
        print("5. Baby Goes To Market By Atinuke \n6. A Good Day For A Hat By Nathaniel G. Fuller \n7. Hello Hello By Brendan Wenzel \n8. Each Peach Pear Plum By Allan Ahlberg and Janet Ahlberg")

        ch_5 = int(input("\nEnter Your Choice: "))

        B1 = "101 Bedtime Stories By Dreamland Publications"
        B2 = "Escargot By Dashka Slater"
        B3 = "What Are Stars By Katie Daynes"
        B4 = "Black Bird Yellow Sun By Steve Light"
        B5 = "Baby Goes To Market By Atinuke"
        B6 = "A Good Day For A Hat By Nathaniel G. Fuller"
        B7 = "Hello Hello By Brendan Wenzel"
        B8 = "Each Peach Pear Plum By Allan Ahlberg and Janet Ahlberg"

        if ch_5 == 1:
            book = B1
            print("\n",B1)
            print("\n101 Bedtime Stories- a treasure house of stories for young children. The stories, which are carefully chosen from the most popular tales are stately illustrated and written in a concise manner. Each story of this book will excite and inspire the imagination of young minds.")
        elif ch_5 == 2:
            book = B2
            print("\n",B2)
            print("\nBonjour! Escargot is a beautiful French snail who wants only two things: \n1. To be your favorite animal. \n2. To get to the delicious salad at the end of the book. \nBut when he gets to the salad, he discovers that there's a carrot in it. And Escargot hates carrots. But when he finally tries one―with a little help from you!―he discovers that it's not so bad after all! \nA charming and interactive picture book ideal for picky eaters and animal lovers alike.")
            
        elif ch_5 == 3:
            book = B3
            print("\n",B3)
            print("\nThey twinkle in the night sky, but what exactly are stars? Which one's the nearest? Can humans visit a star? Curious little children can lift over 30 flaps to find the answers to these questions and many more in this delightful introduction to stars and the night sky, with simple explanations and gorgeous illustrations on every page.")
            
        elif ch_5 == 4:
            book = B4
            print("\n",B4)
            print("\nAs a solitary black bird wings its way through the day, little ones are treated to a magnificent flight from one vibrant color to another. Inimitable illustrator Steve Light showcases a new style in this board book for the youngest readers. Children can journey with the graceful black bird and its tiny worm friend past orange leaves, through green grass, onto gray rocks, under pink flowers, and more before coming to rest beneath a brilliant blue moon.")
            
        elif ch_5 == 5:
            book = B5
            print("\n",B5)
            print("\nJoin Baby and his doting mama at a bustling southwest Nigerian marketplace for a bright, bouncy read-aloud offering a gentle introduction to numbers. \nMarket is very crowded. \nMama is very busy. \nBaby is very curious. \nWhen Baby and Mama go to the market, Baby is so adorable that the banana seller gives him six bananas. Baby eats one and puts five in the basket, but Mama doesn’t notice. As Mama and Baby wend their way through the stalls, cheeky Baby collects five oranges, four biscuits, three ears of sweet corn, two pieces of coconut . . . until Mama notices that her basket is getting very heavy! Poor Baby, she thinks, he must be very hungry by now! Rhythmic language, visual humor, and a bounty of delectable food make this a tale that is sure to whet little appetites for story time.")
            
        elif ch_5 == 6:
            book = B6
            print("\n",B6)
            print("\nMr. Brown loves hats and can't leave the house without wearing just the right one. But on this day, every time he opens the door to leave, the situation changes, and Mr. Brown must change his hat accordingly. At last, wearing every hat he owns, Mr. Brown is on his way. When he finally arrives at his destination, we find that it's Mr. Brown's birthday, and his friends have just the right hat for that as well.")
            
        elif ch_5 == 7:
            book = B7
            print("\n",B7)
            print("\nHello, Hello! is an interactive book for kids. Beginning with two cats, one black and one white, a chain of animals appears before the reader, linked together by at least one common trait. From simple colors and shapes to more complex and abstract associations, each unexpected encounter celebrates the magnificent diversity of our world and ultimately paints a story of connection.")
            
        elif ch_5 == 8:
            book = B8
            print("\n",B8)
            print("\nIn this book with your little eye, take a look and play I spy - so starts the classic story from best-selling author/illustrator team, Janet and Allan Ahlberg. Each Peach Pear Plum introduces favourite fairy tale characters, such as Tom Thumb and The Three Bears and, with a poem on each page hinting as to what is hiding in the picture, children are encouraged to participate and follow the story themselves.")
            break
        
        
        book_list = []
        
        print("\nWould You Like To: ")
        print("1. Borrow This Book (Please Note: You Can Borrow Only One Book At A Time) \n2. Keep Browsing \n3. Go To Home")
        con = int(input("\nYour Choice: "))
        if con == 1: 
            print(f"\nAdded To Your Booklist: {book}")
            print("\nWould You like to: \n1. Proceed With Logout \n2. Exchange Book")
            c = int(input("Your Choice: "))
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
                print("Invalid Input.")
                import menu_2
                
                
        elif con == 2:
            import book_menu
            
        elif con == 3:
            import menu_2
        else:
            print("Invalid Input.")
        
stories()


    
                
        


    
    



    
