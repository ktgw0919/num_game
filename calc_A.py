def find_optimal_A(n):
  P = 20000 - n + 1  # Qの候補の個数
  E = [0] * 20001  # 各Aについての期待値を保存するリスト
  
  for A in range(n, 20001):
    for Q in range(n, 20001):
      if Q < A:
        E[A] -= (A - Q) * 200 / P
      else:
        E[A] += A / P
    
    # 上に凸の2次関数なので減少し始めたら計算を終了
    if E[A] < E[A - 1]:
      break
    

  # 最大期待値を持つAを求める
  optimal_A = E.index(max(E))

  return optimal_A

def light_find_optimal_A(n):
  return n

# n = int(input())
# A = find_optimal_A(n+1)
# print(f'{A=}')


optimal_A = 1
with open('optimal_A.csv', 'w') as f:
  while optimal_A < 20000:
    optimal_A = find_optimal_A(optimal_A + 1)
    print(f"The optimal value for A is {optimal_A}.")
    if optimal_A == 20000:
      f.write('%s' % str(optimal_A))
    else:
      f.write('%s,' % str(optimal_A))


