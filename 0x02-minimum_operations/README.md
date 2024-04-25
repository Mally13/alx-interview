# Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
## Example:
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

```
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```

```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```


## Concepts Needed:
### Dynamic Programming:
Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
Dynamic Programming (GeeksforGeeks) - https://www.geeksforgeeks.org/dynamic-programming/

### Prime Factorization:
Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.
Prime Factorization (Khan Academy) - https://intranet.alxswe.com/rltoken/cFcADpVYRCl5pdut-Lemmg 

### Code Optimization:
Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
How to optimize Python code - https://intranet.alxswe.com/rltoken/98ZF5bRckUKror6pGJQlHQ

### Greedy Algorithms:
The problem can also be approached with greedy algorithms, choosing the best option at each step.
Greedy Algorithms (GeeksforGeeks) - https://intranet.alxswe.com/rltoken/k6-mba0b4nayJi0VqYhKjQ

### Basic Python Programming:
Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
Python Functions (Python Official Documentation) - https://intranet.alxswe.com/rltoken/ao3SJVl4yY1SfugfVa3anw