import re

def get_lines(input_file_dir):
    with open(input_file_dir ,"r") as file:
        text = file.readlines()
    return text

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
total = 0

lines = get_lines("input.txt")

for _ in lines:
    matches = re.findall(pattern, _)
    for x,y in matches:
        total += int(x)*int(y)

print(total)
