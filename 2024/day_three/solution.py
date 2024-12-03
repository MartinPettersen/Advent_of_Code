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

def main(file_name):
    data_list = get_file_data(file_name)
    #print(data_list)
    combined_list = concat_list(data_list)
    mul_list = regex_data(combined_list)
    calculate(mul_list)
    
main("input.txt")