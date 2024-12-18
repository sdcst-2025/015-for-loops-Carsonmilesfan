"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""
jesus = 0
ifmama = 0
balance = int(input("what is your current credit card balance => "))

for i in range(12):
    ii = i + 1
    notmuchtime = int(input(f"Enter total purchases for month {ii} => "))
    quiteawhile = int(input(f"Enter total payments for month {ii} => "))
    senorpeter = balance - quiteawhile
    if senorpeter < 0:
        print(f"sorry insufficient funds, using total balance ({balance})")
        quiteawhile = balance
        balance = 0
    else:
        balance = balance - quiteawhile
    willmakehersmile = notmuchtime - quiteawhile
    ifmama = ifmama + willmakehersmile
    meets = 0.02 * willmakehersmile
    jesus = jesus + meets
    print(f"2% interest has been charged: {jesus}")
    balance = balance - jesus
    print(f"your closing balance is: {balance}")
    tonight = int(input("how much money did you make this month => "))
    balance = balance + tonight

