import re
from getData import get_file_data



def concat_list(list):
    combined = ''.join(list)
    return combined

def regex_data(data):
    mul_list = re.findall("mul\(\d{1,3},\d{1,3}\)",data)    
    return mul_list
    
def calculate(list):
    sum = 0
    for mul in list:
        numbers = re.findall("\d{1,3}",mul)
        sum += (int(numbers[0]) * int(numbers[1]))
    print("sum is ", sum)

def get_start_part(data):
    parts = re.split("don't\(\)",data, 1)
    return parts

def get_remaining_parts(data):
    parts = re.findall("do\(\).+?don't\(\)|do\(\).*",data)
    return parts

def main(file_name):
    data_list = get_file_data(file_name)
    combined_list = concat_list(data_list)
    start_parts = get_start_part(combined_list)
    remaining_parts = get_remaining_parts(start_parts[1])
    remaining_parts.append(start_parts[0])
    combined_parts_list = concat_list(remaining_parts)
    
    mul_list = regex_data(combined_parts_list)
    calculate(mul_list)
    
main("input.txt")