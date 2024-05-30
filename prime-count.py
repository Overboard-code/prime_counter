from gmpy2 import is_prime
from datetime import timedelta
import sys,multiprocessing,time

def k6_is_prime(n):  
    if (n <= 1):  
        return False      
    if (n <= 3):  
        return True        
    if (n%2 == 0 or n%3 == 0):  
        return False      
    limit = int(n**.5)+1
    for i in range(5,limit,6): 
        if (n%i == 0 or n%(i+2) == 0):  
            return False          
    return True  

def prime_near(n,prev=False): 
    s = n-n%6+5  # get next 6k-1
    k6,stop = (-6,1) if prev else (6,n+70*6)  
    if prev:
        k6 = -6
        stop = 1
        s-=6
    for i in range(s,stop,k6):
        #print(f"Checking {i} and {i+2}")
        if prev:
            if is_prime(i+2): 
                return i+2
            if is_prime(i): 
                return i
        else:
            if is_prime(i): 
                return i
            if is_prime(i+2): 
                return i+2
    return -1
    

def prime_range(ste): 
    x = ste[1]
    y = ste[0]
    # Find number of primes from 1 to x
    if x <=1000:
       
        count = sum(p[y:x+1])
        return count
    count = 0
    if y < 5:
        count = 2
        y = 5
    for i in range(y,x,6):
        if is_prime(i):
            count += 1
        if is_prime(i+2):
            count += 1
    return count

# simple sieve primes to 1000
p = [1 if is_prime(i) else 0 for i in range(1,1001) ]

n = int(input("Count primes to: >"))
cpus = multiprocessing.cpu_count()
if n > 1000*cpus:
    a = int(n/cpus+.5)  # one less than # of CPUs
    nums = []
    k = n
    while k - a > 1:
        s = k-a
        s = s-s%6-1
        if s<a: s =1
        nums.append([s,k])
        k = s-1
    print(f"{nums=} ")  # Show the sets 
    start_time = time.time() 
    p =  multiprocessing.Pool(processes=(7)) # get some threads for our pool
    results=p.map(prime_range, nums) # one thread per arctan(1/xxxx)
    p.close()
    p.join()  # wait for them to finish
    c = sum(results)
else:
    start_time = time.time()
    c = prime_range([1,n])
print(f"From 1 to {n:,} there are {c:,}  primes") 

print(f" Search took {str(timedelta(seconds=time.time()-start_time))} ")

print(f"Next prime from {n} is {prime_near(n)}\nPrevios one is {prime_near(n,prev=True)} ") 