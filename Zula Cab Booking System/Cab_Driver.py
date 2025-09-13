import hashlib
class Cab_driver:

    id_count = 0

    def __init__(self,name,password,age,initial_loc,login,earnings,rest,tot_trips,zula,history):
        Cab_driver.id_count += 1
        self.id = Cab_driver.id_count
        self.name = name
        self.password = self.encrypt(password)
        self.age = age
        self.initial_loc = initial_loc
        self.login = login
        self.earnings = earnings
        self.rest = rest
        self.tot_trips = tot_trips
        self.zula = zula
        self.history = history

    def encrypt(self,password):     
        return hashlib.sha256(password.encode()).hexdigest()
    
    def show(self):
        print(f"ID : {self.id} Name : {self.name} Password : {self.password} Age : {self.age} Location : {self.initial_loc} Login : {self.login} Earnings : {self.earnings} Rest : {self.rest} Total_trips : {self.tot_trips} Zula Commission : {self.zula}")

if __name__ == "__CabDriver__":
    print("Run")
