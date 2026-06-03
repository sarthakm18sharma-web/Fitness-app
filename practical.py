def add_records():
    with open("D:\\code\\student.txt",'a') as file:
        r=int(input("Enter the roll no "))
        n=input("Enter the name ")
        c=input("Enter the class")
        m=int(input("Enter the marks"))
        file.write(f"{r},{n},{c},{m}\n")
        print("Records added")
def display_records():
    try:
        with open("D:\\code\\student.txt" ,'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("file not found")
def search_records():
    rollno=input("Enter the roll no")
    found=False
    try:
        with open("D:\\code\\student.txt",'r') as file:
            for line in file:
                if line.startswith(rollno+","):
                    print("Record founded",line.strip())
                    found=True
                    break
            if not found:
                print("no record found")
    except FileNotFoundError:
        print("File not found")
def delete_records():
    rollno=input("Enter the roll no")
    found=False
    with open("D:\\code\\student.txt",'r') as file:
        lines=file.readlines()
    with open("D:\\code\\student.txt",'w') as file:
        for line in lines:
            if not line.startswith(rollno+","):
                file.write(line)
            else:
                found=True
    if found:
        print("Record delete")
    else:
        print("No record found")
def menu():
    while True:
        print("Press 1 to add")
        print("Press 2 to display")
        print("Press 3 to search")
        print("Press 4 to delete")
        print("Press 5 to exit")
        ch=int(input("Enter the choice"))
        if ch==1:
            add_records()
        elif ch==2:
            display_records()
        elif ch==3:
            search_records()
        elif ch==4:
            delete_records()
        elif ch==5:
            print("Exiting...")
            break
menu()
            
            
                
        
     
