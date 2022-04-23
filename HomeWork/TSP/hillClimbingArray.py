from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionArray2 import SolutionArray # 引入平方根解答類別

# 執行爬山演算法 (最多十萬代、失敗一千次就跳出)。
hillClimbing(SolutionArray([0,1,2,3]), 100, 1000)
