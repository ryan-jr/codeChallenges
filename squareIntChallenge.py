"""
Provided an integer n, print the square of each integer from zero, up to AND INCLUDING n.  Print each square on a new line.  

example:

input: 4

expected output:
0
1
4
9
16

"""


def printSquare(n):
  """
  Takes in an integer n, and prints out the square of each number from zero, up to and including n. 

  Runtime: O(n)
  """

  for i in range(0, n + 1):
    print(i * i)


print(printSquare(3))
print(printSquare(-1))
print(printSquare(0))
print(printSquare(-2))


"""
### Solution/Explanation

So this one is relatively straightforward, we take in a number, count up to it and square (AKA: multiply the number by itself) each number in the counting sequence up to and including the original number we were given.  

Key points here:
A.  A loop with range 
B.  Squaring and printing 

The for loop is pretty key here, you could use a while loop, but the for construct makes it easy for us, and since Python also includes a range (which is exclusive) we can use that to help us.  

The squaring is pretty straightforward as well as the printing.  


### Extra thinking
QA/potential constraints

How else could the loop be accomplished?
How would we handle if we got a string?
Can we construct it so that we only get/use positive integers?
"""