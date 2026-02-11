def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    for x in nums:
        print(x)
if __name__ == "__main__":
    solution()