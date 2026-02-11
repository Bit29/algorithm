def solution():
    n = int(input())
    stack = []

    for _ in range(n):
        x = input()
        if "push" in x:
            stack.append(int(x.split()[1]))
        elif x == "pop":
            print(stack.pop() if stack else -1)
        elif x == "size":
            print(len(stack))
        elif x == "empty":
            print(0 if stack else 1)
        elif x == "top":
            print(stack[-1] if stack else -1)

solution()