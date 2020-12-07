from mpmath import mp #You will have to install mpmath from http://mpmath.org/doc/current/setup.html
print("How many digits of PI after comma would you like to display?")
n = int(input()) 
mp.dps = n + 1
print("PI = ", mp.pi)