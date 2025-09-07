def loc_chk(initial_loc):
    if len(initial_loc) == 1 and "A" <= initial_loc <= "H":
        return True
    return False

def Pick(ch):

    while True:
        if ch == "Hail":
            choice = input("Hail Taxi : (Y - Yes) , (N - No) - (y/n) : ").strip()
        elif ch == "Book":
            choice = input("Book Taxi : (Y - Yes) , (N - No) - (y/n) : ").strip()
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("\n Invalid Choice - Enter Correct Choice(y/n) \n")
        
def Define_loc(ch):

    while True:
        if ch == "src":
            loc = input("Initial Location - Cust (A - H) : ").strip().upper()
        elif  ch == "dest":
            loc = input("Destination Location - Cust (A - H) : ").strip().upper()
        if not loc_chk(loc):
            print("\n Invalid Location \n")
        else:
            return loc
        
def calc_fair(dist):
    return dist * 10

def Zula_Ride(driver_lists,route_locations_cab,id,cust_lists):

    if Pick("Hail"):
        flag = 0        
        for i in driver_lists:
            if i["Rest"] == False:
                flag = 1
                break

        if flag:
            print("\n Available Taxis and their Location \n")

            print(f"{"ID":<5} {"Location":<10} {"Rest":<10}")
            for i in driver_lists:
                if i["Rest"] != True:
                    print(f"{i["id"]:<5} {i["Location"]:<10} {str(i["Rest"]):<10}")
            nearest_cab(driver_lists,route_locations_cab,id,cust_lists)

        else:
            print("No Taxis Currently Available or Active")
            return False
        
def nearest_cab(driver_lists,route_locations_cab,id,cust_lists):

    Min_dist_find = float("inf")
    cust_src_loc = Define_loc("src")
    while True:
        cust_dest_loc = Define_loc("dest")
        if cust_dest_loc != cust_src_loc:
            break
        else:
            print("\n Source and Destination Cannot be Same \n")

    trips = float("inf")

    for i in driver_lists:

        if i["Login"] == True and i["Rest"] == False:
            src_dist = abs(route_locations_cab[i["Location"]] - route_locations_cab[cust_src_loc])
            if Min_dist_find > src_dist or (Min_dist_find == src_dist and trips > i["Total_trips"]):
                Min_dist_find = src_dist
                trips = i["Total_trips"]
                curr_driv_id = i["id"]
                curr_driv_Name,curr_driv_Loc,curr_driv_Age = i["Name"],i["Location"],i["Age"]

    dest_dist = abs(route_locations_cab[cust_src_loc] - route_locations_cab[cust_dest_loc])
    fare = calc_fair(Min_dist_find) + calc_fair(dest_dist)
    print(f"{"Name":<15} {"Age":<10} {"Location":<10} {"Fare":<10}")
    print(f"{curr_driv_Name:<15} {curr_driv_Age:<10} {curr_driv_Loc:<10} {fare:<10}")

    if Pick("Book"):
        print("\n Succesfully Booked - :) \n")

        for i in driver_lists:
            i["Rest"] = False

        for i in driver_lists:
            if i["Name"] == curr_driv_Name:
                i["Total_trips"] += 1
                i["Earnings"] += round(fare * 0.7,2)
                i["Zula"] += round(fare - (fare * 0.7),2)
                i["Rest"] = True
                i["Location"] = cust_dest_loc
                i["History"].append({
                                    "Src_Loc" : cust_src_loc, 
                                    "Dest_Loc" : cust_dest_loc, 
                                    "Cust_ID" : id,  
                                    "Zula" : round(fare - (fare * 0.7),2),
                                    "Fare" : round(fare,2)
                                    })
                break
            
        for i in cust_lists:
            if i["id"] == id:
                i["Location"] = cust_dest_loc
                i["Total_trips"] += 1
                i["History"].append({
                    "Src_Loc" : cust_src_loc,
                    "Dest_Loc" : cust_dest_loc,
                    "Cab_detail" : curr_driv_id,
                    "Fare" : round(fare,2)
                })
                return True
    
    else:
        print("\n Booking Cancelled - :( \n")
        return False

if __name__ == "__Customer_login":
    print("Run")
