# Balance Parenthesis
# Implement a function that takes an array testVariable containing opening ( and closing parenthesis ) and determines whether the brackets in the array are balanced or not. The function also takes startIndex = 0 and currentIndex = 0 as parameters.

testVariable = input()
open = ['(', '[', '{']
close = [')', ']', '}']
op,cl =0,0
for i in testVariable:
    if (i in open):
        op+=1
    if (i in close):
        cl+=1
if (op==cl):
    print("It is balanced parenthesis")
else: 
    print('It is Unbalanced parenthesis')

