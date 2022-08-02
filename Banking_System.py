class user():
    def __init__(self,name,email,age,gender,phone,cnic,address,password ):
        self.name=name
        self.email = email
        self.age=age
        self.gender=gender
        self.phone = phone
        self.cnic = cnic
        self.address = address
        self.password = password
    def show_detail(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Age : ",self.age)
        print("Gender: ",self.gender)
        print("Phone : ",self.phone)
        print("CNIC : ",self.cnic)
        print("Address : ",self.address)
        
        
class Bank(user):
    def __init__(self,name,email,age,gender,phone,cnic,address,password,balance):
        super().__init__(name,email,age,gender,phone,cnic,address,password)
        self.balance = balance
    
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount 
        
    def withdraw(self,amount):
        self.amount=amount
        if(self.amount>self.balance):
            print("Insufficient balance | your balance is", self.balance,"\n")
        else:
            self.balance=self.balance-self.amount
            print("\nYou have Withdraw ",self.amount," Successfully!")
            print("Remaining Balance is ",self.balance,"\n")
    def change_password(self,password):
      self.password = password

    def view_detail(self):
        self.show_detail()
        print("Account balance is ", self.balance,"\n")   


def main():
  while True:
    print("******************************************************************")
    print("                    Welcome to Markhor Banking\n")
    user_input = input('Press 1 for Login\nPress 2 for Exit\n')
    print("\n")
    if user_input == '1':
      print("******************************************************************")
      print("                   Login Details\n")
      email = input('Enter your Email: ')
      password = input('Enter your password: ')
      if email in users_dict.keys() and password == users_dict[email].password  :
          print('\nLogged in!\n')
      else:
          print('\nInvalid Credentials\n')    
          return main()
      while True:
        print("******************************************************************")
        print("                       User Menu\n")
        user_input = input('Press 1 for Deposit\nPress 2 for Withdrawl\nPress 3 for Money Transfer\nPress 4 for User Details\nPress 5 to Change Password\nPress 6 to Check Balance\nPress 7 to Exit\n')
        print("\n")
        if user_input == '1':
          print("******************************************************************")
          print("                        Deposit Money\n")
          print("Current balance is ",users_dict[email].balance)
          try:
            data = (int(input("Enter amount to Deposit : ")))
          except:
            print("Plz enter number...")
            continue
          users_dict[email].deposit(data)
          print("\nYou have Deposit ",data,"successfully!")
          print("Now your balance is ",users_dict[email].balance,"\n")
        elif user_input == '2':
          print("******************************************************************")
          print("                        Withdraw Money\n")
          print("Current balance is ",users_dict[email].balance)
          try:
            data = (int(input("Enter amount to Withdraw : ")))
          except:
            print("Plz enter number...")
            continue
          users_dict[email].withdraw(data)
        elif user_input == '3':
          print("******************************************************************")
          print("                        Transfer Money\n")
          receiver_email = input("Enter (User) Email : ")
          if receiver_email in users_dict.keys() :
            try:
              data = (int(input("Enter amount you want to send: ")))
              users_dict[email].withdraw(data)
              users_dict[receiver_email].deposit(data)
              print("\nYou have successfully send ",data," to ",receiver_email)
              print("Now your balance is",users_dict[email].balance,"\n")
            except:
              print("Plz enter number...")
          else:
            print("User does not Eist")
        elif user_input == '4':
          print("******************************************************************")
          print("                        User Details\n")
          users_dict[email].view_detail()
        elif user_input == '5':
          print("******************************************************************")
          print("                        Change Password\n")
          data = (input("Enter New Password : "))
          users_dict[email].change_password(data)
          print("\nYour password have been changed Successfully\n")
          return main()
        elif user_input == '6':
          print("******************************************************************")
          print("                        Account Balance\n")
          print("Your Account Balance is ",users_dict[email].balance,"\n")
        elif user_input == '7':
          print('Exit Successfully!\n')
          return main()
        else:
          print("Incorrect choice")
          continue
    elif user_input == '2':
      print("\nExit successfully!")
      print("******************************************************************")
      break
    else:
      print("Incorrect choice\n")
      continue

users_dict = {} 

user1=Bank("Usman","usman@gmail.com",21,"Male","03477777777","3730177777777","Rawalpindi, Pakistan","123",50000)
users_dict[user1.email] = user1

user2=Bank("Ahmed","ahmed@gmail.com",20,"Male","03477777777","3730177777777","Jhelum, Pakistan","123",70000)
users_dict[user2.email] = user2

user3=Bank("Hamza","hamza@gmail.com",19,"Male","03477777777","3730177777777","Gujar khan, Pakistan","123",90000)
users_dict[user3.email] = user3

user4=Bank("Awais","Awais@gmail.com",19,"Male","03477777777","3730177777777","Rwalpindi, Pakistan","123",120000)
users_dict[user4.email] = user4

user5=Bank("Mobeen","Mobeen@gmail.com",19,"Male","03477777777","3730177777777","Gujar khan, Pakistan","123",150000)
users_dict[user5.email] = user5

user6=Bank("sherry","sherry@gmail.com",25,"Male","03477777777","3730177777777","Jhelum, Pakistan","123",85000)
users_dict[user6.email] = user6

user7=Bank("Tufail Shah","tufail@gmail.com",25,"Male","03477777777","3730177777777","Islamabad, Pakistan","123",250000)
users_dict[user7.email] = user7

main()

