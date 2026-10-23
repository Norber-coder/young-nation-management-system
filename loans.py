loans = []

def request_loan(name,amount):
  inerest=amount*0.05
  total=amount+interest

  loans.append({
  "name":name,
  "loan":loan,
  "interest":interest,
  "total":total,
})

print("Loan Approved")
print("Total Repayment",total)