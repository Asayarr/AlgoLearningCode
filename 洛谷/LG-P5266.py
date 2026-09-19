Q = int(input())
students = {}

for _ in range(Q):
    task = list(map(str, input().split()))
    if task[0] == "1":
        students[task[1]] = int(task[2])
        print("OK")
    elif task[0] == "2":
        print(students.get(task[1],"Not found"))
    elif task[0] == "3":
        if task[1] not in students:
            print("Not found")
        else:
            del students[task[1]]
            print("Deleted successfully")
    else:
        print(len(students))
