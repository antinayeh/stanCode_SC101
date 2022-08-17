"""
File: add2.py
Name: Antina Yeh
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    helper1 = l1
    helper2 = l2

    # setting up first node
    val = helper1.val + helper2.val
    if val >= 10:
        remainder = val % 10
        ans = ListNode(remainder, None)
        carry_over = True
    else:
        ans = ListNode(val, None)
        carry_over = False

    # iterate until reach the end of both helper1 and helper2
    while helper1.next is not None or helper2.next is not None:
        if helper1.next is not None and helper2.next is not None:
            val = helper1.next.val + helper2.next.val
            helper2 = helper2.next
            helper1 = helper1.next
        elif helper1.next is not None:
            val = helper1.next.val
            helper1 = helper1.next
        elif helper2.next is not None:
            val = helper2.next.val
            helper2 = helper2.next
        # check if value is >= to 10
        if carry_over:
            val += 1
        if val >= 10:
            new_node = ListNode(val % 10, None)
            carry_over = True
        else:
            new_node = ListNode(val, None)
            carry_over = False
        # prepend new node
        new_node.next = ans
        ans = new_node
    # check if previous node >= 10
    if carry_over:
        new_node = ListNode(1, None)
        new_node.next = ans
        ans = new_node

    # prepend each node to a new linked list to reverse the list
    reverse_ans = ListNode(ans.val, None)
    while ans.next is not None:
        new_node = ListNode(ans.next.val, None)
        new_node.next = reverse_ans
        reverse_ans = new_node
        ans = ans.next
    return reverse_ans
    #######################


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
