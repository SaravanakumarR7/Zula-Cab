import hashlib
class customer:

    id_count = 0

    def __init__(self,name,password,age,initial_loc,login,tot_trips,history):
        customer.id_count += 1
        self.id = customer.id_count
        self.name = name
        self.password = self.encrypt(password)
        self.age = age
        self.initial_loc = initial_loc
        self.login = login
        self.tot_trips = tot_trips
        self.history = history
        
    def encrypt(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def show(self):
        print(f"ID : {self.id} Name : {self.name} Password : {self.password} Age : {self.age} Location : {self.initial_loc} Login : {self.login} Total_trips : {self.tot_trips}")

if __name__ == "__Customer__":
    print("Run")