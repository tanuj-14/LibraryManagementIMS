import pickle
import datetime

def intro():
    '''function to print the opening screen'''
    print('''LIBRARY MANAGEMENNT SYSTEM
    VERSION 1.0
DEVELOPED BY TANUJ''')

def addbook():
    ''' function to add book info in book.dat file'''
    rec=[]
    
    try:
        '''open the file in the read and read all records into rec'''
        with open('book.dat','rb') as reader:
            rec=pickle.load(reader)
    except FileNotFoundError:#Initially file will exist 
        pass
        
    if len(rec)==0:#checing for the no of records in rec
        bookid=1#if no record is found then id to the first is given 0
    else:
        bookid=rec[-1][0]+1#if records exist the book id of next is last entered +1       
    while True:
        #opening in while loop so that multiple records can be taken        
        bname=input('Enter book name')
        aname=input('Enter author Name')
        pname=input('enter publisher name')
        sub=input('Enter subject')
        cop=int(input('Enter no. copies'))
        price=int(input('Enter price'))
        l=[bookid,bname,aname,pname,sub,cop,0,price]
        rec.append(l)#appending the records in list rec
        bookid=bookid+1
        d=input('do you want to continue[y/n]?')
                
        if d in 'Nn':
            break
    with open('book.dat','wb') as writer:
        pickle.dump(rec,writer)#writing the list into the binary file
        
def deletebook():
    '''FUNCTION TO DELETE BOOK INFORMATION'''
    rec=[]
    try:
        with open('book.dat','rb') as reader:#opening the file in read mode
            rec=pickle.load(reader)#reading the entire file
    except FileNotFoundError:
        print('The book database does not exist')
        return
    
    e=int(input('Enter book id'))#asking for which record to be deleted
    count=0
    for i in rec:
        if i[0]==e:
            rec.remove(i)#removing that record from the list
            print('THE RECORD HAS BEEN DELETED')
            break
    else:
        print('RECORD FOR DELETION NOT FOUND')
    with open('book.dat','wb') as writer:#opening the file in write mode so that modified data can be overwritten
        pickle.dump(rec,writer)#writting the record in file
    
    
def modifybook():
    '''FUNCTION TO MODIFY A BOOK INFORMATION'''
    rec=[]
    try:#opening the file in try except block
        with open('book.dat','rb') as reader:#opening the file in read mode
            rec=pickle.load(reader)
    except FileNotFoundError:#if file does not exist no point of going forward ie to modify
        print('The book database does not exist')
        return
    
    e=int(input('Enter book id'))#asking input for book id
    count=0
    for i in rec:
        if i[0]==e:#checking which book record to modify
            print('''WHAT WOULD YOU LIKE TO MODIFY
                    1 BOOK NAME
                    2 AUTHOR NAME
                    3 PUBLISHER
                    4 SUBJECT
                    5 TOTAL COPIES
                    6 COPIES ISSUED
                    7 PRICE
                    ENTER CHOICE(1-7)''',end='')#giving options to modify
            choice=int(input())
            if choice==1:
                i[1]=input('ENTER NEW BOOK NAME')
            elif choice==2:
                i[2]=input('ENTER NEW AUTHOR NAME')  
            elif choice==3:
                i[3]=input('ENTER NEW PUBLISHER NAME') 
            elif choice==4:
                i[4]=input('ENTER NEW SUBJECT NAME')
            elif choice==5:
                i[5]=int(input('ENTER NEW TOTAL COPIES'))
            elif choice==6:
                i[6]=int(input('ENTER NEW COPIES ISSUED'))
            elif choice==7:
                i[7]=int(input('ENTER NEW PRICE'))
            else:
                print('INVALID CHOICE')
            
            
            print('THE RECORD HAS BEEN MODIFIED')
            break
    else:
        print('RECORD FOR MODIFICATION NOT FOUND')
    with open('book.dat','wb') as writer:
        pickle.dump(rec,writer)#writing the modified record
                
        
