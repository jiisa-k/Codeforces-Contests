def sol(legs):
    if legs % 4 == 0:
        return legs//4
    else:
        return legs//4 + 1

def main():
    
    n = int(input()) # number of test cases
    for i in range(n):
        legs = int(input()) # accept input
        print(sol(legs))

main()        