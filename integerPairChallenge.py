import collections

"""
# Problem Definition

Given an array/list of integers, determine how many pairs of integers there are.  Return the number of pairs as a float


Example: 

input: pairList = [2, 3, 10, 20, 10, 10, 2, 6]
expected output: 3.0

There are 2 pairs (2, and 10)

"""

def pairCounter(arr):
  """
  Takes in an array of intetgers, counting the number of pairs of each integer.  Returns a float of the number of pairs

  Operates in O(n) time complexity because it has to run through everything
  """

  pairCounter = 0

  # We're using a Counter object here for data, if unavailable this could be constructed using a Python dict
  data = collections.Counter(arr)



  
  for k,v in data.items():
    if v == 1:
      pass
    elif v % 2 == 0:
      pairCounter += (v/2)
    else:
      sub = v % 2
      pairCounter += (v - sub) / 2

  return (float(pairCounter))

"""

  pairDict = {}

  for integerItem in arr:
    if integerItem in pairDict:
      pairDict[integerItem] += 1
    else:
      pairDict[integerItem] = 1

  

"""



print(pairCounter([1, 2, 2, 1, 1, 3, 9, 1, 2]))
print(pairCounter([9, 9, 9, 9, 5]))
print(pairCounter([9, 9, 9, 9, 9]))
print(pairCounter([]))
print(pairCounter([0]))
print(pairCounter(["a", "b", "c", "b"]))



"""
### SOLUTION/EXPLANATION

Ok, so there are some keys/tips to this
A.  We know we're getting an array/list of integers in
B.  We know that we want to get a float out
C.  We need to count each integer and see how many 'pairs' there are*
D.  A pair is 2 of something*

### On point C
Because of these constraints, we can count/increment the number of integers there are in a given array using the Counter method in the Collections library.  

If the Collections library wasn't available we would use a Python dictionary/hashmap/hashset/key-value pair

Since dicts provide key/value pairs we want the integer to be the key and the number of times it occurs to be the value.  A couple things to note here:

A.  In Python, dict keys have to be strings
B.  In Python 3.7 dicts are insertion ordered, in 3.6 and prior they were/are unordered meaning that for 3.7 the order something is inserted into the dict, is where it will be in the dict.  

https://docs.python.org/3/whatsnew/3.7.html
https://mail.python.org/pipermail/python-dev/2017-December/151283.html

### On point D
We know that if something is easily divisible by 2, that it will sum nicely with our pair, but what if we had something like five 3 integers in our list?  5 / 2 = 2.5, and we don't want to know the half-pairs.  For this, we can use a modulo operator and take out the remainder, then we can subtract that from the number of items that we have, get an even number, divde the even number by 2, and end up with the number of pairs of said integer

Aside: Modulo gets the remainder part of division, so 5 % 2 would be 1, since the remainder is 1.  

Soooooo it would look like:
Let's say that there are 5 instances of a given integer in our array/list...

1.  5 % 2 = 1 (because 5 / 2 leaves us with a remaineder of 1)
2.  5 - 1 = 4 (we're subtracting because we want the number of pairs, that extra 1 isn't part of a pair)
3.  4 / 2 = 2 (we get 2 pairs)


### Extra thinking
Let's think about some potential constraints/QA issues:

We can deal with these later, but it's good to have them in mind.  

What if the array was empty?
What if the array had strings of numbers?
What if the array had strings, or letters, or characters?
What if the array only held a 0?
What if the array held a large amount of a single number?

Is there a way to make this more readable, or run faster?


"""

