# -*- coding: UTF-8 -*-
# 从尾到头输出单链表
# https://blog.csdn.net/cyuyanenen/article/details/51474623
# base struct come from https://www.tutorialspoint.com/python/python_linked_lists.htm
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.header = None

    def listprint(self):
        printval = self.header
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.header = Node("Mon 1")
e2 = Node("Tue 2")
e3 = Node("Wed 3")
e4 = Node("Thu 4")

list.header.nextval = e2
e2.nextval = e3
e3.nextval = e4

print("print from start:")
list.listprint()

def printFromEnd(node):
    if node.nextval is not None:
        printFromEnd(node.nextval)
    print node.dataval

print("print from end:")
printFromEnd(list.header)