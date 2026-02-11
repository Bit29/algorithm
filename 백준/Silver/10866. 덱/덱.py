from collections import deque
def solution():
    que=deque()
    n=int(input())
    out=[]
    for _ in range(n):
        cmd=input().split(" ")
        if cmd[0]=="push_front":
            que.appendleft(cmd[1])
        elif cmd[0]=="push_back":
            que.append(cmd[1])
        elif cmd[0]=="pop_front":
            out.append(que.popleft() if que else -1)
        elif cmd[0]=="pop_back":
            out.append(que.pop() if que else -1)
        elif cmd[0]=="size":
            out.append(len(que))
        elif cmd[0]=="empty":
            out.append(0 if que else 1)
        elif cmd[0]=="front":
            out.append(que[0] if que else -1)
        elif cmd[0]=="back":
            out.append(que[-1] if que else -1)
    print("\n".join([str(x) for x in out]))
    return
if __name__ == "__main__":
    solution()