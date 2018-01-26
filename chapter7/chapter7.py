import sys
import turtle
t=turtle.Screen()
p=turtle.Turtle()
a=turtle.Turtle()
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        e = "Test at line {0} ok.".format(linenum)
    else:
        e = ("Test at line {0} FAILED.".format(linenum))
    print(e)





mylist=[1,2,4,5,6,7,9,32,54,67]
mylist1=["hello","babab","sam","frank","newbe","conming","xbnhk"]
JAXSIN=["frank","wison","jaxsin","aronson"]
def count_odd(mylist):
    odd=0
    for i in mylist:
        if i%2 == 0:
            odd += 1
    print(odd)

count_odd(mylist)

def sum_even(mylist):
    sumeven=0
    for i in mylist:
        if i%2 == 0:
            sumeven += i
    print(sumeven)    
    
sum_even(mylist)

def sum_negative(mylist):
    sumnega=0
    for i in mylist:
        if i < 0:
            sumnega += i
    print(sumnega)

sum_negative(mylist)

def countword5(mylist):
    numwords=0
    for i in mylist:
        if len(i) == 5:
            numwords += 1
    return numwords
    
    
def primenumber(mylist):
    pn=0
    for i in mylist:
        if i == prime_number:
            prime_number += i
    print(primenumber)
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))

def before_sam(mylist):
    count=0
    for i in mylist:
        if i == "sam":
            count += 1
            break
        count += 1
    return count

def sqrt(n):
    approx = n/3
    while True:
        better = (approx + n/approx)/2
        print(better)
        if abs(approx-better)<0.001:
            return better
        approx = better

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



        
def test_suite():
    test(count_odd(mylist)==6)
    test(sum_even(mylist)==10)
    test(sum_negative(mylist)==-95)
    test(countword5(mylist1)==5)
    test(sum_even(mylist)==8)
    test(before_sam(mylist1)==3)
    test(before_sam(JAXSIN)==4)

test_suite()

path=[(160, 20), (-43, 10), (270, 8), (-43, 12)]


for (angle,dist) in path:
        a.right(angle)
        a.forward(dist)
        
house=[(45,141.4),(90,70.7),(90,70.7),(90,141.4),(135,100),(90,100),(90,100),(90,100)]

for(angle,dist)in house:
    p.left(angle)
    p.forward(dist)




