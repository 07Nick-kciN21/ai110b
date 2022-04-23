from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionScheduling import SolutionScheduling # 引入平方根解答類別

# 執行爬山演算法 (最多3萬代、失敗一千次就跳出)
hillClimbing(SolutionScheduling.init(), 10000, 1000)
# SolutionScheduling.init()