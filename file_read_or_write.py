t = 1
array = [[362, 127,282, 171],[121, 124, 181, 438],[211, 234, 569, 965],[233, 545, 546, 983],[274, 623, 893, 993],[0, 0, 0, 0],[2, 2, 2, 2],[111, 111, 111, 111],[000, 000, 000, 000],[723, 902, 126, 344]]
with open("data.txt", 'w') as f:
    for i in range(7):
        f.write("%d\n " %i)
        for j in range(len(array)):
            f.write("%d %d %d %d\n" %(array[j][0], array[j][1], array[j][2], array[j][3]))