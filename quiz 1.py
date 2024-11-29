def print_triangle(n):
    lines = (2*n)-1
    for i in range(lines):
        if(i < n):
            for j in range(i+1):
                print("*", end='')
                #print(i, j)
        else:
            for j in range(lines-i):
                print("*", end='')
                #print(i, j)
        print("")

def print_mixed_types(a, b, c):
    add = a+b
    print(add, c, end=" ")

def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False

def validate_even(numbers):
    result = map(is_even, numbers)
    return list(result)

def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j*i, end=' ')
        print("")

def  swap_elements(lst, n):
    size = len(lst)
    x = lst[n]
    y = lst[size-n-1]
    #print(size, x, y)
    lst[n] = y
    lst[size-n-1] = x
    return lst

def classify_grade(score):
    if(score >= 90):
        print("Excellent")
    elif(score >= 80 and score <= 89):
        print("Very Good")
    elif(score >= 70 and score <= 79):
        print("Good")
    elif(score >= 60 and score <= 69):
        print("Average")
    elif(score >= 50 and score <= 59):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    #print_triangle(3)
    #print_mixed_types(42, 3.14, "world")
    #print(validate_even([-2, -1, 0, 1, 2]))
    #multiplication_table(4)
    #print(swap_elements([1, 2, 3, 4, 5], 1))
    #print(swap_elements(['a', 'b', 'c', 'd'], 0))
    #classify_grade(58)
    L = [12, 34, 21, 4, 6, 9, 42]
    lst = []
    lst2 = [x for x in L if x > 10]
    for x in L:
        if x > 10:
            lst.append(x)
    print(lst)
    print([x for x in lst2])
    worked = [300, 880]
    hours = [x / 60 for x in worked]
    print(hours)