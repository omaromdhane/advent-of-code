input = open("../input.txt", "r")


safe_reports = 0

while True:
    line = input.readline()
    if line == "":
        break
    levels = [int(x.strip()) for x in line.split(" ")]

    if(len(levels) < 2):
        safe_reports+=1

    if (sorted(levels) == levels or sorted(levels, reverse=True) == levels):
        total_ok_pairs = 0
        for level_index in range(len(levels)-1):
            diff = abs(levels[level_index]-levels[level_index+1])
            if not (diff >=1 and diff <=3):
                break
            else: 
                total_ok_pairs+=1
        if (total_ok_pairs == len(levels)-1):
            safe_reports+=1
                
print(safe_reports)