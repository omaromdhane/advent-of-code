input = open("../input.txt", "r")

similarity_score = 0

left_values = []
right_values = []
right_occurrence_map = {}

while True:
    line = input.readline()
    if line == "":
        break
    
    left_value, right_value = (int(x.strip()) for x in line.split("  "))
    left_values.append(left_value)
    right_values.append(right_value)

    if right_value in right_occurrence_map:
        right_occurrence_map[right_value] += 1
    else:
        right_occurrence_map[right_value] = 1

for left_value in left_values:
    if left_value in right_occurrence_map:
        similarity_score += left_value * right_occurrence_map[left_value]

print(similarity_score)