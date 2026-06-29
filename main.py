from manager import StudentManager

def main():
    manager=StudentManager()
    
    
    while True:
        print("-------------WELCOME TO THE STDUENT MANAGEMENT SYSTEM-------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Exit")
        
        try:
            choice=int(input("Enter the function to perform: "))
            if choice==1:
                manager.add()
            elif choice==2:
                manager.view()
            elif choice==3:
                manager.search()
            elif choice==4:
                manager.update()
            elif choice==5:
                manager.delete()
            elif choice==6:
                manager.statistics()
            elif choice==7:
                break
            else:
                print("invalid input!!")
        except ValueError:
            
            print("Please enter a number!!")
        

if __name__ == "__main__":
    main()