def main():
 
    n = int(input())
 
    for i in range (0, n):
        temp = input()
        temp = temp.split()
        l = int(temp[0])
        r = int(temp[1])
 
        print(r-l)
 
main()
