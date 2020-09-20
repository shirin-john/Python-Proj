import time
from emoji import emojize as e

def alph():
    while True:
        print("_" * 130)
        print(e(":bookmark: Alphabet Books:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nAlphabet Books:")

        print("\n1. Dr. Seuss's ABC By Dr. Seuss \n2. Eating The Alphabet By Lois Ehlert \n3. 10 Little Rubber Ducks By Eric Carle \n4. One duck Stuck By Phyllis Root \n5. Curious George Learns To Count From 1 To 100 By H. A. Rey")
        print("6. On the Launch Pad: A Counting Book About Rockets (Know Your Numbers) By Michael Dahl \n7. One Two Three By Tom Slaughter \n8. Animalphabet By Julia Donaldson")
        A1 = "Dr. Seuss's ABC By Dr. Seuss"
        A2 = "Eating The Alphabet By Lois Ehlert"
        A3 = "10 Little Rubber Ducks By Eric Carle"
        A4 = "One duck Stuck By Phyllis Root"
        A5 = "Curious George Learns To Count From 1 To 100 By H. A. Rey"
        A6 = "On the Launch Pad: A Counting Book About Rockets (Know Your Numbers) By Michael Dahl"
        A7 = "One Two Three By Tom Slaughter"
        A8 = "Animalphabet By Julia Donaldson"

        ch_4 = int(input("\nPlease Enter Your Choice: "))

        if ch_4 == 1:
            book = A1
            print("\n",A1)
            print("\nLetters come alive on the page, as Dr. Seuss fills the alphabet with his classic colorful characters, from dreaming David Donald Doo to itchy Ichabod to the quick Queen of Quincy, and of course the  Zizzer-Zazzer-Zuzz. Starting with the most basic building blocks of language, Dr. Seuss makes reading FUN!\nBIG A \nlittle a \nWhat begins with A?")
            break
        elif ch_4 == 2:
            book = A2
            print("\n",A2)
            print("\nA popular alphabet storybook is presented in a sturdy, easy-to-hold board-book edition for the youngest readers and highlights vivid collage illustrations of colorful apples, blueberries, carrots, yams, and zucchini.")
            break
        elif ch_4 == 3:
            book = A3
            print("\n",A3)
            print('\nAhoy! All aboard for a world of learning and fun! \n"Ducks overboard!" shouts the captain, as a giant wave washes a box of 10 little rubber ducks off his cargo ship and into the sea. The ducks are swept away in various directions. One drifts west, where a friendly dolphin jumps over it. A whale sings to another. But as the sun sets, the 10th little rubber duck is left all alone, bobbing helplessly on the big wide sea. Small readers and listeners will empathize with the little'" duck's plight—and will rejoice at the heartwarming surprise ending.")
            break
        elif ch_4 == 4:
            book = A4
            print("\n",A4)
            print("\nCount all of the animals who come splishing, plunking, slooshing to the rescue in this counting board book!\nCan two fish, tails going swish, help? Will three moose, munching on spruce, be able to pull the unlucky duck out of the muck? Perfectly sized for small hands, this counting rhyme is a feast of sounds and numbers that will have young listeners scrambling to join the slippy, sloppy fun!")
            break
        elif ch_4 == 5:
            book = A5
            print("\n",A5)
            print("\nCurious George is a good little monkey, and always very curious. Now George is curious about numbers. Counting from 1 to 10 is easy, but can he count all the way to 100? George has picked the perfect day to try. It’s his town’s 100th birthday today and everyone is coming out to celebrate!")
            break
        elif ch_4 == 6:
            book = A6
            print("\n",A6)
            print("\n3 . . . 2 . . . 1 . . . blastoff! In award-winning author Michael Dahl's, On the Launch Pad: A Counting Book About Rockets, a space shuttle awaits liftoff. Each page features bright illustrations with hidden numbers in the artwork to introduce the concept of counting. This exciting combination of outer space and math keeps readers flipping the pages and counting along.")
            break
        elif ch_4 == 7:
            book = A7
            print("\n",A7)
            print("\nCreated in deceptively simple paper cuts, this is a counting book with a difference: each image is not only an introduction to numerals but also to the shapes and colors of modern art. Small children, and those with an interest in modern art, will find much to enjoy in this gorgeous picture book.")
            break
        elif ch_4 == 8:
            book = A8
            print("\n",A8)
            print("\nAn interactive animal ABC guessing game with peep-through pages and amazing fold-out flaps, by the bestselling Julia Donaldson, author of The Gruffalo, and visionary illustrator Sharon King-Chai.\nWith eye-catching artwork and an exotic array of animals to marvel over, this is a gorgeous book to treasure – can you guess who has more legs than a butterfly? And who is wrinklier than a hedgehog?\nEach page draws you further into a beautifully vibrant world of huge elephants, slithery snakes and growling tigers, inviting you to compare one animal to another and learn comparison words and adjectives from the natural world.")
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
            
            import menu_2
            
            
    elif con == 2:
        import book_menu
        
    elif con == 3:
        import menu_2
    else:
        print("Invalid Input.")
        import menu_2
alph()


        

        
            
