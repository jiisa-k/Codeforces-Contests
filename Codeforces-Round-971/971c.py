
import math
 
def main():
 
    n = int(input())
 
    for i in range(0, n):
 
        temp = input()
        temp = temp.split()
        temp = [int(elem) for elem in temp]
 
        x = temp[0]
        y = temp [1]
        k = temp[2]
 
        x_step = math.ceil(x/k)
        y_step = math.ceil(y/k)
 
        if x_step > y_step:
            print(int(x_step*2-1))
 
        else:
            print(int(y_step*2))
 
main()
