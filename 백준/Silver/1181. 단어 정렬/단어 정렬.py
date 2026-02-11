def solution():
    n=int(input())
    words=[]
    for _ in range(n):
        words.append(input())
    words=set(words)
    answer=sorted(words,key=lambda x:(len(x),x))
    print("\n".join(answer))
    return
if __name__ == "__main__":
    solution()