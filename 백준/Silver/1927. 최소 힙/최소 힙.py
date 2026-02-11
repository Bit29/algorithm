import heapq
import sys
def solution():
    input=sys.stdin.readline
    stack=[]
    n=int(input())
    
    for _ in range(n):
        x=int(input())
        if x!=0:
            heapq.heappush(stack,x)
        elif stack and x==0:
            print(heapq.heappop(stack))
        else:
            print(0)
    return

if __name__ == "__main__":
    solution()