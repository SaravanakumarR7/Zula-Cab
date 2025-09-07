import hashlib

def loc_chk(initial_loc):
    if len(initial_loc) == 1 and "A" <= initial_loc <= "H":
        return True
    return False

def driv_loc():

    while True:
        location = input("Initial Location - Cab (A - H) : ").strip().upper()
        if not loc_chk(location):
            print("\n Invaild Location \n")
        else:
            return location

def Driver_log(driver_lists,Log_Name_Driver,Log_Password_Driver):

    Log_Password_Driver = hashlib.sha256(Log_Password_Driver.encode()).hexdigest()

    for i in driver_lists:
        if i["Name"] == Log_Name_Driver and i["Password"] == Log_Password_Driver:
            if i["Login"] == False:
                print(f"\n Welcome {i["Name"]} - Driver, You have Successfully Logged In \n")
                i["Login"] = True
                i["Location"] = driv_loc()
                return True
            else:
                print("\n Account Already Logged In \n")
                return False
        
    print("\n Invalid UserName or Password \n")
    return False