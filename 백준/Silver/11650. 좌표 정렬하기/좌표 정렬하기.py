def solution():
    n = int(input())
    points = []

    for _ in range(n):
        points.append(tuple(map(int, input().split())))

    answer = sorted(points)
    for x,y in answer:
        print(str(x) + " " + str(y) )

if __name__ == "__main__":
    solution()