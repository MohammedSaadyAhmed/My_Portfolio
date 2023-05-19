import datetime
import csv
import glob
import os 




def User_Input():
    
    print("1. Create a contact. ")
    print("2. Update a contact. ")
    print("3. Delete a contact. ")
    
    action = int(input("Enter your Choice: "))
    
    if action == 1:
        Create_Contact()
        
    elif action == 2:
        Update_Contact()
        
    elif action == 3:
        Delete_Contact()
    
    else:
        print("Wrong choice. Please choose from 1, 2, or 3.")
        User_Input()


def Create_Contact():
    Name = input(" 1st, Enter the name: ")
    Email = input(" 2nd, Enter the Email:  ")
    Phone_Number = get_valid_Phone_Number()
    Address = input(" 4th, Enter the address: ")
    insertion_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')
    save_inputs(Name, Email, Phone_Number, Address, insertion_date)
    User_Input()




def get_valid_Phone_Number():
    while True:
        Phone_Number = input(" 3rd, Enter the phone number: ")
        if Phone_Number.isdigit():
            return Phone_Number
        else:
            print("It,s invalid. Enter the correct phone number.")


def save_inputs(Name, Email, Phone_Number, Address, insertion_date):
    with open('Saady.csv', 'a', newline='') as file:
        adder = csv.writer(file)
        adder.writerow([Name, Email, Phone_Number, Address, insertion_date])
    print("Successfully saved!")


def Update_Contact():
    search_field = IsValid_Field()
    search_email = input("Enter the E_mail of the contact you want to update: ")

    with open('Saady.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if IsValid_Email(rows, search_email):
        for row in rows:
            if row[1] == search_email:
                if int(search_field) == 1:
                    new_value = input("Enter the new Name: ")
                    row[0] = new_value
                elif int(search_field) == 2:
                    new_value = input("Enter the new Email: ")
                    row[1] = new_value
                elif int(search_field) == 3:
                    print("For new Phone_Number ")
                    new_value = get_valid_Phone_Number()
                    row[2] = new_value
                elif int(search_field) == 4:
                    new_value = input("Enter the new Address: ")
                    row[3] = new_value
                elif int(search_field) == 5:
                    User_Input()
                    

        with open('Saady.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("The Update has been done successfully")
        User_Input()
    else:
        print("It's not exist.  Enter a valid E_mail!")
        Update_Contact()


def IsValid_Field():
    while True:
        field = input("Which field you want to update:\n"
                 "1.  Name\n"
                 "2.  Email\n"
                 "3.  Phone_Number\n"
                 "4.  Address\n"
                 "5.  Getback to change the request\n"
                 "Enter the field number: ")
        if field.isdigit() and 0 < int(field) <= 5:
            if int(field) < 5:
                return field
            elif int(field) == 5:
                User_Input()
                
                
        else:
            print("Please enter the field number.")


def IsValid_Email(rows, email):
    for row in rows:
        if row[1] == email:
            return True
    return False


def Delete_Contact():
    search_email = input("Enter The Email for the contact You Want To delete: ")

    with open('Saady.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[1] == search_email:
            validation = 1
            break
        else:
            validation = 0
    if validation == 1:
        for row in rows:
            if row[1] == search_email:
                rows.remove(row)
                with open('Saady.csv', 'w', newline='') as file:
                    adder = csv.writer(file)
                    adder.writerows(rows)
                print("Contact has been  deleted Successfully")
                User_Input()

    else:
        print("This Email doesn't exist in the file !")
        User_Input()




if __name__ == '__main__':
    print("Please select your request :")
    User_Input()
