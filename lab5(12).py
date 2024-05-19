amo_bal = float(input("Enter your account balance: $"))
with_am = float(input("Enter withdrawal amount: $"))
if amo_bal>=1000 and amo_bal<=1500:
    if with_am >=500 and with_am <=1500:
        print("Transaction successful")
elif amo_bal ==200 and with_am ==300:
    print("Insufficient funds")
else:
    print("Invalid error")
