import random

def gen_A(correct: int, pre_ans: int) -> int:
  """
  correct (int): 前の回答の正誤．0:セーフ，1:正解，2:アウト
  pre_ans (int): 前の回答
  """
  ans = 0

  if pre_ans == 0: 
    '''
    最初の回答
    '''
    ans = 1

  elif correct == 0:
    '''
    前の回答がセーフの場合
    '''
    ans = pre_ans + 1

  elif correct == 1:
    '''
    前の回答が正解の場合
    '''
    ans = 1

  elif correct == 2:
    '''
    前の回答がアウトの場合
    '''
    ans = 1

  return ans


def gen_Q() -> int:
  """
  Qを生成する関数
  """
  # Q = random.randint(1, 20000)

  while True:
    Q = input()
    if Q.isdigit():
        number = int(Q)
        if 1 <= number <= 20000:
            break
        else:
            print("1~20000の整数を入力")
    else:
        print("1~20000の整数を入力")

  return Q

def game():

  score = 0  # スコアを記録

  Q = gen_Q() # 最初のQを生成
  A = gen_A(0, 0) # 最初のAを生成

  for i in range(100000):
    if A > Q:  # アウトの場合
      score -= (A - Q) * 200
      Q = gen_Q()
      A = gen_A(2, A)

    elif A == Q:  # 正解の場合
      score += A
      Q = gen_Q()
      A = gen_A(1, A)

    elif A < Q:  # セーフの場合
      score += A
      A = gen_A(0, A)
    

  print(f'{score=}')
  return score

game()

        