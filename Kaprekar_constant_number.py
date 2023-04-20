# Kaprekar's constant number: 6174
#       -- Discoverd by Indian mathematician D. R. Kaprekar.
#
# Rule:
# 1. Enter 4 digit number such that there exist at least 2 different digits (All four digits cannot be same)
# 2. Arrange the 4 digits in descending.
# 3. Same number arrange the digits in ascending order.
# 4. Subtract the smaller number from the bigger number.
# 5. Go back to step 2 and repeat until Kaprekar's constant number is reached.


class Fun_math(object):
    def Kaprekar_Constant(self):
        x = input('Enter a four digit Number with at least two different digits : ')
        while len(str(x)) != 4:
            print('Number is not four digit')
            x = input('Enter a four digit Number with at least two different digits : ')
        
        str_x = str(x)
        
        while all(ch == str_x[0] for ch in str_x):
            print('All four digits of the number are same')
            x = input('Enter a four digit Number with at least two different digits : ')
            str_x = str(x)
        
        print('\n')
        i=0
        x = int(x)
        while x != 6174:
            digits = [int(d) for d in str(x)]
            digits_sorted = sorted(digits)
            a_number = int(''.join(map(str, digits_sorted)))
            d_number = int(''.join(map(str, digits_sorted[::-1])))
            
            x = d_number - a_number
            
            i += 1
            print(f"Iteration number {i}: {d_number} - {a_number} = {x}")

        
        print('\n')
        print(f"The Kaprekar's constant number {x} if found")
        print(f"Number of iteration to reach the Kaprekar's constant number: {i}")


        
        
        
s = Fun_math()
s.Kaprekar_Constant()

"""
--- Case Study ---
Enter a four digit Number with at least two different digits : 3689
Iteration number 1: 9863 - 3689 = 6174

The Kaprekar's constant number 6174 if found
Number of iteration to reach the Kaprekar's constant number: 1

"""
