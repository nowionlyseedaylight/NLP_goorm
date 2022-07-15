# range 함수의 경우, 숫자를 하나씩 생성하여 return
# 요소를 하나씩 생성해서 return하는 객체를 'generator'라고 함.

def my_range(stop):
    number = 0
    while number < stop:
        yield number    # function에 yield를 사용할 때 generator가 됨. yield하는 위치에서 값을 return. 
        number += 1
        
for i in my_range(5):
    print(i)
    
even_generator = (i*2 for i in range(100))    # 괄호로 generator comprehension 형태로 선언 가능
