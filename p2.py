# Find grade using else if ladder

marks = float(input("enter your marks : "))

if marks> 1 or marks <0:
    print('''
*** Invalid input ***
Marks must be between 0 and 1 
             ''')
elif marks >= 0.9:
    print("Grade A")
elif marks >= 0.8:
    print("Grade B")
elif marks >= 0.7:
    print("Grade C")
elif marks >= 0.6:
    print("Grade D")
else:
    print("Grade F")

