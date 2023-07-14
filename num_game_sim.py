'''
テスト用プログラム
関数gen_Aの中にアルゴリズムを記載(今は仮で先生が言っていた方法)
gen_Aの中身を変えたらいろいろ試せる
関数gen_QでQを生成(このプログラムでは1~20000でランダム)
下部のnum_simの値を変えるとシミュレーション回数を変更可能
'''

import random

max_num = 20000

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
  
  print(ans, end = ',')

  return ans


def gen_Q() -> int:
  """
  Qを生成する関数
  """
  Q = random.randint(1, 20000)
  return Q

def game(count_game: int):

  score = 0  # スコアを記録
  count_safe = 0  # (検証用)セーフ数を記録
  count_correct = 0  # (検証用)正解数を記録
  count_out = 0  # (検証用)アウト数を記録

  Q = gen_Q() # 最初のQを生成
  A = gen_A(0, 0) # 最初のAを生成

  for i in range(100000):
    if A > Q:  # アウトの場合
      score -= (A - Q) * 200
      count_out += 1
      Q = gen_Q()
      A = gen_A(2, A)

    elif A == Q:  # 正解の場合
      score += A
      count_correct += 1
      Q = gen_Q()
      A = gen_A(1, A)

    elif A < Q:  # セーフの場合
      score += A
      count_safe += 1
      A = gen_A(0, A)

  # 下のコメントアウトを解除すればセーフ数，正解数，アウト数を出力可能
  '''
  print(f'{count_game=}')
  print(f'{count_correct=},{count_safe=},{count_out=}')
  print(f'{score=}')
  '''
  
  return score

sum_score = 0
num_sim = 100 # ゲームのシミュレーション回数
for i in range(num_sim):
  sum_score += game(i)
ave_score = sum_score / num_sim

print(f'{ave_score=}')

        