input = open("../input.txt", "r")

list_1 = []
list_2 = []
while True:
    line = input.readline()
    if not line:
        break
    
    numbers_str = line.strip().split()
    num1 = int(numbers_str[0].strip())
    num2 = int(numbers_str[1].strip())
    list_1.append(num1)
    list_2.append(num2)

list_1.sort()
list_2.sort()
total_distance = 0
for i in range(len(list_1)):
    num1 = list_1[i]
    num2 = list_2[i]
    total_distance+= abs(num1-num2)
print(total_distance)






