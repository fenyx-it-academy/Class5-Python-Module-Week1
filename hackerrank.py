# <!-- HackerRank -->
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b,a-b,a*b,sep='\n')
# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
# Print Function
if __name__ == '__main__':
    n = int(input())
    print(*[i for i in range(1,n+1)],sep="")
# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(*[(sum(student_marks[i])/len(student_marks[i])) for i in student_marks if i==query_name]))