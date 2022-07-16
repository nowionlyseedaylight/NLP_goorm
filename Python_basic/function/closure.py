num = 10
def print_closure_factory(number):  # Closure Funtion Factory
    def print_closure():       # Closure 함수 / Factory의 변수(number) 사용 --> closure마다 고유한 변수
        print(number)
        
    return print_closure    # 생성된 closure 반환

print_5 = print_closure_factory(5)
print_10 = print_closure_factory(10)

number += 10
print_5()
print_10()
