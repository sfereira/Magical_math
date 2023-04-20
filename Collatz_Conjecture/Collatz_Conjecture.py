# Collatz conjecture
# 
# Rule:
# 1. Insert a natural number
# 2. If the number n if even, divide by `2`.
# 3. If the number n is odd, do `3n + 1`.
# 4. Repeat steps 2 and 3 until the number is 1.

class Fun_math(object):
    def Collatz_conjecture(self,x):
        initial= x
        s_x=[x]
        i = 0
        while x != 1:
            
            if x % 2 == 0:
                x = x // 2
            
            else:
                x = (3*x) + 1
            
            s_x.append(x)
            i +=1
        
        #print('The trend followed')
        #print(s_x)
        print(f"For {initial} --> Total number interation: {i} ")

        
        
# Run Case Study

s = Fun_math()
for i in range(2,10):
    result = s.Collatz_conjecture(i)
    
"""
For 2 --> Total number interation: 1 
For 3 --> Total number interation: 7 
For 4 --> Total number interation: 2 
For 5 --> Total number interation: 5 
For 6 --> Total number interation: 8 
For 7 --> Total number interation: 16 
For 8 --> Total number interation: 3 
For 9 --> Total number interation: 19 
"""
