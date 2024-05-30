# prime_counter
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
