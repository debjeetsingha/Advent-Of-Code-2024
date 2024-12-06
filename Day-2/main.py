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

def is_safe(report: list) -> bool:
    if monotonic(report) and distance_1to3(report):
        return True
    return False


def safe_with_damper(report: list) -> bool:
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

def get_safe_report_count(report_list):
    safe_count = 0
    for report in report_list:
        if is_safe(report):
            safe_count += 1
    return safe_count

def safe_count_with_damper(report_list):
    safe_count = 0
    for report in report_list:
        if safe_with_damper(report):
            safe_count += 1
    return safe_count


if __name__=="__main__":
    report_list = get_data()

    # part 1
    print(get_safe_report_count(report_list))

    # part2
    print(safe_count_with_damper(report_list))



