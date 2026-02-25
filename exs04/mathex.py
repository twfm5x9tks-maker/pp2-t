#1
import math

degree=int(input())
rad=math.radians(degree)

print(round(rad, 6))



#2
heig=int(input())
first=int(input())
second=int(input())
avg=math.fsum([first,second])/2
area=avg*heig

print(area)


#3
n=int(input())
s=int(input())
area=(n*s**2)/(4*math.tan(math.pi/n))
print(math.trunc(area))


#4
leng=float(input())
heig=float(input())
area=math.prod([leng, heig])
print(area)