# grade = [2, 2, 5, 3, 3, 5, 4, 5, 4, 3, 2, 3, 5, 4, 4, 5]

def split_list(grade):
    suma = 0
    for i in grade:
        suma += i
    
    avg = suma/len(grade)
    return avg

print(split_list([2, 2, 5, 3, 3, 5, 4, 5, 4, 3, 2, 3, 5, 4, 4, 5]))