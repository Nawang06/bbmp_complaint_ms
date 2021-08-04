import os
name = ''
phone = ''
pincode = ''
wardno = ''
complaint = ''
x = 1

def lodge():
    global x
    os.system('cls')
    print("")
    print("You Have Chosen To Lodge A Complaint")
    print("***********************************************************************************************************************")
    print("")
    phone = input("Please enter your Phone Number to continue: ")
    name = input("Enter your Name: ")
    pincode = input("Enter your area pincode: ")
    wardno = input("Enter your ward number: ")
    complaint = input('Please enter your Complaint description: ')
    print("")
    x1=str(x)
    list1 = [x1,phone,name,pincode,wardno,complaint]
    file = open("complaints.txt", "a")
    for i in list1:
        file.write(i+'\t')
    file.write('\n')
    print("This Is Your COMPLAINT ID: "+x1+"\nPlease Do Provide the ID whenever you need to modify or delete a complaint\nThank You\n")
    file.close()
    x+=1
    input("Press ANY Key To Continue:")
    os.system('cls')
    return


def display():
    print("")
    flag = 1
    file = open("complaints.txt", "r")
    re=file.readlines()
    os.system('cls')
    phone = input("Enter your phone number to search your complaint: ")
    print("")
    for line in re:
        list2 = line.split('\t')
        l=list2[0]
        ph = list2[1]
        name = list2[2]
        pincode = list2[3]
        wardno = list2[4]
        complaint = list2[5]
        if ph == phone:
            print("Your Complaint Details are".center(125,'*'))
            print("")
            print("Complaint ID: ".ljust(50,'.'),l.rjust(75))
            print("Phone".ljust(50,'.'),ph.rjust(75))
            print("Name".ljust(50,'.'),name.rjust(75))
            print("Pincode".ljust(50,'.'),pincode.rjust(75))
            print("Ward Number".ljust(50,'.'),wardno.rjust(75))
            print("Complaint".ljust(50,'.'),complaint.rjust(75))
            flag = 0
    if flag==1:
        print("Details not found")
    input("Press ANY Key To Continue:")
    os.system('cls')
    return

def modify():
    flag = 1
    file = open ("complaints.txt",'r+')
    re=file.readlines()
    os.system('cls')
    phone = input("Enter Your Mobile Phone Number:\t")
    cid = input("Enter Your Complaint ID\t")
    print("")
    file.seek(0)
    for line in re:
        list2 = line.split('\t')
        if (list2[0]==cid and list2[1] == phone):
            flag=0
            print()
            print("Your Complaint Details are".center(125,'*'))
            print("")
            print("Complaint ID: ".ljust(50,'.'),list2[0].rjust(75))
            print("Phone".ljust(50,'.'),list2[1].rjust(75))
            print("Name".ljust(50,'.'),list2[2].rjust(75))
            print("Pincode".ljust(50,'.'),list2[3].rjust(75))
            print("Ward Number".ljust(50,'.'),list2[4].rjust(75))
            print("Complaint".ljust(50,'.'),list2[5].rjust(75))
            print("")
            list2[5]=input("Enter the modification in the complaint:\t")
            news = '\t'.join(list2)
            file.write(news)
            print("")
            print("The Complaint has been Modified".center(120,"*"))
            print("")
        else:
            file.write(line)
        file.truncate()
    if(flag==1):
        print("The Complaint ID/Phone Number Doesn't match or the Complaint doesn't Exist. Try Again")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return

def delete():
    flag = 1
    file = open ("complaints.txt",'r+')
    re=file.readlines()
    os.system('cls')
    phone = input("Enter Your Mobile Phone Number:\t")
    cid = input("Enter Your Complaint ID\t")
    print("")
    file.seek(0)
    for line in re:
        list2 = line.split('\t')
        if (list2[0]==cid and list2[1] == phone):
            flag=0
            print()
            print("Your Complaint Details are".center(125,'*'))
            print("")
            print("Complaint ID: ".ljust(50,'.'),list2[0].rjust(75))
            print("Phone".ljust(50,'.'),list2[1].rjust(75))
            print("Name".ljust(50,'.'),list2[2].rjust(75))
            print("Pincode".ljust(50,'.'),list2[3].rjust(75))
            print("Ward Number".ljust(50,'.'),list2[4].rjust(75))
            print("Complaint".ljust(50,'.'),list2[5].rjust(75))
            print("")
            print("\nComplaint Has Been Deleted\n")
        else:
            file.write(line)
        file.truncate()
    if(flag==1):
        print("The Complaint ID/Phone Number Doesn't match or the Complaint doesn't Exist. Try Again")
    file.close()
    input("Press ANY Key To Continue:")
    os.system('cls')
    return

choice = 1
z = 1
print("Welcome to the BBMP Complaint Management Portal".center(210,"-"))
print("")
print("")
while(z!= 0):
    choice = 1
    print("Please Do Identify Yourself:")
    print("")
    print("1. Administrator")
    print("2. User")
    print("0. EXIT")
    z=int(input("Press the number corresponding to the role : "))
    if z==1:
          os.system('cls')
          while(choice!=0):
            print("")
            print("")
            print("BBMP Complaint Management System".center(210,"*"))
            print("")
            print("MENU:")
            print("")
            print("1. Display The Complaints")
            print("2. Modify The Complaints")
            print("0. Log Out")
            print()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display()
            elif choice == 2:
                modify()
            elif choice == 0:
                print()
                os.system('cls')
            else:
                print("Invalid Choice. Choose Again!")
    elif z==2 :
        os.system('cls')
        while(choice!=0):
                print("")
                print("")
                print("BBMP Complaint Management System".center(210,"*"))
                print("")
                print("MENU:")
                print("")
                print("1. Lodge a complaint")
                print("2. Display your Complaints")
                print("3. Delete your complaint")
                print("4. Modify Your Complaint")
                print("0. Log Out")
                print()
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    lodge()
                elif choice ==2:
                    display()
                elif choice == 3:
                    delete()
                elif choice == 4:
                    modify()
                elif choice == 0:
                    print()
                    os.system('cls')
                else:
                    print("Invalid Choice. Choose Again!")
    else:
        os.system('cls')
        print("Invalid Choice. Choose Again!")
        print("")
        

