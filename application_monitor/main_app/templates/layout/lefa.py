def solution(A,B,C,D):
    emp = []
    emp.append(A)
    emp.append(B)
    emp.append(C)
    emp.append(D)

    hour = []
    minuets = []
    n = 1
    print(emp)

    while n != 24:
        n = n +1
        a =int(f'{emp[n-1]}{emp[n]}')
        if a <=23:
            hour.append(a)
            minuets.append(a)
        elif a>23 and n <=59:
            minuets.append(a)
    print(f"Hours {hour}")
    print(f"Minuets {minuets}")
solution(1,2,6,3)