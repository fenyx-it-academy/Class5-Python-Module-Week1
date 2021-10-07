### Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a and b > 1 and 10*10 :
        print (a+b)
        print (a-b)
        print (a*b)


### Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1): 
        print(i, end="")


### Finding the Percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores=sum(scores)/3
        student_marks[name] = scores
    query_name = input()    
    print('%.2f' % student_marks[query_name])


### Find the Runner-Up Score

highest = -101
second_Highest = -101
for num in arr:
    if num > second_Highest:
        if num > highest:
            second_Highest = highest
            highest = num
        elif num < highest: 
            second_Highest = num
print(second_Highest)
