#The program starts and this menu appears
import sys
import LibraryCard
import book3
import pickle
I=0

#-----------------The Main Menu-----------------#
def Menu():
    print """\n\n
     \t\t\t\tWELCOME TO THE READER's HAVENS
    \t\t\t       #------------------------------#"""

    print "\t\tMENU"

    print "\t\tSelect your Option/Choice"


    print "\t\t1. View Book Catalogue/Database","\t\t       9. __Search__"
    print "\t\t2. Issue a Book","\t\t\t\t          ----------"
    print "\t\t3. Buy a Book"
    print "\t\t4. Return a Book"
    print "\n\t\t5. Create your Library Card (New to the library?)"
    print "\t\t6. View Member details"
    print "\t\t7. Edit Member Details"
    print "\n\t\t8. Donate a Book"
        
    print "\n\t\t10. About Us\t\t\t\t\t       11. Exit"
    print "\t   "
    print "\n\n\t\t(Enter 'cancel' to go back to the main menu after selecting an option)"

    response=int(raw_input("\n\n\t\tYour Response: "))
    print "\n\n"
    return response

#------------------End of Menu------------------#
    
def BacktoMenu(Message):
    while True:
        r4=raw_input(Message)
        r4=r4.title()
        if r4 in ['Y','Yes']:
            return True
        elif r4 in ['N','No']:
            return False
        else:
            print "\nPlease enter (Yes/No) only"
            continue
    


Card=LibraryCard.Card  #Card : Dictionary with all the card objects


I+=len(Card)
while True:
    response=Menu()

#------------------Exit-------------------#
    if response==11:
        sys.exit() #Exit

#----------------About Us-----------------#
    elif response==10:
        print """About Us:

This is a Mini-Library (investigatory) project by Tanishq, Shivanshu and Tanmay
of class XII-D of DLF Public School""" 
        if BacktoMenu("Go back to the menu (Y/N)?"):
            continue
        else:
            sys.exit()
#---------------New Member---------------#            
    elif response==5:
    
        LibraryCard.Newcard()
        I+=1
        if BacktoMenu("Do you want to go back to Main Menu?"):
            continue
        else:
            sys.exit()
            
#---------------View Member Details---------------#    
    elif response==6:
        while True:
        
            n=int(raw_input("Enter your card number:"))
            try:
                if str(Card[n]):
                    pass
            except KeyError:
                print "Invalid Card number"
                if BacktoMenu("Enter again? "):
                    continue
                else:
                    break
            print "\nYour card details:"
            Card[n].display()

            if BacktoMenu("\nGo back to the main menu (Y/N)?"):
                break
            else:
                sys.exit()
#---------------Edit Member details---------------#
    elif response==7: #Edit Card
        while True:
            Card=LibraryCard.Editcard(Card)
            LibraryCard.Card=dict(Card)
            if BacktoMenu("Do you want to change something else?"):
                continue
            else:
                if BacktoMenu("Do you want to go back to the menu?"):
                    break
                else:
                    sys.exit()

#----------------View Books in the Library----------------#
    elif response==1:

        book3.Displaylist()
        while True:
            if BacktoMenu("\nView details of any book? (Y/N)"):
                n=int(raw_input("Enter book number:"))
                book3.Book5.bookvar[n].Display()
                print "\n\n"
                if BacktoMenu("View the Book list again?"):
                    book3.Displaylist()
                    continue
                else:
                    break
            else:
                break
        if BacktoMenu("Go back to the main menu (Y/N)?"):
            continue
        else:
            sys.exit()

#---------------Issue a Book---------------#
    elif response==2:
        n=raw_input("Enter you Card/Member number:")
        n=n.title()
        
        while True:
            
            bn=int(raw_input("Enter the serial number of the Book to be issued (To go to Main Menu and see Book List, Enter 9999)"))
            if bn==9999 or n=='Cancel':
                break
            
            elif bn in range(0,book3.Book5.N+1):
                n=int(n)
                p=book3.Book_no[bn].Issue()
                if p=="success":
                    Card[n].Issue(name=book3.Book5.L[bn-1],bn=bn)
                    Card[n].issues+=1
                p="*"
                break
            else:
                print "Book not found"
                if BacktoMenu("Enter Book serial number again?"):
                    continue
                else:
                    if BacktoMenu("Go back to Main Menu?"):
                        bn="Menu"
                        break
                    else:
                        sys.exit()
        if bn==9999 or n=='Cancel':
            continue
        elif p=="*":
            if BacktoMenu("Go back to Main Menu?"):
                continue
            else:
                sys.exit()
#---------------Buy Book---------------#
    elif response==3:

        n=raw_input("Enter you Card/Member number:")
        n=n.title()
        if n=='Cancel':
            continue
        n=int(n)
        while True:
            
            bn=int(raw_input("Enter the Book serial number you want to buy: (To go to Main Menu and see Book List, Enter 9999)"))
            if bn==9999:
                break
            elif bn in range(0,book3.Book5.N+1):
                p=book3.Book5.bookvar[bn].Buy()
                if p=='success':
                    Card[n].Buy(name=book3.Book5.L[bn-1],bn=bn)
                    print "Book",book3.Book5.bookvar[bn].name,"bought successfully!"
                    p="*"
                break
            else:
                print "Book not found"
                if BacktoMenu("Enter Book serial number again?"):
                    continue
                else:
                    if BacktoMenu("Go back to Main Menu?"):
                        p=9999
                        break
                    else:
                        sys.exit()
        if bn==9999:
            continue
        elif p=="*":
            if BacktoMenu("Go back to Main Menu?"):
                continue
            else:
                sys.exit()
#---------------Return Book---------------#
    elif response==4:
        n=raw_input("Enter your Card number/ID:")
        n=n.title()
        if n=='Cancel':
            continue
        bn=raw_input("Enter the book number/ID:")
        bn=bn.title()
        if bn=='Cancel':
            continue
        n,bn=int(n),int(bn)
        q=Card[n].Returnbook(name=book3.Book5.bookvar[bn].name,bn=bn)
        if q=='success':
            book3.Book5.bookvar[bn].Return()
        if BacktoMenu("Return to the main menu? (Y/N)"):
            continue
        else:
            sys.exit()
        
            
        
#---------------Donate Book---------------#
    elif response==8:
        r=book3.DonateBook()
        if r=='cancel':
            continue
        book3.Book_no=book3.Book5.bookvar

#-----------------Search-----------------#
    elif response==9:
        while True:
            bname=raw_input("Enter the name of the book:")
            bname=bname.title()
            if bname=='cancel':
                break
            else:
                for i in range(0,len(book3.Book5.bookvar)):
                    if bname==book3.Book5.L[i]:
                        book3.Book5.bookvar[i+1].Display()
                        break
                else:
                    print "Book with that name not found."
                    
                if BacktoMenu("Search again for a book?"):
                    continue
                else:
                    if BacktoMenu("Go back to the main menu?"):
                        break
                    else:
                        sys.exit()
#-----------------END-----------------#
