def solution():
    n=int(input())
    have_nums=list(map(int,input().split(" ")))
    have_nums=set(have_nums)
    m=int(input())
    check_nums=list(map(int,input().split(" ")))
    for x in check_nums:
        if x in have_nums:
            print(1,end=" ")
        else:
            print(0,end=" ")
if __name__ == "__main__":
    solution()