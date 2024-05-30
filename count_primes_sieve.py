from gmpy2 import is_prime
from datetime import timedelta
import sys,time

sieve_size = 10000000
strt = sieve_size - sieve_size%6 -1
# simple sieve of primes to 10,000,000
p = bytearray([0] * sieve_size)
p[2] = 1
p[3] = 1 
for i in range(5,sieve_size+1,6): 
    if is_prime(i):   p[i] = 1
    if is_prime(i+2): p[i+2] = 1

n = int(input("Count primes to: >"))
start_time = time.time() 
c=0
if n < sieve_size:
    c =  sum(p[1:n+1])
else:
    c = sum(p) 
    for i in range(strt,n+1,6):  # just 6k±1
        if is_prime(i):   c+=1 # 6k-1
        if is_prime(i+2): c+=1 # 6k+1
         
    
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")
