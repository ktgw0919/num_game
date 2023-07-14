'''
テスト用プログラム
関数gen_Aの中にアルゴリズムを記載(今は仮で先生が言っていた方法)
gen_Aの中身を変えたらいろいろ試せる
関数gen_QでQを生成(このプログラムでは1~20000でランダム)
下部のnum_simの値を変えるとシミュレーション回数を変更可能
'''

import random

max_num = 20000

def calc_optimum_A(min_possible_answer: int):
  """
  最適なAを計算する関数
  min_possible_answer (int): 正解候補の最小値(前回の解答した値 + 1)
  """
  max_val = None
  A = min_possible_answer
  for i in range(min_possible_answer, max_num):
    val = ((200002 - i - min_possible_answer) - 100 * (i - min_possible_answer + 1) * (i - min_possible_answer)) / (20001 - min_possible_answer)
    if max_val is None or val > A:
      max_val = val
      A = i
    else:
      break

  return A


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
    ans = calc_optimum_A(1)

  elif correct == 0:
    '''
    前の回答がセーフの場合
    '''
    ans = calc_optimum_A(pre_ans + 1)

  elif correct == 1:
    '''
    前の回答が正解の場合
    '''
    ans = calc_optimum_A(1)

  elif correct == 2:
    '''
    前の回答がアウトの場合
    '''
    ans = calc_optimum_A(1)
  
  
  """
  if pre_ans == 0: 
    '''
    最初の回答
    '''
    ans = calc_optimum_A(1)

  elif correct == 0:
    '''
    前の回答がセーフの場合
    '''
    ans = calc_optimum_A(pre_ans + 1)

  elif correct == 1:
    '''
    前の回答が正解の場合
    '''
    ans = calc_optimum_A(1)

  elif correct == 2:
    '''
    前の回答がアウトの場合
    '''
    ans = calc_optimum_A(1)
  """
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
num_sim = 1
for i in range(num_sim):
  sum_score += game(i)
ave_score = sum_score / num_sim
print(f'{ave_score=}')

        
