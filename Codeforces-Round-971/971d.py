'''
This problem took me quite a few attempts to solve in Python. I kept facing a TLE. I looked at the official solution for this problem and noticed it was very similar to my solution, but the official solution used a set of points instead of a list of points. Sets are implemented using hash tables, so the lookup operation for sets is faster, and that made all the difference here.
'''

def main():
    
    n = int(input())

    for i in range(0, n):

        n_points = int(input())

        points = []
        pointsx = []

        for j in range(0, n_points):
            temp = input()
            temp = temp.split()
            temp = [int(elem) for elem in temp]
            points.append((temp[0], temp[1]))
            pointsx.append(temp[0])

            # points.append(temp)
        count = 0
        count_dict = {}
        points = set(points)    

        for elem in points:
            count_dict[elem[0]] = count_dict.get(elem[0], 0) + 1
            if count_dict[elem[0]] ==  2:
                count += (n_points - 2)
            if (elem[0] - 1, elem[1]^1) in points and (elem[0] + 1, elem[1]^1) in points: 
                count += 1

        print(count)

main()





        
