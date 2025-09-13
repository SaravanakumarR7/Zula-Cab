import hashlib
import shutil
from Cab_Driver import Cab_driver
from Passengers import Passenger
from Driver_login import Driver_log
from Passenger_login import Pass_log
from Booking import Zula_Ride

Admin_Name = "Admin"
Admin_pass = hashlib.sha256("Log".encode()).hexdigest()

def age_chk(age):
    if 18 <= int(age) <= 70:
        return True
    else:
        print("\n Not Eligible for Driving - Under 18 or Above 70 \n")
        return False

def del_chk():
    while True:
        chk = input("Are You Sure To Delete ? Yes/No - (y/n): ").strip()
        if chk.lower() == 'y':
            return True
        elif chk.lower() == 'n':
            return False
        else:
            print("Invalid Choice - (Choose - (y/n) )")

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
            return Cab_driver(name,password,int(age),initial_loc,login,earnings,rest,tot_trips,zula,Driv_His)
        else:
            return 0
        
def customer_coll():
    while True:
        name = input("Passenger Name : ").strip()

        if duplicate(name,cust_lists):
            print("\n Passenger - Name Already Exists \n")
        else:
            break
    
    password = input("Passenger Password : ").strip()
    initial_loc = None
    login = False
    tot_trips = 0
    Cust_His = []

    while True:
        age = input("Passenger Age : ").strip()

        if not age.isdigit():
            print("\n Age Cannot be Negative or Cannot be String or Empty \n")
        else:
            return Passenger(name,password,int(age),initial_loc,login,tot_trips,Cust_His)

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
    print(" Choice 1 - Sign_Up - (Driver / Passenger) " \
    "\n Choice 2 - Login - (Driver / Passenger) " \
    "\n Choice 3 - ZULA Ride" \
    "\n Choice 4 - Admin Login " \
    "\n Choice 5 - History of Rides - (Driver / Passenger)" \
    "\n Choice 6 - Edit Profile or Password - (Driver / Passenger) " \
    "\n Choice 7 - Exit \n")

    choice = choice_chk(input("Enter Your Choice : ").strip())

    if not choice:
        print("\n Choice Cannot be Negative or String or Empty \n")  
        
    elif choice == 1:

        print("\n Choice 1 - Driver Sign_Up " \
            "\n Choice 2 - Passenger Sign_Up \n")
        
        choice = choice_chk(input("Choice : ").strip())

        if choice == 1:
            driv = driver_coll()
            if isinstance(driv,Cab_driver):
                driver_lists.append(driv_store(driv))
                print("\n Driver Registration Completed - Login to Access Further \n")

        elif choice == 2:
            cust = customer_coll()
            cust_lists.append(cust_store(cust))
            print("\n Passenger Registration Completed - Login to Access Further \n")

        else:
            print("\n Invalid Choice \n")

    elif choice == 2:

        print("\n Choice 1 - Driver Login " \
        "\n Choice 2 - Passenger Login \n")

        choice = choice_chk(input("Choice : ").strip())

        if choice == 1:
            if driver_lists:
                Log_Name_Driver = input("Driver UserName : ").strip()
                Log_Password_Driver = input("Driver Password : ").strip()
                Driver_log(driver_lists,Log_Name_Driver,Log_Password_Driver)
                
            else:
                print("\n No Driver Account Registered Yet - Sign up by Selecting Choice 1 \n")
                
        elif choice == 2:
            if cust_lists:
                Log_Name_Cust = input("Customer Username : ").strip()
                Log_Password_Cust = input("Customer Password : ").strip()
                Pass_log(cust_lists,Log_Name_Cust,Log_Password_Cust)
                
            else:
                print("\n No Passenger Account Registered Yet - Sign up by Selecting Choice 2 \n")
            
        else:
            print("\n Invalid Choice \n")
        
    elif choice == 3:

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
            print("\n No Passengers Available Yet \n")

    elif choice == 4:

        Admin_Name_Log = input("Admin_UserName : ").strip()
        Admin_pass_Log = hashlib.sha256(input("Admin_Password : ").strip().encode()).hexdigest()

        if Admin_Name == Admin_Name_Log and Admin_pass == Admin_pass_Log:

            print("\n Successfully Logged In \n")

            while True:

                print(" Admin Choice 1 - Drivers Details" \
                "\n Admin Choice 2 - Passenger Details" \
                "\n Admin Choice 3 - Driver History" \
                "\n Admin Choice 4 - Remove Driver" \
                "\n Admin Choice 5 - Exit \n")

                Admin_choice = choice_chk(input("Admin Choice : ").strip())
                flag = 0

                if not Admin_choice:
                    print("\n Admin Choice Cannot be Negative or Cannot be a String or Empty \n")

                elif Admin_choice == 1:

                    print("\n Driver Details: \n")

                    if driver_lists:

                        print(f"{"ID":<10} {"Name":<20} {"Age":<10} {"Location":<20} {"Login":<10} {"Earnings":<20} {"Rest":<15} {"Total_trips":<20} {"Zula Commission":<20}")
                        tot_fare = 0
                        tot_commission = 0
                        for drv in driver_lists: 
                            tot_fare += drv["Earnings"]
                            tot_commission += drv["Zula"]
                            print(f"{drv["id"]:<10} {drv["Name"]:<20} {drv["Age"]:<10} {str(drv["Location"]):<20} {str(drv["Login"]):<10} ${drv["Earnings"]:<20} {str(drv["Rest"]):<15} {drv["Total_trips"]:<20} ${drv["Zula"]:<20}")
                        
                        print("\n Total_Fare Collected : ",tot_fare)
                        print(" Total_Zula_Commission Collected : ",tot_commission)

                    else:
                        print("\n No Drivers Available Yet \n")
                    print()

                elif Admin_choice == 2:

                    print("\n Passengers Details: \n")

                    if cust_lists:

                        print(f"{"ID":<10} {"Name":<20} {"Age":<10} {"Location":<20} {"Login":<10} {"Total_trips":<20}")
                        for cst in cust_lists:
                            print(f"{cst["id"]:<10} {cst["Name"]:<20} {cst["Age"]:<10} {str(cst["Location"]):<20} {str(cst["Login"]):<10} {cst["Total_trips"]:<20}")                  
                    
                    else:
                        print("\n No Passengers Available Yet \n")
                    print()

                elif Admin_choice == 3:

                    if driver_lists:

                        his_driv_name = input("Driver Name : ").strip()

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
                                print(f"{"Source":<20} {"Destination":<20} {"Cust_ID":<10} {"Zula_Commission":<20} {"Fare":<20}")
                                
                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<20} {j["Dest_Loc"]:<20} {j["Cust_ID"]:<10} ${j["Zula"]:<20} ${j["Fare"]:<20}")
                                print()

                            else:
                                print("\n No Trips were Given \n")

                        else:
                            print("\n Invalid Username \n")

                    else:
                        print("\n No Driver Registered Yet \n")
                
                elif Admin_choice == 4:

                    print("\n Delete Section - (Driver) \n")
                    del_name = input("Driver Name : ").strip()

                    for i in range(len(driver_lists)):
                        if driver_lists[i]["Name"] == del_name:
                            flag = 1

                            if del_chk():
                                del_driv = driver_lists.pop(i)
                                print("\n Successfully Removed Driver : ",del_name)
                                print("\n Driver Details \n")

                                for key,val in del_driv.items():
                                    print(f"{key} : {val}")
                                print()
                                break

                            else:
                                print("\n No Actions Taken \n")
                                break

                    if not flag:
                        print("\n No Driver Found \n")

                elif Admin_choice == 5:
                    print("\n Admin Logged Out Successfully \n")
                    break

                else:
                    print("\n Invalid Admin Choice \n")

        else:
            print("\n Invalid Username or Password \n")
        
    elif choice == 5:
        select = input("Select Type :- (Driver - 1) / (Passenger - 2) : ").strip()
        flag = 0
        if select.isdigit() and select == '2':

            if cust_lists:
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
                        print(f"{"Source":<20} {"Destination":<20} {"Cab_ID":<10} {"Fare":<20}")

                        for i in cust_lists:
                            if i["Name"] == pass_name and i["Login"] == True:

                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<20} {j["Dest_Loc"]:<20} {j["Cab_detail"]:<10}  ${j["Fare"]:<20}")
                                print()

                    else:
                        print("\n No Trips Were Taken \n")

                else:
                    print("\n Login To Access Further \n")
                    
            else:    
                print("\n No Passengers Registered Yet \n")

        elif select.isdigit() and select == '1':

            if driver_lists:
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

                        print(f"{"Source":<20} {"Destination":<20} {"Cust_ID":<10} {"Zula_Commission":<20} {"Fare":<20}")

                        for i in driver_lists:
                            if i["Name"] == driv_name and i["Login"] == True:
                                for j in i["History"]:
                                    print(f"{j["Src_Loc"]:<20} {j["Dest_Loc"]:<20} {j["Cust_ID"]:<10} ${j["Zula"]:<20} ${j["Fare"]:<20}")
                                print() 

                    else:
                        print("\n No Trips Were Taken \n")     

                else:
                    print("\n Login To Access Further \n")

            else:
                print("\n No Drivers Registered \n")

        else:
            print("\n Invalid Selection \n")

    elif choice == 6:

        print("\n Choice 1 - Edit Driver Profile - (Name) " \
              "\n Choice 2 - Edit Passenger Profile - (Name) " \
              "\n Choice 3 - Edit Driver - (Password) " \
              "\n Choice 4 - Edit Passenger - (Password) \n")
        
        choice = choice_chk(input("Choice : ").strip())
        flag = 0

        if choice == 1:
            chk_User_Name = input("Current Driver Name : ").strip()
            chk_Password = hashlib.sha256(input("Current Driver Password : ").strip().encode()).hexdigest()

            for i in driver_lists:
                if i["Name"] == chk_User_Name and i["Password"] == chk_Password:
                    flag = 1
                    if i["Login"] == True:

                        while True:
                            new_User_Name = input("New Driver Name : ").strip()

                            if any(ch["Name"] == new_User_Name for ch in driver_lists):
                                print("\n UserName Already Exists \n")
                            else:
                                break

                        while True:
                            choice = input("Are You Sure ? Y - (Yes) , N - (No) (y/n) : ").strip()

                            if choice.lower() == 'y':
                                i["Name"] = new_User_Name
                                print("\n UserName Successfully Changed \n")
                                break
                            elif choice.lower() == 'n':
                                print("\n No Changes Made \n")
                                break
                            else:
                                print("\n Invalid Choice \n")
                        break

                    else:
                        print("\n Login In To Edit Profile \n")
                        break

            if not flag:
                print("\n Invalid UserName or Password or No User Found \n")

        elif choice == 2:

            chk_User_Name = input("Current Passenger Name : ").strip()
            chk_Password = hashlib.sha256(input("Current Passenger Password : ").strip().encode()).hexdigest()
            
            for i in cust_lists:
                if i["Name"] == chk_User_Name and i["Password"] == chk_Password:
                    flag = 1
                    if i["Login"] == True:

                        while True:
                            new_User_Name = input("New Passenger Name : ").strip()

                            if any(ch["Name"] == new_User_Name for ch in cust_lists):
                                print("\n UserName Already Exists \n")
                            else:
                                break

                        while True:
                            choice = input("Are You Sure ? Y - (Yes) , N - (No) - (y/n) : ").strip()

                            if choice.lower() == 'y':
                                i["Name"] = new_User_Name
                                print("\n UserName Successfully Changed \n")
                                break
                            elif choice.lower() == 'n':
                                print("\n No Changes Made \n")
                                break
                            else:
                                print("\n Invalid Choice \n")
                        break

                    else:
                        print("\n Login In To Edit Profile \n")
                        break

            if not flag:
                print("\n Invalid UserName or Password or No User Found \n")

        elif choice == 3:

            chk_User_Name = input("Current Driver Name : ").strip()
            chk_Password = hashlib.sha256(input("Current Driver Password : ").strip().encode()).hexdigest()
            
            for i in driver_lists:
                if i["Name"] == chk_User_Name and i["Password"] == chk_Password:
                    flag = 1
                    if i["Login"] == True:
                        new_Password = hashlib.sha256(input("New Driver Password : ").strip().encode()).hexdigest()

                        while True:
                            choice = input("Are You Sure ? Y - (Yes) , N - (No) - (y/n) : ").strip()

                            if choice.lower() == 'y':
                                i["Password"] = new_Password
                                print("\n Password Successfully Changed \n")
                                break
                            elif choice.lower() == 'n':
                                print("\n No Changes Made \n")
                                break
                            else:
                                print("\n Invalid Choice \n")
                        break 

                    else:
                        print("\n Login In To Edit Password \n")
                        break

            if not flag:
                print("\n Invalid UserName or Password or No User Found \n")
            
        elif choice == 4:

            chk_User_Name = input("Current Passenger Name : ").strip()
            chk_Password = hashlib.sha256(input("Current Passenger Password : ").strip().encode()).hexdigest()
            
            for i in cust_lists:
                if i["Name"] == chk_User_Name and i["Password"] == chk_Password:
                    flag = 1
                    if i["Login"] == True:
                        new_Password = hashlib.sha256(input("New Passenger Password : ").strip().encode()).hexdigest()

                        while True:
                            choice = input("Are You Sure ? Y - (Yes) , N - (No) - (y/n) : ").strip()

                            if choice.lower() == 'y':
                                i["Password"] = new_Password
                                print("\n Password Successfully Changed \n")
                                break
                            elif choice.lower() == 'n':
                                print("\n No Changes Made \n")
                                break
                            else:
                                print("\n Invalid Choice \n")
                        break

                    else:
                        print("\n Login In To Edit Password \n")
                        break

            if not flag:
                print("\n Invalid UserName or Password or No User Found \n")

        else:
            print("\n Invalid Choice \n")

    elif choice == 7:
        print("\n Successfully Exited \n")
        break

    else:
        print("\n Invaild Choice \n")

if __name__ == "__Main__":
    print("Run")