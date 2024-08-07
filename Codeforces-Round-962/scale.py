def sol(n, matrix, k):

    ri = 0 # to track row index
    ci = 0 # to track column index 

    scaled = []

    while ri < n:
        row = []
        row.append(matrix[ri][ci])
        ci += k

        while (ci < n):
            row.append(matrix[ri][ci])
            ci += k
        ri += k
        ci = 0

        scaled.append(row)

    return scaled


def main():
    
    n = int(input()) # number of test cases

    for i in range(n):
        
        inp = input()
        inp = inp.split()
        n = int(inp[0])
        k = int(inp[1])

        matrix = []

        # accept matrix as input
        for i in range(n):
            inp = input()
            row = []
            for digit in inp:
                row.append(int(digit))
            matrix.append(row)

 
        scaled = sol(n, matrix, k)
        # scaled = matrix

        for i in range(len(scaled)):
            for j in range(len(scaled[i])):
                print(scaled[i][j], end = "")
            print()

main() 