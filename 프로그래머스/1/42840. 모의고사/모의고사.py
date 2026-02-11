def solution(answers):
    student1=[1, 2, 3, 4, 5]
    student2=[2, 1, 2, 3, 2, 4, 2, 5]
    student3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num1=[0,1]
    num2=[0,2]
    num3=[0,3]
    for i in range(len(answers)):
        if student1[i%5]==answers[i]:
            num1[0]+=1
        if student2[i%8]==answers[i]:
            num2[0]+=1
        if student3[i%10]==answers[i]:
            num3[0]+=1
        
    answer=[num1,num2,num3]
    answer.sort(reverse=True)
    return sorted([e[1] for i,e in enumerate(answer) if i==0 or answer[0][0]==e[0]])