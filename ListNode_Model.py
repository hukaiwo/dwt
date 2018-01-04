#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#链表的节点
class ListNode:
    def __init__(self,x1, y1, x2, y2, frame):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.frame =frame
        self.next = None
#bundingbox的链表
class LinkList:
    root = None
    def __init__(self):
        self.root = None
#delete list
    def dele(self):
        self.root = 0
#append newNode
    def updataList(self, x1, y1, x2, y2, i):
        newNode = ListNode(x1, y1, x2, y2, i)
        if self.root is None:
            self.root = newNode
        else:
            tempNode = self.root
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = newNode
#find the last node
    def findTheLastPoint(self):
        tempRoot = self.root
        while tempRoot.next:
            tempRoot = tempRoot.next
        return tempRoot
#管理链表的节点
class manageNode:
    def __init__(self, res, i):
        self.node = res
        self.frame = i
        self.next = None
#管理链表的生成，删除等操作
class manageList:
    root = None

    def __init__(self):
        self.root = None


    def insert(self, newdata, i):
        newNode = manageNode(newdata, i)
        if not self.root:
            self.root = newNode
        else:
            tempNode = self.root
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = newNode


    def findTheLastNode(self):
        tempNode = self.root
        while tempNode.next:
            tempNode = tempNode.next
        return tempNode.node