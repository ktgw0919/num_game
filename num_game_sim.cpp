/*
作りかけ．時間があるときに作る．
*/

#include <iostream>
#include <random>

using namespace std;

random_device rd;
mt19937 rd_eng(rd());
uniform_int_distribution<> random(1, 20000);

/* Qを生成する関数 */
int gen_Q(void)
{
  int Q = random(rd_eng);
}
