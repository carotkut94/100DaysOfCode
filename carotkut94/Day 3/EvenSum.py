# Solution statement for the problem statement of Day 3.
# Source Project Euler : https://projecteuler.net/problem=2
# Statement : Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Author : Deathcode aka carotkut94

# I started with the bruteforce approach by generating fibonacci number and checking it
# if it is an even or odd and then adding it to total if even


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = 0
total = 0
while True:
    f = fib(n)
    n += 1
    if f > 4000001:
        break
    if f % 2 == 0:
        total = total + f
print(total)

# and after solving this problem I wrote a quite of long list of fibonacci numbers like 1, 1, 2, 3, 5, 8, 13, 21, 34,
# 55, 89, 144, 233, 377, 610 after seeing them for quite a while i saw that even numbered fibonacci number is preceded
# and succeeded by 2 odd numbers i.e whole list can be seen as odd, odd, EVEN, odd, odd, EVEN, odd, odd, EVEN and soo on
# and now if we see clearly we just have to find a way via which we just have to remove all odd numbers from the list
# Here we have to change the N1 to 2 as first even fibonacci is 2 and N2 as 8 as second fibonacci sequence is 8, and
# other next fibonacci numbers can be generated as 4*N2+N1 i.e 4*8 + 2 = 34 and now N1 and N2 will be swapped and this
# will reduce the runtime of the app


def fib2(n):
    f1 = 2
    f2 = 8
    total = 10
    while True:
        fn = 4 * f2 + f1
        if fn >= n:
            return total
        total += fn
        f1, f2 = f2, fn


print(fib2(4000001))

# for further improvement I read that their exists a formula know as Binet's Formula which can be found at
# https://en.wikipedia.org/wiki/Fibonacci_number#Relation_to_the_golden_ratio
# I am studying this, once i have a clear picture of it, i will implement it too.
