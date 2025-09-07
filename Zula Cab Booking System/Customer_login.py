import hashlib

def Cust_log(cust_lists,Log_Name_Cust,Log_Password_Cust):

    Log_Password_Cust = hashlib.sha256(Log_Password_Cust.encode()).hexdigest()

    for i in cust_lists:
        if i["Name"] == Log_Name_Cust and i["Password"] == Log_Password_Cust:
            if i["Login"] == False:
                print(f"\n Welcome {i["Name"]} - Passenger, You have Successfully Logged In \n")
                i["Login"] = True
                return True
            else:
                print("\n Account Already Logged In \n")
                return False
    print("\n Invalid UserName or Password \n")
    return False