def dispbook():
    '''function to display all book records'''
    with open('book.dat','rb') as readerwriter:
        rec=pickle.load(readerwriter)
        for i in rec:
            print(i)

def addmember():
    rec=[]
    
    try:
        '''open the file in the read mode and reading all records into rec'''
        with open('member.dat','rb') as reader:
            rec=pickle.load(reader)
    except FileNotFoundError:
        pass
        
    if len(rec)==0:
        memid=1
    else:
        memid=rec[-1][0]+1
    while True:
                
        memname=input('Enter member name')
        memclass=input('Enter member class')
        memsec=input('Enter member section')
        l=[memid,memname,memclass,memsec]
        rec.append(l)
        memid += 1
        d=input('do you want to continue[y/n]?')
                
        if d in 'Nn':
            break
    with open('member.dat','wb') as writer:
        pickle.dump(rec,writer)

def delmember():
    '''TO DELETE MEMBER'''
    rec=[]
    try:
        with open('member.dat','rb') as reader:
            rec=pickle.load(reader)
    except FileNotFoundError:
        print('The member database does not exist')
        return
    
    e=int(input('Enter member id'))
    for i in rec:
        if i[0]==e:
            rec.remove(i)
            print('THE RECORD HAS BEEN DELETED')
            break
    else:
        print('RECORD FOR DELETION NOT FOUND')
    with open('member.dat','wb') as writer:
        pickle.dump(rec,writer)

def modifymember():
    '''TO MODIFY A MEMBER'''
    rec=[]
    try:
        with open('member.dat','rb') as reader:
            rec=pickle.load(reader)
    except FileNotFoundError:
        print('The member database does not exist')
        return
    
    e=int(input('Enter member id'))
    count=0
    for i in rec:
        if i[0]==e:
            print('''WHAT WOULD YOU LIE TO MODIFY
                    1 MEMBER NAME
                    2 MEMBER CLASS
                    3 MEMBER SECTION
                    ENTER CHOICE(1-3)''',end='')
            choice=int(input())
            if choice==1:
                i[1]=input('ENTER NEW MEMBER NAME')
            elif choice==2:
                i[2]=input('ENTER NEW MEMBER CLASS')  
            elif choice==3:
                i[3]=input('ENTER NEW MEMBER SECTION') 
            else:
                print('INVALID CHOICE')
            print('THE RECORD HAS BEEN MODIFIED')
            break
    else:
        print('RECORD FOR MODIFICATION NOT FOUND')
    with open('member.dat','wb') as writer:
        pickle.dump(rec,writer)

def displaymember():
    '''functionn to display all book records'''
    with open('member.dat','rb') as readerwriter:
        rec=pickle.load(readerwriter)
        for i in rec:
            print(i)

def bookdatabase():
    '''ENTERING BOOK DATABASE MANIPULATION MENU'''
    while True:
        print('WELCOME TO THE BOOK DATABASE')
        print('''MANIPULATING BOOK DATABASE
              1 ADD BOOK
              2 DELETE BOOK
              3 MODIFY BOOK
              4 DISPLAY BOOK RECORD
              5 RETURN
              ENTER YOUR CHOICE[1/2/3/4]''')
        choice=int(input('ENTER YOUR CHOICE'))
        if choice==1:
            addbook()
        elif choice==2:
            deletebook()
        elif choice==3:
            modifybook()
        elif choice==4:
            dispbook()
        elif choice==5:
            return
        else:
            print('INVALID CHOICE ENTERED')

def memberdatabase():
    '''ENTERING MEMBER DATABASE MANIPULATION MENU'''
    print('''MANIPULATING MEMBER DATABASE
            1 ADD MEMBER
            2 DELETE MEMBER
            3 MODIFY MEMBER
            4 DISPLAY MEMBER RECORD
            5 RETURN
            enter your choice[1/2/3/4/5]''', end = "")
    choice = int(input())

    if choice==1:
        addmember()
    elif choice==2:
        delmember()
    elif choice==3:
        modifymember()
    elif choice==4:
       displaymember()
    elif choice==5:
       return
    else:
        print('INVALID CHOICE ENTERED')
    
    
