##Problem 1:
##Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
##
##The following variables contain values as described below:
##
##balance - the outstanding balance on the credit card
##
##annualInterestRate - annual interest rate as a decimal
##
##monthlyPaymentRate - minimum monthly payment rate as a decimal
##
##For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:
##
##Month: 1
##Minimum monthly payment: 96.0
##Remaining balance: 4784.0
##Be sure to print out no more than two decimal digits of accuracy - so print
##
##Remaining balance: 813.41
##instead of
##
##Remaining balance: 813.4141998135 
##Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:
##
##Total paid: 96.0
##Remaining balance: 4784.0

monthlyInterestRate = (annualInterestRate / 12.0)
month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
totalPaid = 0
for m in month:
    
    minMonthlyPayment = monthlyPaymentRate * balance
    remainingBalance = balance - minMonthlyPayment
    balance = remainingBalance + (monthlyInterestRate * remainingBalance)
    totalPaid += minMonthlyPayment

    
    print "Month:", m+1
    print "Minimum monthly payment:", round(minMonthlyPayment ,2)
    print "Remaining balance:", round(balance * 100) / 100
print "Total paid:", round(totalPaid * 100) / 100
print "Remaining balance:", round(balance * 100) / 100


##Problem 2:
##Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment,
##we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
##
##In this problem, we will not be dealing with a minimum monthly payment rate.
##
##The following variables contain values as described below:
##
##balance - the outstanding balance on the credit card
##
##annualInterestRate - annual interest rate as a decimal
##
##The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
##
##Lowest Payment: 180 

monthlyInterestRate = annualInterestRate / 12.0

monthly_payment = 10
updated_balance = balance - 10
while updated_balance > 0:
    monthly_payment += 10
    updated_balance = balance
    month = 0
    while month < 12 and updated_balance > 0:
        updated_balance -= monthly_payment
        interest = monthlyInterestRate * updated_balance
        updated_balance += interest
        month += 1
    updated_balance = updated_balance * 100 / 100
print "Lowest monthly payment:", monthly_payment

##Problem 3:
##Rewrite your code for faster execution, using bisection search:

monthlyInterestRate = annualInterestRate / 12.0
lowbound = balance / 12
highbound = (balance * (1 + monthlyInterestRate) ** 12) / 12
month = 0
remain = balance
epsilon = 0.10
while (remain >= epsilon):
    
    guess_min = (lowbound + highbound) / 2
        
    for i in range(1, 13):
        
        new_balance = remain - guess_min
        interest = annualInterestRate / 12 * new_balance
        remain = new_balance + interest
        
    if remain < 0:
        highbound = guess_min
        remain = balance

    elif remain > epsilon:
        lowbound = guess_min
        remain = balance

print "Lowest Payment: %.2f" %(guess_min)
