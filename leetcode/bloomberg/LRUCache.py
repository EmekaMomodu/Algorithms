"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

"""


class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete_node(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def move_node_to_head(self, node: Node) -> None:
        self.delete_node(node)
        self.add_node(node)

    def pop_tail(self) -> Node:
        popped_tail = self.tail.prev
        self.delete_node(popped_tail)
        return popped_tail

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.move_node_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self.cache[key] = node
            self.move_node_to_head(node)
        else:
            newNode = Node()
            newNode.key = key
            newNode.value = value
            self.add_node(newNode)
            self.cache[key] = newNode
            self.size += 1
            if self.size > self.capacity:
                popped_tail = self.pop_tail()
                del self.cache[popped_tail.key]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
