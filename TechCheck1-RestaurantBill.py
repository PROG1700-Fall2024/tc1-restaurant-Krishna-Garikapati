"""Student Name:Krishna Priyanka Garikapati
Student W#: W0502117"""
#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.



#Caculating Restaurant bill
def main():
 billamount=float(input("Please enter the bill amount:"))
 print("Your original bill amount is $", billamount)
 #Tax=15% of original bill amount
 taxamount=((15/100)*billamount)
 print("The tax on bill is $", taxamount)
 #Tip=20% of original bill amount
 tip=((20/100)*billamount)
 print("The tax on bill is $", tip )
 Totalbill=(billamount+taxamount+tip)
 print("The total amount of bill is $", Totalbill )
main()