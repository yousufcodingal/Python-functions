numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x,y:x+y, numbers1,numbers2)
print(list(result))

def square(n): 
    return n*n
squares=list(map(square,numbers2))
print(squares)