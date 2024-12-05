import re
from GetData import get_file_data

class Safety_manual_printer():
    def __init__(self, file_name):
        data = get_file_data(file_name)
        separation_index = data.index('')
        self.page_ordering_rules = data[:separation_index]
        self.pages_to_produce = data[separation_index:]
        #print(self.page_ordering_rules)
        #print(self.pages_to_produce)

    def check_with_rules(self, page, tempPage):
        for rule in self.page_ordering_rules:
            split_rules =  rule.split('|')
            #print(rule)
            #print(split_rules)
            #print(page,"|", tempPage)
            if (tempPage == split_rules[0] and  page == split_rules[1]):
                #print("hit")
                return False
        return True


    def check_if_valid(self, page, pages):
        #print("pages: ",pages)
        isValid = True
        for i in range(len(pages)):
            tempPage = pages[i]
            #print("page|tempPage ", page,tempPage)
            res = self.check_with_rules(page,tempPage)      
            if res == False:
                isValid = False
            #else:
                #res =self.check_if_valid(tempPage, pages[i:])
                #print(tempPage, pages[i:])
                #if res == False:
                    #isValid = False
        
        return isValid
        
    def check_order(self):
        
        sum = 0
        
        for print_order in self.pages_to_produce:
            pages = re.split(",", print_order)
            inOrder= True
            
            for i in range(len(pages)):
                res = self.check_if_valid(pages[i],pages[i:])
                if res == False:
                    inOrder = False
            #print("pages", pages)
            if inOrder:
                #print(print_order)
                midle_number = pages[int(len(pages)/2)]
                #print(midle_number)
                if midle_number != "":
                    sum += int(midle_number)
        print("sum: ",sum)
safety_manual_printer = Safety_manual_printer("input.txt")
safety_manual_printer.check_order()