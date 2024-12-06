def get_data():
    report_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split(" ")))
            report_list.append(report)
    return report_list


"""
first check if monotonic e.g strictly increasing or decreasing
then check if difference of subsequent elements are atleast 1 or atmost 3
if all above true: increment safe_count
"""

def monotonic(report:list) -> bool :
    diff = report[0]-report[1]
    if diff < 0:
        direction = -1
    elif diff > 0:
        direction = 1
    else:
        return False
    
    for x in range(1,len(report)-1):
        new_diff = report[x]- report[x+1]
        if new_diff < 0:
            new_direction = -1
        elif new_diff > 0:
            new_direction = 1
        else:
            return False
        if new_direction != direction:
            return False
    return True



def distance_1to3(report:list)-> bool:
    for x in range(len(report)-1):
        diff = abs(report[x]-report[x+1])
        if not(diff==1 or diff==2 or diff==3):
            return False
    return True

def get_safe_report_count(report_list):
    safe_count = 0
    for report in report_list:
        if monotonic(report) and distance_1to3(report):
            safe_count += 1
    return safe_count


if __name__=="__main__":
    report_list = get_data()

    # part 1
    print(get_safe_report_count(report_list))



