#Python Program to Sort the List According to the Second Element in Sublist

data = [[4,7],[1,3],[9,2],[6,5]]

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j][1] > data[j + 1][1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j+1] = temp

print("List sorted by second element:",data)