def solution():
    n=int(input())
    stack=[]
    for _ in range(n):
        x=int(input())
        if stack and x==0:
            stack.pop()
        else:
            stack.append(x)
    print(sum(stack))
    
    return

if __name__ == "__main__":
    solution()