import hashlib
import shutil
from Cab_Driver import cab_driver
from Customer import customer
from Driver_login import Driver_log
from Customer_login import Cust_log
from Booking import Zula_Ride

Admin_Name = "Admin"
Admin_pass = hashlib.sha256("Log".encode()).hexdigest()

def age_chk(age):
    if 18 <= int(age) <= 70:
        return True
    else:
        print("\n Not Eligible for Driving - Under 18 or Above 70 \n")
        return False
    
def choice_chk(choice):
    if choice.isdigit():
        return int(choice)
    return False

def duplicate(name,lists):
    for names in lists:
        if names["Name"] == name:
            return True
    return False

def driver_coll():

    while True:
        name = input("Driver Name : ").strip()
        if duplicate(name,driver_lists):
            print("\n Driver - Name Already Exists \n")
        else:
            break

    password = input("Driver Password : ").strip() 
    initial_loc = None
    login,rest = False,False
    tot_trips,earnings,zula = 0,0,0
    Driv_His = []

    while True:
        age = input("Driver Age : ").strip()
        if not age.isdigit():
            print("\n Age Cannot be Negative or Cannot be String or Empty \n")
        elif age_chk(age):
            return cab_driver(name,password,int(age),initial_loc,login,earnings,rest,tot_trips,zula,Driv_His)
        else:
            return 0
        
def customer_coll():

    while True:
        name = input("Customer Name : ").strip()
        if duplicate(name,cust_lists):
            print("\n Passenger - Name Already Exists \n")
        else:
            break
    
    password = input("Customer Password : ").strip()
    initial_loc = None
    login = False
    tot_trips = 0
    Cust_His = []

    while True:
        age = input("Customer Age : ").strip()
        if not age.isdigit():
            print("\n Age Cannot be Negative or Cannot be String or Empty \n")
        else:
            return customer(name,password,int(age),initial_loc,login,tot_trips,Cust_His)

def driv_store(driv):

    return {"id" : driv.id,
            "Name" : driv.name,
            "Password" : driv.password,
            "Age" : driv.age,
            "Location" : driv.initial_loc,
            "Login" : driv.login,
            "Earnings" : driv.earnings,
            "Rest" : driv.rest,
            "Total_trips" : driv.tot_trips,
            "Zula" : driv.zula,
            "History" : driv.history
                }

def cust_store(cust):

    return {"id" : cust.id,
            "Name" : cust.name,
            "Password" : cust.password,
            "Age" : cust.age,
            "Location" : cust.initial_loc,
            "Login" : cust.login,
            "Total_trips" : cust.tot_trips,
            "History" : cust.history
                }

driver_lists = []
cust_lists = []
route_locations_cab = {
    'A' : 0,
    'C' : 4,
    'D' : 7,
    'F' : 9,
    'B' : 15,
    'G' : 18,
    'H' : 20,
    'E' : 23
    }


