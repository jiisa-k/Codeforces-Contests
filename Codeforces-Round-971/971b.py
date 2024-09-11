
def main():
 
    n = int(input())
 
    for i in range (0, n):
 
        rows  = int(input())
        cols = []
        for j in range(0, rows):
            temp = input()
            cols.append(temp)
 
        cols = cols[ : : -1]
 
        out = []
 
        for col in cols:
            for sym in range(0, 4):
                if col[sym] == "#":
                    out.append(sym + 1)
 
        for elem in out:
            print(elem, end = " ")
 
        print()


main()
