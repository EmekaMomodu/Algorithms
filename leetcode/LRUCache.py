"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    # TODO add more comments for revision sake
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        # initialise cache which is an empty dict which would have the structure (key -> Node(key, value))
        self.cacheDict = dict()
        self.cacheLinkedList = LinkedList()
        # initialise currentCache size
        self.currentCacheSize = 0

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        # if key already exists, update value in node, and make node the head
        if key in self.cacheDict:
            node = self.cacheDict[key]
            self.cacheLinkedList.deleteNode(node)
            updatedNode = Node(key, value)
            self.cacheLinkedList.insertNodeAtHead(updatedNode)
            self.cacheDict[key] = self.cacheLinkedList.head
        # if new key, and cache size is < maxSize, add (key, node) to dict and make node the head
        elif key not in self.cacheDict and self.currentCacheSize < self.maxSize:
            node = Node(key, value)
            self.cacheLinkedList.insertNodeAtHead(node)
            self.cacheDict[key] = self.cacheLinkedList.head
            self.currentCacheSize += 1
        # if cache size is at maxCapacity, remove tail and remove key, add new key and make node head
        else:
            keyToDelete = self.cacheLinkedList.tail.key
            self.cacheDict.pop(keyToDelete)
            self.cacheLinkedList.deleteNode(self.cacheLinkedList.tail)
            node = Node(key, value)
            self.cacheLinkedList.insertNodeAtHead(node)
            self.cacheDict[key] = self.cacheLinkedList.head
            self.currentCacheSize += 1


    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cacheDict:
            return None
        # make node head
        node = self.cacheDict[key]
        self.cacheLinkedList.deleteNode(node)
        node.prev = None
        node.next = None
        self.cacheLinkedList.insertNodeAtHead(node)
        self.cacheDict[key] = self.cacheLinkedList.head
        # return value
        return self.cacheDict[key].value

    def getMostRecentKey(self):
        # Write your code here.
        # return head
        return self.cacheLinkedList.head.key


# implement a doubly linked list class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtHead(self, node):
        # if head is None then point head and tail to node
        if self.head is None:
            self.head = node
            self.tail = node
        # else make node head
        else:
            tempHead = self.head
            node.next = tempHead
            tempHead.prev = node
            self.head = node

    def deleteNode(self, node):
        # sole node
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
        # head node
        elif node.prev is None and node.next is not None:
            node.next.prev = None
            self.head = node.next
        # tail node
        elif node.prev is not None and node.next is None:
            node.prev.next = None
            self.tail = node.prev
        # inbetween node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
