"""
Problem: Remove nth Node from End of List



Statement
Given the head of a singly linked list, remove the nth

 node from the end of the list and return its head.

Constraints:

The number of nodes in the list is k.
1
≤
1≤
 k
≤
1
0
3
≤10
3

−
1
0
3
≤
−10
3
 ≤
 Node.value
≤
1
0
3
≤10
3

1
≤
1≤
 n
≤
≤
 k


"""

def remove_nth_last_node(head, n):
    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for i in range(n):
        right = right.next

    # Removal of the head node.
    if not right:
        return head.next

    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next to next element of left.
    left.next = left.next.next

    return head