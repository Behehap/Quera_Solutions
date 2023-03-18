import math

n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())

#prints the summerion of the numbers
sum = n1 + n2 + n3 + n4
print("Sum : " + "{:6f}".format(sum))

avr = sum / 4
print("Average : " + "{:6f}".format(avr))

pro = n1 * n2 * n3 * n4
print("Product : " + "{:6f}".format(pro))

# Bn = the bigger number
Bn1 = (abs(n1-n2) + (n1+n2)) / 2
Bn2 = (abs(n3-n4) + (n3+n4)) / 2 
Bn3 = (abs(Bn1-Bn2) + (Bn1+Bn2)) / 2
Maximum = Bn3
print("MAX : " + "{:6f}".format(Maximum))

# Sn = the smaller number
Sn1 = ((n1+n2) - abs(n1-n2)) / 2
Sn2 = ((n3+n4) - abs(n3-n4)) / 2 
Sn3 = ((Sn1+Sn2) - abs(Sn1-Sn2)) / 2
Minimum = Sn3
print("MIN : " + "{:6f}".format(Minimum))

