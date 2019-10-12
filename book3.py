import pickle
F=open("Number of Books.txt","r")
class Book5:
    
    L=[] #List of Book names
    N=int(F.read())
    F.close()
    bookvar={}
    def __init__(self,name,genre,summary,author,qty,price,no=N+1):
        self.number=no
        self.name=name
        self.genre=genre
        self.summary=summary
        self.author=author
        self.Qty=qty
        self.price=price
        self.status=""
        Book5.N+=1
        F=open("Number of Books.txt","w")
        F.write(str(Book5.N))
        F.close()
        if self.Qty==0:
            
            self.Status="Not available"
        else:
            self.Status="Available"

    def Buy(self):
        if self.Status=="Available":
            print "The price is",self.price
            while True:
                
                ans=raw_input("Do you want to buy it? (Y/N)")
                if ans in ['Y','y','Yes','yes']:
                
                    self.Qty-=1
                    StoreBooks() 
                    if self.Qty==0 or self.Qty<0:
                        self.Status="Not available"
                    return 'success'
                elif ans in ['N','n','No','no']:
                    return "*"
                else:
                    print "Please enter (Yes/No) only"
                    continue
        else:
            print "Sorry, the book is currently not available"
            return "*"

    def Issue(self):
        if self.Status=="Available":

            duration=raw_input("Enter the duration: (minutes)")
            if duration in ['cancel','Cancel']:
                return 'cancel'
            
            self.Qty-=1
            StoreBooks()
            print "Book",self.name,"Issued successfully!"
            if self.Qty==0 or self.Qty<0:
                self.Status="Not available"
            return "success"
        else:
            print "Sorry, the book is currently not available"
            
    def Display(self):
        print "\n\n"
        print "Name:",self.name
        print "Author:",self.author
        print "Genre:",self.genre
        print "Description:",self.summary
        print "\nStatus:",self.status
        print "Quantity available:",self.Qty
        print "Price:",self.price

    def Return(self):
        self.Qty+=1
        print "Book returned successfully!"

def Setstatus():
    for i in range(1,Book5.N+1):
        if Book5.bookvar[i].Qty>0:
            Book5.bookvar[i].status="Available"
        else:
            Book5.bookvar[i].status="Not Available"


def Displaylist(): #Displays list of books(catalogue)
    for i in range(1,len(Book5.L)+1):
        print i,":",Book5.L[i-1]

def DonateBook():
    name=raw_input("Enter the Book's name:")
    name=name.title()
    qty=raw_input("Enter quantity of books:")
    qty=qty.title()
    if name=='Cancel' or qty=='Cancel':
        return 'cancel'
    qty=int(qty)
    l=''
    for i in range(1,len(Book5.L)+1):
        
        if name==Book5.bookvar[i].name:
            h=raw_input("Confirm? (Yes/No)")
            l="P"
            if h in ['Y','y','Yes','yes']:
                
                Book5.bookvar[i].Qty+=qty
                StoreBooks()
                print "\n\nThank you for your donation!"
                break
        elif name==Book5.L[i-1]:
            break
            
    if l!='P':
        genre=raw_input("Enter its Genre:")
        author=raw_input("Enter its Author:")
        qty=int(raw_input("Enter the quantity of books:"))
        price=int(raw_input("Enter the price of the book:"))
        summary=raw_input("Enter the description of the book:")
        B1=Book5(name,genre,summary,author,qty,price,Book5.N+1)
        StoreBook(B1)
        print "\n\nThank you for you donation!"
        Book5.bookvar[Book5.N+1]=B1
        Book5.L+=[B1.name]
        #Change: Book_no in Library_main after tuple
    
def StoreBook(B):
    F=open("B_ooks.dat","ab")
    pickle.dump(B,F)
    F.close()
    

def StoreBooks():
    F=open("B_ooks.dat","wb")
    for i in range(1,Book5.N+1):
        pickle.dump(Book5.bookvar[i],F)
    F.close()
        
    

def GetBooks():
    F=open("B_ooks.dat","rb")
    try:
        D={}
        for i in range(1,Book5.N+1):
            D[1]=pickle.load(F)
            Book5.bookvar[i]=D[1]
        F.close()
        return Book5.bookvar
    except EOFError:
        F.close()
        return Book5.bookvar

if Book5.N>0:
    Book_no=GetBooks()   #the first statement of the program
    Book5.bookvar=dict(Book_no)
    Setstatus()

try:
    
    for i in range(1,Book5.N+1):
        Book5.L+=[Book_no[i].name]
    
except KeyError:
    pass


