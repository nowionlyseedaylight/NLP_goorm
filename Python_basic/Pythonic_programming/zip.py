# 2개 이상의 순환 가능한 객체를 앞에서부터 한번에 접근할 때 사용한다.

seq1 = ['What', 'is', 'zip']
seq2 = [True, False, True]
seq3 = [1, 2, 3, 4]           # 길이가 안 맞을 경우 남는 건 버린다.

for w1, w2, w2 in zip(seq1, seq2, seq3):    # 앞에서부터 하나씩 빼서 Tuple로 반환
  print(w1, w2, w3)
  
  
  
# Unpacking을 이용해서 2차원 리스트의 열 단위 접근도 가능하다.

array = [[1,2,3], [4,5,6], [7,8,9]]
for row in array:
  print(row)
  
for col in zip(*array):
  print(col)
