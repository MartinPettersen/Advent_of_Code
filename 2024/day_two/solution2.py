
def get_lists(file_name):
    lists = []
    with open(file_name, 'r') as file:
        for line in file:
            temp_line = line.strip().split(" ")
            #print(temp_line)
            lists.append(temp_line)
            #for list in temp_line:
    return lists
      
def increase_decrease_check(list):
    #print(list)
    increasing_list = list.copy()
    decreasing_list = list.copy()
    increasing_list.sort()
    decreasing_list.sort(reverse=True)
    
    if increasing_list == list or decreasing_list == list:
        #print("increasing-decreasingtest",increasing_list, decreasing_list, list)
        return True
    else:
        return False
             

def change_checker(list):
    
    previous_temp = None
    #print(list)
    for temp in list:
        if previous_temp == None:
            previous_temp = int(temp)
        else:
            dif = abs(previous_temp - int(temp))
            #print(list,dif)
            #print(previous_temp, temp)
            if dif < 1 or dif > 3:
            #    print(list,dif)
                
                return False
            previous_temp = int(temp)
            #print(dif)
    #print(list)
    return True
            
def safety_check(lists):
    #print(lists)
    safe_counter = 0
    for list in lists:
        #print(list)
        print(' '.join(list))
        result_increase_decrese = increase_decrease_check(list)
        #print(list, result_increase_decrese)
        if result_increase_decrese:
            change_result = change_checker(list)
            #print(list, result_increase_decrese, change_result)
            if change_result and result_increase_decrese:
                #print(list)
                safe_counter += 1
    return(safe_counter)
        
        
lists = get_lists("input.txt")
print(len(lists))
safe_counter = safety_check(lists)
print(safe_counter)