
# Parse input text to form two list
def get_data():
    left_list = []
    right_list = []

    with open('input.txt', 'r') as file:
        for eachline in file:
            line = eachline.split(" ")
            left_list.append(int(line[0]))
            right_list.append(int(line[3].rstrip("\n")))

    return left_list, right_list

# Find total distance after sorting
def find_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for x,y in zip(left_list,right_list):
        total_distance += abs(x-y)

    return total_distance


def similarity_score(left_list, right_list):
    score = 0
    for x in left_list:
        count = 0
        for y in right_list:
            if x == y:
                count += 1
        score += (x * count)
    return score

if __name__ == '__main__':

    left, right = get_data()

    # part 1
    print(find_distance(left, right))

    # part 2
    print(similarity_score(left, right))