def mandat():
    '''MENU TO ACCESS THE MAIN DATABASE - BOOK AND MEMBER'''
    while True:
        print('''MANIPULATING DATABASES
    1 BOOK DATABASE
    2 MEMBER DATABASE
    3 RETURN
    ENTER YOUR CHOICE[1/2/3]''')
              
        choice=int(input('ENTER YOUR CHOICE'))
        if choice==1:
            bookdatabase()
        elif choice==2:
            memberdatabase()
        elif choice==3:
            return
        else:
            print('Invalid choice entered')
            
          
def admin():
    '''MANIPULATING DATABASES'''
    print('''MANIPULATE DATABASES
YOU MUST BE THE ADMINSTRATOR''')
    user=input('ENTER USERNAME')
    passd=input('ENTER PASSWORD')
    if passd=='cbseproject':
        print('WELCOME ADMINSTRATOR')
        mandat()
    else:
        print('ACCESS DENIED')
 
    
def issue():
    '''FUNCTION TO ISSUE A BOOK'''
    # Read all member records in memberrec; Return if member file does not exist
    memberrec=[]
    try:
        with open('member.dat','rb') as reader:
            memberrec=pickle.load(reader)
    except FileNotFoundError:
        print('The member database does not exist')
        return

    # Read in the member id
    memid = int(input('ENTER MEMBER ID'))

    # Check validity of member id
    found=0
    for i in memberrec:
        if i[0]==memid:
            found=1
    if found==1:
        # If member id is valid

        # Read all book records in bookrec
        bookrec=[]
        try:#opening the file in try except block
            with open('book.dat','rb') as reader1:#opening the file in read mode
                bookrec=pickle.load(reader1)
        except FileNotFoundError:#if file does not exist no point of going forward ie to modify
            print('The book database does not exist')
            return

        # Ask for book id to issue
        bookid = int(input('ENTER ID OF THE BOOK YOU WANT TO ISSUE'))

               
        c=0
        for i in bookrec:
            if i[0]==bookid:
                if i[5] == i[6]:
                    print("Sorry, all copies of this book already issued")
                    c = -1
                    break
                else:
                    print("Book available. Book is being issued to you. Return within 7 days")

                    # Increase book issued count and write back to book.dat
                    i[6] += 1
                    with open('book.dat','wb') as writer:
                        pickle.dump(bookrec,writer)
                    # Create issue transaction record and write to transaction.dat
                    l = [memid]
                    l.append(bookid)
                    date=datetime.date.today()
                    l.append(date)
                    l.append(-1)# no of days for which book kept, -1 for not returned yet
                    l.append(0)#for fine

                    # Fetch all records of transaction file
                    trans = []
                    try:
                        with open('transaction.dat','rb') as reader1:
                            trans = pickle.load(reader1)
                    except:
                        pass

                    # Append this transaction to transactions list
                    trans.append(l)
                    
                    #Write back the transactions
                    with open('transaction.dat','wb') as writer1:
                        pickle.dump(trans,writer1)
                    
                    c=1
                    break
            
        if c==0:
            print('NO SUCH BOOK ID EXISTS')
            return
    else:
        print('YOU ARE NOT A MEMBER OF THE FAMILY')
        return
    
