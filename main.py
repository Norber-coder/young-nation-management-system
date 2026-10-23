from savings import add_saving, view_savings
from loans import request_loan

while Truer:
  print("\nYOUNG NATION SYSTEM")
  Print("1.Add Saving")
  print("2.Request Loan")
  print("3.View Savings")
  print("4.Exit")

  choice= input("Choose:")

  if choice =="1":
   name= input("Member Name:")
   amount= float(input("Amount:"))
   add_saving(name,amount)

elif choice =="2":
   name= input("Member Name:")
   amount=float(input("Loan Amount:"))
   request_loan(name,amount)

elif =="3":
 view_savings()

elif choice =="4":
  break
