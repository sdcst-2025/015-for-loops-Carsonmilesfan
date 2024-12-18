#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
sanders = int(input("enter an integer that is smaller than ten (it can be bigger if you want, it still works) => "))
jerick = 0
liechtenstein = 0
for miles in range(sanders):
    mile = miles + 1
    for i in range(mile):
        jerick = 10 ** i
        liechtenstein = liechtenstein + jerick
    
print(f"the sum of the series is {liechtenstein}")