def ret():
    ''' FUNCTION TO RETURN A BOOK '''
    # Open the transaction file and get all records
    try:
        with open('transaction.dat','rb') as reader:
            rec=pickle.load(reader)
    except:
        print("No issue records found. Returning....")
        return
    print("Printing transactions")
    print(rec)
    # Read in the member id of the student returning the book
    e=int(input('ENTER YOUR MEMBER ID'))
    c=0

    # Search for record corresponding to member id in transaction.dat records
    for i in rec:
        # If a member id match found
        if i[0]==e:
            # Read all book records in rec1
            with open('book.dat','rb+') as readerwriter:
                rec1=pickle.load(readerwriter)

            # Look for the book id being returned
            for j in rec1:
                # If found
                if j[0]== i[1]:
                    # Decrease book issued count
                    j[6]=j[6]-1

                    # Get issue date
                    td1=i[2]
                    # Get return date
                    #td2=datetime.date.today()
                    # Changing for testing
                    td2 = datetime.date(2020,12,30)
                    # Calculate difference
                    tdelta=td2-td1
                    # Store the days for which book kept
                    i[3]=tdelta.days
                    # Indicate that book was found
                    c=1
                    # If book kept for more than 7 days calculate and store fine
                    if tdelta.days>7:
                        i[4]=5*(tdelta.days-7)
                        print("Please pay the fine amount Rs.",i[4])
    
    if c==1:
        with open('transcation.dat','wb') as writer:
            pickle.dump(rec,writer)
        with open('book.dat','wb') as writer1:
            pickle.dump(rec1,writer1)
        print("Book return successful")
    else:
        print('SORRY YOU ENTERED INCORRECT BOOK ID')
        return
    
def enq():
    reader=open('book.dat','rb')
    rec=pickle.load(reader)
    print('''WELCOME USER BY WHICH FIELD WOULD YOU LIKE SEARCH BOOK
            1BOOK NAME
            2AUTHOR NAME
            3PUBLISHER NAME
            4SUBJECT NAME

            ENTER CHOICE[1/2/3/4]''',end='')
    choice=int(input())
    if choice==1:
        e1=input('Enter book name')
        found=0
        for i in rec:
            if i[1].lower()== e1.lower():
                print(i)
                found=1
        if found==0:
            print('SORRY NO SUCH BOOK EXISTS')
            return
            
    elif choice==2:
        e2=input('Enter author name')
        found=0
        for i in rec:
            if i[2].lower()==e2.lower():
                print(i)
                found=1
        if found==0:
            print('SORRY NO BOOK BY THIS AUTHOR IS THERE')
    elif choice==3:
        e3=input('Enter publisher name')
        found=0
        for i in rec:
            if i[3].lower()==e3.lower():
                print(i)
                found=1
        if found==0:
            print('SORRY NO BOOK BY THIS PUBLISHER IS THERE')
    elif choice==4:
        e4=input('Enter subject name')
        found=0
        for i in rec:
            if i[4].lower()== e4.lower():
                print(i)
                found=1
        if found==0:
            print('SORRY NO BOOK IN THIS SUBJECT IS THERE')
    else:
        print("Invalid option. You must enter 1/2/3/4")
    reader.close()
    
def report():
    print('''WHICH REPORT WOULD YOU LIKE TO VIEW
            1TRANSACTIONS
            2FINE COLLECTED

            choice[1/2]''',end='')
    x=int(input())
    with open('transaction.dat','rb')as reader:
            rec=pickle.load(reader)
    if x==1:
        for i in rec:
            print(i)
    if x==2:
        c=0
        for i in rec:
            c=c+i[4]
        print('TOTAL FINE COLLECTED IS RUPEES',c)
    else:
        print('INVALID CHOICE ENTERED')
def help1():
    print('''WELCOME TO THE HELPDESK OF THE LIBRARY MANANGEMENT PROGRAMME''')
            



def welcome():
    '''function to print the main menu'''
    while True:
        print('''WELCOME TO THE LIRARY
            WHAT FUNCTION DO YOU WANT TO TO PERFORM?
            1 MANIPULATE DATABASE
            2 ISSUE A BOOK
            3 RETURN A BOOK
            4 ENQUIRY
            5 REPORTS
            6 HELP
            7 EXIT

            ENTER YOU CHOICE(1-7)''',end='')
        choice=int(input())
        if choice==1:
            admin()
        elif choice==2:
            issue()
        elif choice==3:
            ret()
        elif choice==4:
            enq()
        elif choice==5:
            report()
        elif choice==6:
            help1()
        elif choice==7:
            return
        else:
            print('invalid choice you must enter a number between 1 and 7')
            
        
intro()
welcome()
