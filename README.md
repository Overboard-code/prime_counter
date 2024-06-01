# prime_counter_MP
Counts prime numbers found from 1 to N.  uses multiproccesing. 

I wanted to multiproccess the counting of primes.  So I needed to start n tasks that would each use a CPU thread.  I leave one empty and let the rest work on a chunk of the problem.  

The result looks like: 
```
$ python prime_count_MP.py 
Count primes to: >123456789 
nums=[[1, 30864178], [30864179, 46296280], [46296281, 61728382], [61728383, 77160484], [77160485, 92592586], [92592587, 108024688], [108024689, 123456789]] 
thrds=7  chunk=15432098 
results=[1908156, 883607, 866683, 854944, 845074, 837807, 830989]
From 1 to 123,456,789 there are 7,027,260  primes
 Search took 0:00:11.864988 
```
For all the primes counted to a billion takes abot a minute on my old i7 laptop with 8 cputhreads. During the minute the 7 threads are 100% busy. 

```
$ python prime_count_MP.py 
Count primes to: >1000000000
nums=[[1, 249999976], [249999977, 374999980], [374999981, 499999984], [499999985, 624999988], [624999989, 749999992], [749999993, 874999996], [874999997, 1000000000]] 
thrds=7  chunk=125000000 
results=[13679317, 6392436, 6284113, 6204468, 6142847, 6093687, 6050666]
From 1 to 1,000,000,000 there are 50,847,534  primes
 Search took 0:01:19.134144 
```
# prime_counter_sieve

This code creates a numpy byte array of the same size as the number.  Then makes a with a 1 and 0 sieve for each prime.     Then we just do an np.sum() to find the prime count.  

If the number is less than 10 billion it is much faster than the multiproccesing code.  If much larger it runs slower. 

here is a run to 123,456,789 like above:
```
$ python prime_count_sieve.py 
Creating new sieve of 100,000,000 primes.
 Make sieve for 100,000,000 took 0:00:00.468188 
Count primes to: >123456789
Creating new sieve of 123,456,789 primes.
 Make sieve for 123,456,789 took 0:00:00.587500 
From 1 to 123,456,789 there are 7,027,260  primes
 Search took 0:00:00.648750 
```
Here is to 1 billion (5 seconds):
```
$ python prime_count_sieve.py 
Creating new sieve of 100,000,000 primes.
 Make sieve for 100,000,000 took 0:00:00.472750 
Count primes to: >1000000000
Creating new sieve of 1,000,000,000 primes.
 Make sieve for 1,000,000,000 took 0:00:05.326424 
From 1 to 1,000,000,000 there are 50,847,534  primes
 Search took 0:00:05.812908 

```
