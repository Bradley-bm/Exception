bill = int(input("Enter the bill amount: "))
paid = int(input("Enter the amount paid: "))
while True:
    if bill < 0 or paid < 0:
        print("Invalid amount.")
        break
    due = paid - bill
    if due < 0:
        print("Insufficient payment.")
        continue
    elif due == 0:
        pass
    else:
        print("Bill amount: $", bill)
        print("Amount paid: $", paid)
        print("Change due: $", round(due, 2))
        break
    print("Exact payment. No change required.")
    break
