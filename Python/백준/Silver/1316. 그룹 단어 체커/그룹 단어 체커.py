def solution():
    n=int(input())
    answer=0

    for _ in range(n):
        check=True
        s=input()
        dic=[]
        for i in s:
            if not dic or i not in dic:
                dic.append(i)
            elif dic and i==dic[-1]:
                continue
            else:
                check=False
                break
        if check:
            answer+=1
    print(answer)
    
if __name__ == "__main__":
    solution()