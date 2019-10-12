#Library Card module

"""  Creates a New Library Card, Retrieves existing Cards and provides/sends them to the main module.
Classes:
    LibCard
        functions: display()
                   Issue()
                   Buy()
                   Returnbook()
Functions:
    Editcard  (To t=edit the details of a card (name/comment))
    Storecard  (To store a newly generated Card)
    ChangeStoredcard  (To store the information changed in a card)
    Getcard  (To retrieve cards from data file)
    CNumber  (To generate a unique card number)
    Newcard  (To create a new card(LibCard) object)
    """

#---------------------------------------#
import pickle
import datetime

def CNumber(p):
    n=p+1
    while True:
        yield n
        n+=1

class LibCard:
    with open("Number of Cards.txt","r") as F:  #Filechangelocation
        N=int(F.read())
    
    def __init__(self,Cno,name,D_o_J,Ino,Bno,Comment):
        self.Number=Cno
        self.Name=name
        self.D_o_J=D_o_J
        self.issues=Ino
        self.buys=Bno
        self.Comments=Comment
        self.issued=[]
        self.bought=[]
        LibCard.N+=1
        F=open("Number of Cards.txt","w+") #Filechangelocation
        F.write(str(LibCard.N))
        F.close()
        self.d=0 #Number of displays
        
    def display(self):
        print """  
+-----------------------------+
|     The Reader's Havens""",(30-27)*' ',"""|
|    2/7, Potsdam, Berlin""",(30-27)*' ',"""|
|                             |
|Card Number/ID:""",self.Number,(30-(len(str(self.Number))+19))*' ',"""|
|Name:""",self.Name,(30-(len(self.Name)+9))*' ',"""|
|Date of Joining:""",self.D_o_J,(30-(len(self.D_o_J)+20))*' ',"""|
|Number of Books issued:""",self.issues,(30-(len(str(self.issues))+27))*' ',"""|
|Comments:""",self.Comments,(30-(len(self.Comments)+13))*' ',"""|
+-----------------------------+\n"""
        if self.d>0:
            print "Previous activities\n"
            print "Books issued:\n"
            for i in range(0,len(self.issued)):
                print '\t',self.issued[i][0],self.issued[i][1],self.issued[i][2],self.issued[i][3],'('+self.issued[i][4]+')'
            
            print "\nBooks bought:\n"
            for i in range(0,len(self.bought)):
                print '\t',self.bought[i][0],self.bought[i][1],self.bought[i][2],self.bought[i][3]
        self.d=1

    def Issue(self,name,bn):
        self.issues+=1
        self.issued.append((str(self.issues)+'.',name,' ['+str(bn)+']',datetime.date.today().strftime("%d-%m-20%y"),"pending"))
        ChangeStoredcard(Card)
    def Buy(self,name,bn):
        self.buys+=1
        self.bought.append((str(self.buys)+'.',name,' ['+str(bn)+']',datetime.date.today().strftime("%d-%m-20%y")))
        ChangeStoredcard(Card)

    def Returnbook(self,name,bn):
        for i in range(0,len(self.issued)):
            if self.issued[i][1]==name:
                if self.issued[i][4]=='pending':
                    self.issued[i]=(self.issued[i][0],self.issued[i][1],self.issued[i][2],self.issued[i][3],'returned')
                    return 'success'
                else:
                    print "The book has been already returned"
        else:
            print 'The given book has not been issued by you yet'
            
        
def Newcard():
    card_no=next(NewNo)
    Name=raw_input("Enter your Name:")
    D_o_J=datetime.date.today().strftime("%d-%m-20%y")
    booksissued=0
    booksbought=0
    Remarks=raw_input("Enter remarks/comments(optional) (max size 18):")
    Card[LibCard.N]=LibCard(card_no,Name,D_o_J,booksissued,booksbought,Remarks)
    print "Your Library Card has been created successfully"
    print "\nPlease note your card number"
    Card[LibCard.N].display()
    Storecard(Card[LibCard.N])

def Storecard(card):

    F=open("Cards.dat","a+b") #Filechangelocation
    pickle.dump(card,F)
    F.close()

def Getcard():
    Card={}
    for i in range(1,LibCard.N+1):
        try:
            x=pickle.load(F)
            Card[i]=x
        except EOFError:
            F.close()
            break
    return Card

def Editcard(Card):
    while True:
        n=int(raw_input("Enter your card number:"))
        if n in range(1,LibCard.N+1):
            print "\nSelect you query:"
            print "1. Edit your Name"
            print "2. Edit Comment"
            x=int(raw_input("Your input: "))
            if x==1:
                 newname=raw_input("Enter field Name:")
                 Card[n].Name=newname
                 print "\n"
                 print "Your updated card info:"
                 Card[n].display()
                 ChangeStoredcard(Card)
                 return Card  #Use this value (in the variable Card)
                
            elif x==2:
                newcomment=raw_input("Enter field Comment:")
                Card[n].Comments=newcomment
                print "Your updated card info:"
                Card[n].display()
                ChangeStoredcard(Card)
                return Card
        else:
            print "Given Card Number",n,"is invalid"
            continue
         

def ChangeStoredcard(Card):
    with open("Cards.dat","wb") as F:
        for i in range(1,LibCard.N+1):
            pickle.dump(Card[i],F)

NewNo=CNumber(0)   

Card={}     #Card : Dictionary with all the card objects

if LibCard.N>0:
    F=open("Cards.dat","r+b") #Filechangelocation
    Card=Getcard()
    F.close()
    
    
