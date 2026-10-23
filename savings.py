savings = []

def add_saving(name,amount):
  savings.append({
   "name":name,
   "amount":amount
   })
  print("Saving added successfully")

def view_savings():
   print("\nSavings Records")

  for record in savings:
   pri nt(record)