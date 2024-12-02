import numpy as np

def check_number_range(number, list):
    
    for num in list:
        if abs(num) < 1:
            return False
        if abs(num) > 3:
            return False
    return True

def check_for_unsafe_dif(list):
    difference = np.diff(list)
    res = check_number_range(3, difference)
    return res
    #print(difference)

def check_if_always_decrease(list):
    list_copy = list.copy()
    list_copy.sort(reverse=True)
    if list == list_copy:
        return True
    else:
        return False

def check_if_always_increase(list):
    list_copy = list.copy()
    list_copy.sort()
    if list == list_copy:
        return True
    else:
        return False

def get_lists(file_name):
    lists = []
    with open(file_name, 'r') as file:
        for line in file:
            temp_line = line.strip().split(" ")
            res = map(int, temp_line)
            lists.append(list(res))
    return lists
    
def check_for_change(lists):
    
    safe_counter = 0
    
    for list in lists:
        res_increase = check_if_always_increase(list)  
        #print(res_increase)
        res_decrease = check_if_always_decrease(list)  
        #print(res_decrease)
        
        if ( res_increase or res_decrease):
            res = check_for_unsafe_dif(list)
            if res:
                safe_counter += 1
    print("safe: ",safe_counter)
        
lists = get_lists("input.txt")
#print(lists)
check_for_change(lists)