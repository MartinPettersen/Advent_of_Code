#list_one = [3,4,2,1,3,3]
#list_two = [4,3,5,3,9,3]


def get_lists(list_name):
    list_one = []
    list_two = []
    with open(list_name, 'r') as file:
        for line in file:
            temp_line = line.strip().split("   ")
            list_one.append(temp_line[0])
            list_two.append(temp_line[1]) 
             
    return list_one, list_two
    
def dif_checker(num1, num2):
    return abs(int(num1) - int(num2))

def list_difference(list_a, list_b):
    list_a.sort()
    list_b.sort()
    list_dif= []
    for i in range(len(list_a)):
        list_dif.append(dif_checker(list_a[i],list_b[i]))
    
    return (sum(list_dif))

def similarity_checker(list_a, list_b):
    similarity_score = 0

    for i in range(len(list_a)):
        counter = list_b.count(list_a[i])
        similarity_score += counter * int(list_a[i])
        #print(counter,list_a[i], counter * int(list_a[i]))
    
    return similarity_score

list_one, list_two = get_lists('input.txt')
print(list_difference(list_one, list_two))
print(similarity_checker(list_one, list_two))