import ListNode_Model

data_f = open("data_1.txt", "r")
lines = data_f.readlines()
useData = []
each_frame_boundingbox_list = []
a_bounding_box_data = []
for line in lines:
    if len(line.split('\n')[0].split(' ')) < 4:
        useData.append(each_frame_boundingbox_list)
        each_frame_boundingbox_list = []
        continue
    a_bounding_box_data = []
    data = line.split('\n')[0].split(' ')
    for i in range(4):
        a_bounding_box_data.append(int(data[i]))
    each_frame_boundingbox_list.append(a_bounding_box_data)




first = []
for i in range(len(useData[0])):
    theHeadOfEveryList = ListNode_Model.LinkList()
    theHeadOfEveryList.updataList(useData[0][i][0], useData[0][i][1], useData[0][i][2], useData[0][i][3], 1)
    first.append(theHeadOfEveryList)
theHeadOfEveryManageList = ListNode_Model.manageList()
theHeadOfEveryManageList.insert(first, 1)

for x in range(1, len(useData)):
    theLastManageNode = theHeadOfEveryManageList.findTheLastNode()
    theLastDelList = []    #每一条链表对应一个boundingbox，当找到后删除，在用了该链表之后立即删除

    nextFrame = []
    for i in range(len(theLastManageNode)):
        theLastDelList.append(theLastManageNode[i])
#每一帧的boundingbox
    for y in range(len(useData[x])):
        count = 0
        count1 = 0
        theDistanceOfTwoBoundingBox = []
        minestDistacne = 1000
        #每条链表的末端
        for n in range(len(theLastDelList)):
            theTempListNode = theLastDelList[n].findTheLastPoint()
            a = ((theTempListNode.x1 + theTempListNode.x2) / 2.0 - (useData[x][y][0] + useData[x][y][2]) / 2.0) ** 2 + ((theTempListNode.y1 + theTempListNode.y2) / 2.0 - (useData[x][y][1] + useData[x][y][3]) / 2.0) ** 2
            theDistanceOfTwoBoundingBox.append(a)
            minestDistacne = min(minestDistacne, theDistanceOfTwoBoundingBox[-1])
        for n in range(len(theDistanceOfTwoBoundingBox)):
            if minestDistacne == theDistanceOfTwoBoundingBox[n]:
                count = n
        #找到在原来位置相同的链表在尾端加数据
        for i in range(len(theLastManageNode)):
            a1 = theLastDelList[count].root.x1
            a2 = theLastDelList[count].root.x2
            b1 = theLastDelList[count].root.y1
            b2 = theLastDelList[count].root.y2
            n1 = theLastManageNode[i].root.x1
            n2 = theLastManageNode[i].root.x2
            m1 = theLastManageNode[i].root.y1
            m2 = theLastManageNode[i].root.y2
            if a1 == n1 and a2 == n2 and b1 == m1 and b2 == m2:
                count1 = i
                break
        del theLastDelList[count]
        if minestDistacne < 20 and theLastManageNode[count1].findTheLastPoint().frame - x < 5:
            theLastManageNode[count1].updataList(useData[x][y][0], useData[x][y][1], useData[x][y][2], useData[x][y][3], x)
            nextFrame.append(theLastManageNode[count1])
        else:
            mylist = ListNode_Model.LinkList()
            mylist.updataList(useData[x][y][0], useData[x][y][1], useData[x][y][2], useData[x][y][3], x)
            nextFrame.append(mylist)
    if len(theLastDelList) != 0:
        for z in range(len(theLastDelList)):
            if theLastDelList[z].findTheLastPoint().frame - x < 5:
                nextFrame.append(theLastDelList[z])
    theHeadOfEveryManageList.insert(nextFrame, x)
read_Node = theHeadOfEveryManageList.root
with open("data.txt", 'w') as f:
    while read_Node:
        f.write("The %dth Frame\n" % read_Node.frame)
        for i in range(len(read_Node.node)):
            read_list_node = read_Node.node[i].root
            while read_list_node:
                f.write("%d %d %d %d ->" % (read_list_node.x1, read_list_node.y1, read_list_node.x2, read_list_node.y2))
                read_list_node = read_list_node.next
            f.write("the %dth list\n" % i)
        read_Node = read_Node.next
