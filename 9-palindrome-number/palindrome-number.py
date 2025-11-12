class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0
        while num > 0:
            ld=num % 10
            result = (result*10) + ld
            num = num //10
        return x==result

#Explaination 
   # first we will take a dummy integer where we have to store the number to check in the last
   #suppose digit is x = 1234
   #     num = x   number is stored in num now
             #now num = 1234 
   #     result = 0   result will be initially 0 
            # coz (0*10)+ last second digit
            # from this we will be able to get the intial digit last one 
   #     while num > 0:
   #         ld=num % 10     # here we find the remainder
   #         result = (result*10) + ld  # here we change the digit 
   #         num = num //10       # here we will decrese the digit 
   #     return x==result    #checking  

   #ITERATIONS:
    # (0 * 10) + 4 = 4
    #          V
    # (4 * 10) + 3 = 43  
    #          V
    #(43*10) + 2 = 432
    #          V
    #(432*10) + 1 = 4321 
    # check the digit x == num