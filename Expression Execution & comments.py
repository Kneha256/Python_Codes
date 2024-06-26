#String and numeric values can operate together with *
#Repeat the string value as the numeric value is.
a,b = 4,6
c = "@"
print(a*b*c)   #@@@@@@@@@@@@@@@@@@@@@@@@

a,b = 2,2
c = "Hello"
print(a*b*c) #HelloHelloHelloHello

#String with string can operate with +
#concatenation
a,b="2",3
c="@"
print((a+c)*b) #2@2@2@

a,b="hello",3
c="World"
print((a+c)*b) #helloWorldhelloWorldhelloWorld

#numeric values can opperate with all operatiors
a,b=2,3
c=4
print(a+b*c) #14

#Arithemetic expression with int and float will give float value
a,b=2,5.0
c=a*b
print(c) #10.0
    #or
a,b=2,5.0
print(a*b) 

#division operator with two integer will give float value
a,b=1,2
print(a/b) 0.5

#integer division-(//) with float, gives int value but display as float
a,b=1.5,3
c=a//b
print(c, a/b) #0.0 0.5

a,b=2,1
print(a//b) 2

#floor gives closest int, which is lesser or equal to the float value
#(a//b) is same as floor(a/b)

a,b=4,2
print(a/b) 2.0
   #and
a,b=4,2
print(a//b) 2

a,b=-12,5
print(a/b)
   #and
a,b=-12,5
print(a//b)

#remainder is negative when denominator is -ve 
a,b=3,2
print(a%b)

a,b=-3,2
print(a%b)

a,b=16,-5
print(a%b)

a,b=5,-2
print(a%b)

#comments-won't be printed (#)
   #Or for multiline comments
"""this
is my
first book"""


