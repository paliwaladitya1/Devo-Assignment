import sys

def NumberCheck(flag):
    while flag == True:

        lst = []
        # number of elemetns as input
        try:
            n = int(input("Enter list of numbers : "))
        except:
            print("not a valid number")
            continue;
        for i in range(0, n):
            try:
                element = int(input())
            except:
                print("not a valid number")
                continue;
            lst.append(element) # adding the element
        print(lst)
        for num in lst:
            print("numbers",num)
            num_check = 1
            sum_of_div = 0
            while num_check < num:
                if(num % num_check == 0):
                    sum_of_div = sum_of_div + num_check
                num_check = num_check + 1 
            if sum_of_div == num:
                print(num ,"it's a perfect number")
            elif sum_of_div < num:
                print(num ,"it's a defective number ")
            else:
                print(num ,"it's a abundent number")
        flag = get_bool("Do you wish to continue checking numbers (yes/no)")

def get_bool(prompt):
    while True:
        try:
           return {"yes":True,"no":False}[input(prompt).lower()]
        except KeyError:
           print("Invalid input please enter yes or no!")

if __name__ == "__main__":
    NumberCheck(True)

