# 함수의 이름 없이 빠르게 만들어 쓸 수 있는 익명 함수
# 수학에서의 람다 대수에서 유래함.

def add(a,b):
    return a+b
  
add = lambda a, b: a+b          # a+b를 반환하는 익명함수 (lambda function)


# 공식적으로는 사용을 권장하지는 않으나, 많이 쓰이는 편임.
# 여러 줄로 표현하는 건 불가능함.
