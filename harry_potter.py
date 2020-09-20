import time
from emoji import emojize as e

def enid_b():
    while True:
        print("_" * 130)
        print(e(":bookmark: The Harry Potter Series By J. K. Rowling:"))
        print("\n*Please Note: You Can Borrow Only One Book At A Time. Once You have Borrowed A Book, You May Log Out Or Exchange Your Book.")
        print("\nThe Harry Potter Series By J. K. Rowling:")

        print("\n1. Harry Potter And The Philosopher's Stone \n2. Harry Potter And The Chamber Of Secrets \n3. Harry Potter And The Prisoner Of Azkaban \n4. Harry Potter And The Goblet Of Fire") 
        print("5. Harry Potter And The Order Of The Phoenix \n6. Harry Potter And The Half Blood Prince \n7. Harry Potter And The Deathly Hallows")
        
        I1 = "Harry Potter And The Philosopher's Stone"
        I2 = "Harry Potter And The Chamber Of Secrets"
        I3 = "Harry Potter And The Prisoner Of Azkaban"
        I4 = "Harry Potter And The Goblet Of Fire"
        I5 = "Harry Potter And The Order Of The Phoenix"
        I6 = "Harry Potter And The Half Blood Prince"
        I7 = "Harry Potter And The Deathly Hallows"


        ch_7 = int(input("\nPlease Enter Your Choice: "))

        if ch_7 == 1:
            book = I1
            print("\n",I1)
            print("\nHarry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. The magic starts here!")
            break
        elif ch_7 == 2:
            book = I2
            print("\n",I2)
            print("\nHarry Potter's summer has included the worst birthday ever, doomy warnings from a house-elf called Dobby, and rescue from the Dursleys by his friend Ron Weasley in a magical flying car! Back at Hogwarts School of Witchcraft and Wizardry for his second year, Harry hears strange whispers echo through empty corridors - and then the attacks start. Students are found as though turned to stone . Dobby's sinister predictions seem to be coming true.")
            break
        elif ch_7 == 3:
            book = I3
            print("\n",I3)
            print("\nWhen the Knight Bus crashes through the darkness and screeches to a halt in front of him, it's the start of another far from ordinary year at Hogwarts for Harry Potter. Sirius Black, escaped mass-murderer and follower of Lord Voldemort, is on the run - and they say he is coming after Harry. In his first ever Divination class, Professor Trelawney sees an omen of death in Harry's tea leaves . But perhaps most terrifying of all are the Dementors patrolling the school grounds, with their soul-sucking kiss.")
            break
        elif ch_7 == 4:
            book = I4
            print("\n",I4)
            print("\nThe Triwizard Tournament is to be held at Hogwarts. Only wizards who are over seventeen are allowed to enter - but that doesn't stop Harry dreaming that he will win the competition. Then at Hallowe'en, when the Goblet of Fire makes its selection, Harry is amazed to find his name is one of those that the magical cup picks out. He will face death-defying tasks, dragons and Dark wizards, but with the help of his best friends, Ron and Hermione, he might just make it through - alive!")
            break
        elif ch_7 == 5:
            book = I5
            print("\n",I5)
            print("\nDark times have come to Hogwarts. After the Dementors' attack on his cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to find him. There are many who deny the Dark Lord's return, but Harry is not alone: a secret order gathers at Grimmauld Place to fight against the Dark forces. Harry must allow Professor Snape to teach him how to protect himself from Voldemort's savage assaults on his mind. But they are growing stronger by the day and Harry is running out of time.")
            break
        elif ch_7 == 6:
            book = I6
            print("\n",I6)
            print("\nWhen Dumbledore arrives at Privet Drive one summer night to collect Harry Potter, his wand hand is blackened and shrivelled, but he does not reveal why. Secrets and suspicion are spreading through the wizarding world, and Hogwarts itself is not safe. Harry is convinced that Malfoy bears the Dark Mark: there is a Death Eater amongst them. Harry will need powerful magic and true friends as he explores Voldemort's darkest secrets, and Dumbledore prepares him to face his destiny.")
            break
        elif ch_7 == 7:
            book = I7
            print("\n",I7)
            print("\nAs he climbs into the sidecar of Hagrid's motorbike and takes to the skies, leaving Privet Drive for the last time, Harry Potter knows that Lord Voldemort and the Death Eaters are not far behind. The protective charm that has kept Harry safe until now is now broken, but he cannot keep hiding. The Dark Lord is breathing fear into everything Harry loves, and to stop him Harry will have to find and destroy the remaining Horcruxes. The final battle must begin - Harry must stand and face his enemy.")
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
