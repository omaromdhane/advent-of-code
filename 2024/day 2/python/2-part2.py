

def check_is_safe(levels):
    safe_reports = 0
    if(len(levels) < 2):
        safe_reports+=1
    if (sorted(levels) == levels or sorted(levels, reverse=True) == levels):
        total_ok_pairs = 0
        for i in range(len(levels)-1):
            diff = abs(levels[i]-levels[i+1])
            if not (diff >=1 and diff <=3):
                break
            else: 
                total_ok_pairs+=1
        if (total_ok_pairs == len(levels)-1):
            safe_reports+=1
    if(safe_reports==1):
        return True
    else:
        return False

def solution(input):
    safe_reports = 0
    while True:
        line = input.readline()
        if line == "":
            break
        levels = [int(x.strip()) for x in line.split(" ")]

        if(len(levels) < 2):
            safe_reports+=1
            continue
        
        if(check_is_safe(levels)):
            safe_reports+=1
            continue

        for level_index in range(len(levels)):
            levels_copy = levels.copy()
            levels_copy.pop(level_index)
            if(check_is_safe(levels_copy)):
                safe_reports+=1
                break
    return safe_reports

input = open("../input.txt", "r")
print(solution(input))