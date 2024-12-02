import numpy as np

def check_number_range(list):
    
    isSafe = True
    
    for num in list:
        if abs(num) < 1:
            isSafe = False
        if abs(num) > 3:
            isSafe = False
    return isSafe


def check_for_unsafe_dif(list):
    difference = np.diff(list)
    res = check_number_range(difference)
    return res


def increase_decrease_bad_lvl_check(list):
    temp_num = None
    for num in list:
        if temp_num == None:
            temp_num = num

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
   
def checks(list):
    res_increase = check_if_always_increase(list)  
    res_decrease = check_if_always_decrease(list)  
        
    if ( res_increase or res_decrease):
        res = check_for_unsafe_dif(list)
        if res:
            return True
    return False
        
def bad_level_dampener(list):
    
    bad_level_saved = False
    
    for i in range(len(list)):
        list_copy = list.copy()
        list_copy.pop(i)
        res = checks(list_copy)
        if res:
            bad_level_saved = True
    return bad_level_saved
    
def check_for_change(lists):
    
    safe_counter = 0
    
    for list in lists:
        res = checks(list)
        if res:
            safe_counter += 1
        else:
            saved = bad_level_dampener(list)
            if saved:
                safe_counter += 1
                
                    
    print("safe: ",safe_counter)
        
lists = get_lists("input.txt")
check_for_change(lists)