while True:
    print("Welcome To ZULA".center(shutil.get_terminal_size().columns))
    print(" Choice 1 - Sign Up - Driver " \
    "\n Choice 2 - Sign Up - Customer " \
    "\n Choice 3 - Driver Login " \
    "\n Choice 4 - Customer Login " \
    "\n Choice 5 - ZULA Ride" \
    "\n Choice 6 - Admin Login " \
    "\n Choice 7 - History of Rides" \
    "\n Choice 8 - Exit")
    print()
    choice = choice_chk(input("Enter Your Choice : ").strip())

    if not choice:
        print("\n Choice Cannot be Negative or String or Empty \n")  

    elif choice == 1:

        driv = driver_coll()
        if isinstance(driv,cab_driver):
            driver_lists.append(driv_store(driv))
            print("\n Driver Registration Completed - Login to Access Further")

    elif choice == 2:

        cust = customer_coll()
        cust_lists.append(cust_store(cust))
        print("\n Customer Registration Completed - Login to Access Further \n")

    elif choice == 3:

        if driver_lists:
            Log_Name_Driver = input("Driver UserName : ").strip()
            Log_Password_Driver = input("Driver Password : ").strip()
            Driver_log(driver_lists,Log_Name_Driver,Log_Password_Driver)
        else:
            print("\n No Driver Account Registered Yet - Sign up by Selecting Choice 1 \n")

    elif choice == 4:

        if cust_lists:
            Log_Name_Cust = input("Customer Username : ").strip()
            Log_Password_Cust = input("Customer Password : ").strip()
            Cust_log(cust_lists,Log_Name_Cust,Log_Password_Cust)
        else:
            print("\n No Customer Account Registered Yet - Sign up by Selecting Choice 2 \n")
    
    elif choice == 5:

        if cust_lists:
            flag = 0
            Book_pass_Name = input("Passenger Name : ").strip()
            for i in cust_lists:
                if i["Name"] == Book_pass_Name:
                    flag = 1
                    if i["Login"] == True:
                        flag += 2
                        Zula_Ride(driver_lists,route_locations_cab,i["id"],cust_lists)
            if flag == 0:
                print("\n Account Doesn't Exists \n")
            elif flag == 1:
                print("\n Login To Book Cab \n")
        else:
            print("\n Register and Login To Book Rides \n")

    elif choice == 6:

        Admin_Name_Log = input("Admin_UserName : ").strip()
        Admin_pass_Log = hashlib.sha256(input("Admin_Password : ").strip().encode()).hexdigest()

        if Admin_Name == Admin_Name_Log and Admin_pass == Admin_pass_Log:
            print("\n Successfully Logged In \n")

            while True:
                print(" Admin Choice 1 - Drivers Details" \
                "\n Admin Choice 2 - Customers Details" \
                "\n Admin Choice 3 - Driver History" \
                "\n Admin Choice 4 - Exit")
                print()
                Admin_choice = choice_chk(input("Admin Choice : ").strip())

                if not Admin_choice:
                    print("\n Admin Choice Cannot be Negative or Cannot be a String or Empty \n")

                elif Admin_choice == 1:
                    print("\n Driver Details: \n")
                    if driver_lists:
                        print(f"{"ID":<5} {"Name":<10} {"Age":<5} {"Location":<15} {"Login":<10} {"Earnings":<10} {"Rest":<10} {"Total_trips":<15} {"Zula Commission":<15}")
                        for drv in driver_lists:
                            print(f"{drv["id"]:<5} {drv["Name"]:<10} {drv["Age"]:<5} {str(drv["Location"]):<15} {str(drv["Login"]):<10} ${drv["Earnings"]:<10} {str(drv["Rest"]):<10} {drv["Total_trips"]:<15} ${drv["Zula"]:<15}")
                        print()
                    else:
                        print("\n No Drivers Available Yet \n")
                    print()

                elif Admin_choice == 2:
                    print("\n Customer Details: \n")
                    if cust_lists:
                        print(f"{"ID":<5} {"Name":<10} {"Age":<5} {"Location":<15} {"Login":<10} {"Total_trips":<15}")
                        for cst in cust_lists:
                            print(f"{cst["id"]:<5} {cst["Name"]:<10} {cst["Age"]:<5} {str(cst["Location"]):<15} {str(cst["Login"]):<10} {cst["Total_trips"]:<15}")
                        print()                        
                    else:
                        print("\n No Customers Available Yet \n")

                elif Admin_choice == 3:
                    if driver_lists:
                        his_driv_name = input("Driver Name : ").strip()
                        flag = 0
                        for i in driver_lists:
                            if i["Name"] == his_driv_name:
                                flag = 1
                                his_driv_id = i["id"]
                                trips = i["Total_trips"]
                                break
                        if flag:
                            print("\n Cab ID : ",his_driv_id)
                            print("\n Total Number of Trips : ",trips)
                            fare = sum(j["Fare"] for j in i["History"])
                            zula = sum(j["Zula"] for j in i["History"])
                            print("\n Total Fare Collected : ",fare)
                            print("\n Total Zula Commission Collected : ",zula)
                            print("\n Trip Details: ")

                            if trips > 0:
                                print(f"{"Source":<10} {"Destination":<15} {"Cust_ID":<10} {"Zula_Commission":<20} {"Fare":<10}")
                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<10} {j["Dest_Loc"]:<15} {j["Cust_ID"]:<10} ${j["Zula"]:<20} ${j["Fare"]:<10}")
                                print()
                            else:
                                print("\n No Trips were Given \n")
                        else:
                            print("\n Invalid Username \n")
                    else:
                        print("\n No Driver Registered \n")
                elif Admin_choice == 4:
                    print("\n Admin Logged Out Successfully \n")
                    break
                
                else:
                    print("\n Invalid Admin Choice \n")

        else:
            print("\n Invalid Username or Password \n")
        
    elif choice == 7:
        select = input("Select Type :- (Driver - 0) / (Passenger - 1) : ").strip()

        if choice_chk(select):
            if cust_lists:
                flag = 0
                pass_name = input("(History) - Passenger Name : ").strip()

                for i in cust_lists:
                    if i["Name"] == pass_name and i["Login"] == True:
                        pass_id = i["id"]
                        flag = 1
                        history = i["History"]
                        break

                if flag:
                    print("\n Passenger ID : ",pass_id)
                    print("\n Passenger Name : ",pass_name)
                    print("\n Trip Details: ")
                    if history:
                        print(f"{"Source":<10} {"Destination":<15} {"Cab_ID":<10} {"Fare":<10}")

                        for i in cust_lists:
                            if i["Name"] == pass_name and i["Login"] == True:
                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<10} {j["Dest_Loc"]:<15} {j["Cab_detail"]:<10}  ${j["Fare"]:<10}")
                                print()
                    else:
                        print("\n No Trips Were Taken \n")
                else:
                    print("\n Login To Access Further \n")

            else:    
                print("\n No Passengers Registered - (Passenger) \n")

        elif select.isdigit() and select == '0':
            if driver_lists:
                flag = 0
                driv_name = input("(History) - Driver Name : ").strip()

                for i in driver_lists:
                    if i["Name"] == driv_name and i["Login"] == True:
                        driv_id = i["id"]
                        history = i["History"]
                        flag = 1
                        break
        
                if flag:
                    print("\n Cab ID : ",driv_id)
                    print("\n Cab Driver Name : ",driv_name)
                    print("\n Trip Details \n")
                    if history:
                        print(f"{"Source":<10} {"Destination":<15} {"Cust_ID":<10} {"Zula_Commission":<20} {"Fare":<10}")

                        for i in driver_lists:
                            if i["Name"] == driv_name and i["Login"] == True:
                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<10} {j["Dest_Loc"]:<15} {j["Cust_ID"]:<10} ${j["Zula"]:<20} ${j["Fare"]:<10}")
                                print() 
                    else:
                        print("\n No Trips Were Taken \n")                 
                else:
                    print("\n Login To Access Further \n")

            else:
                print("\n No Drivers Registered \n")
                
        else:
            print("Invalid Selection")

    elif choice == 8:

        print("\n Successfully Exited \n")
        break

    else:

        print("\n Invaild Choice \n")

if __name__ == "__Main__":
    print("Run")