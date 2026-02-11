from collections import deque
def solution():
    n=int(input())
    que=deque()
    out=[]
    for _ in range(n):
        cmd = input().split()
        if cmd[0]=="push":
            que.append(cmd[1])
        elif cmd[0]=="pop":
            out.append((que.popleft() if que else -1))
        elif cmd[0]=="size":
            out.append((len(que)))
        elif cmd[0]=="empty":
            out.append((0 if que else 1))
        elif cmd[0]=="front":
            out.append((que[0] if que else -1))
        elif cmd[0]=="back":
            out.append((que[-1] if que else -1))
    print("\n".join(map( str,out)))
    return
if __name__ == "__main__":
    solution()