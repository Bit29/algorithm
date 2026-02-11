def solution():
    n=int(input())
    A = list(map(int, input().split()))
    m=int(input())
    arr= list(map(int,input().split()))
    A.sort()

    for num in arr:
        isExist=False
        start,end=0,n-1
        while start<=end:
            mid=(start+end)//2
            if num==A[mid]:
                isExist=True
                print(1)
                break
            elif num>A[mid]:
                start=mid+1
            else:
                end=mid-1
        if not isExist:
            print(0)
if __name__=="__main__":
    solution()