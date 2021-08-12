"""

  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.


  A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
  branch is a path of nodes in a tree that starts at the root node and ends at
  any leaf node.

"""

import unittest


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    branchSumList = []
    branchSumsHelper(root, branchSumList, 0)
    return branchSumList


def branchSumsHelper(root, branchSumList, runningSum):
    if root is None:
        return

    newRunningSum = runningSum + root.value

    if root.left == None and root.right == None:
        branchSumList.append(newRunningSum)
        return

    branchSumsHelper(root.left, branchSumList, newRunningSum)
    branchSumsHelper(root.right, branchSumList, newRunningSum)


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


"""
Test Case 1
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": "10", "right": null, "value": 5},
      {"id": "6", "left": null, "right": null, "value": 6},
      {"id": "7", "left": null, "right": null, "value": 7},
      {"id": "8", "left": null, "right": null, "value": 8},
      {"id": "9", "left": null, "right": null, "value": 9},
      {"id": "10", "left": null, "right": null, "value": 10}
    ],
    "root": "1"
  }
}
Test Case 2
{
  "tree": {
    "nodes": [
      {"id": "1", "left": null, "right": null, "value": 1}
    ],
    "root": "1"
  }
}
Test Case 3
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": null, "value": 1},
      {"id": "2", "left": null, "right": null, "value": 2}
    ],
    "root": "1"
  }
}
Test Case 4
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": null, "right": null, "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3}
    ],
    "root": "1"
  }
}
Test Case 5
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3},
      {"id": "4", "left": null, "right": null, "value": 4},
      {"id": "5", "left": null, "right": null, "value": 5}
    ],
    "root": "1"
  }
}
Test Case 6
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": "10", "right": "1-2", "value": 5},
      {"id": "6", "left": "1-3", "right": "1-4", "value": 6},
      {"id": "7", "left": null, "right": null, "value": 7},
      {"id": "8", "left": null, "right": null, "value": 8},
      {"id": "9", "left": null, "right": null, "value": 9},
      {"id": "10", "left": null, "right": null, "value": 10},
      {"id": "1-2", "left": null, "right": null, "value": 1},
      {"id": "1-3", "left": null, "right": null, "value": 1},
      {"id": "1-4", "left": null, "right": null, "value": 1}
    ],
    "root": "1"
  }
}
Test Case 7
{
  "tree": {
    "nodes": [
      {"id": "0", "left": "1", "right": null, "value": 0},
      {"id": "1", "left": "10", "right": null, "value": 1},
      {"id": "10", "left": "100", "right": null, "value": 10},
      {"id": "100", "left": null, "right": null, "value": 100}
    ],
    "root": "0"
  }
}
Test Case 8
{
  "tree": {
    "nodes": [
      {"id": "0", "left": null, "right": "1", "value": 0},
      {"id": "1", "left": null, "right": "10", "value": 1},
      {"id": "10", "left": null, "right": "100", "value": 10},
      {"id": "100", "left": null, "right": null, "value": 100}
    ],
    "root": "0"
  }
}
Test Case 9
{
  "tree": {
    "nodes": [
      {"id": "0", "left": "9", "right": "1", "value": 0},
      {"id": "9", "left": null, "right": null, "value": 9},
      {"id": "1", "left": "15", "right": "10", "value": 1},
      {"id": "15", "left": null, "right": null, "value": 15},
      {"id": "10", "left": "100", "right": "200", "value": 10},
      {"id": "100", "left": null, "right": null, "value": 100},
      {"id": "200", "left": null, "right": null, "value": 200}
    ],
    "root": "0"
  }
}

Your Solutions



Run Code
Solution 1
Solution 2
Solution 3
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    branchSumList = []
	branchSumsHelper(root, branchSumList, 0)
	return branchSumList

def branchSumsHelper(root, branchSumList, runningSum):
	if root is None:
		return
	
	newRunningSum = runningSum + root.value
	
	if root.left == None and root.right == None:
		branchSumList.append(newRunningSum)
		return
	
	branchSumsHelper(root.left, branchSumList, newRunningSum)
	branchSumsHelper(root.right, branchSumList, newRunningSum)
		
		

1
# This is the class of the input root. Do not edit it.
2
class BinaryTree:
3
    def __init__(self, value):
4
        self.value = value
5
        self.left = None
6
        self.right = None
7
​
8
​
9
def branchSums(root):
10
    branchSumList = []
11
    branchSumsHelper(root, branchSumList, 0)
12
    return branchSumList
13
​
14
def branchSumsHelper(root, branchSumList, runningSum):
15
    if root is None:
16
        return
17
    
18
    newRunningSum = runningSum + root.value
19
    
20
    if root.left == None and root.right == None:
21
        branchSumList.append(newRunningSum)
22
        return
23
    
24
    branchSumsHelper(root.left, branchSumList, newRunningSum)
25
    branchSumsHelper(root.right, branchSumList, newRunningSum)
26
        
27
        
28
​

Custom Output

Raw Output

Submit Code
Run or submit code when you're ready.

"""
