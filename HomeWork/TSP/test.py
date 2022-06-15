# class NestedIterator(object):

#     def __init__(self, nestedList):
#         self.list = nestedList
      
#     def next(self):
#         ans = []
#       # 如果是list
#         if(type(self.list[0]) == list):
#           # 進入搜尋
#             ans += self.searchlist(self.list[0])
#         elif(type(self.list[0]) == int):
#             ans.append(self.list[0])
#         self.list = self.list[1:]
#         return ans
#         """
#         :rtype: int
#         """
    
#     def searchlist(self, List):
#         rel = []
#         i=0
#         for i in range(len(List)):
#             if(type(List[i]) == list):
#                 rel += self.searchlist(List[i])
#             else:
#                 rel.append(List[i])
#         return rel

#     def hasNext(self):
#         if(len(self.list) > 0):
#             return True
#         """
#         :rtype: bool
#         """

# nestedList = NestedIterator([[1,3],2,[5,[4,2,1]],7])
# res = []
# while nestedList.hasNext():
#     res += nestedList.next()
# print(res)
# a = [1,2,3,[4,5,6],1,[2,2,[5,4,3]]]

# def searchlist(List):
#   rel = []
#   i=0
#   for i in range(len(List)):
#     if(type(List[i]) == list):
#       rel += searchlist(List[i])
#     else:
#       rel.append(List[i])
#   return rel

# print(searchlist(a))

class NestedIterator(object):
    def __init__(self, nestedList):
        def flatten(l):
            temp = []
            for i in l:
                if i.isInteger():
                    temp.append(i.getInteger())
                else:
                    temp.extend(flatten(i.getList()))
            return temp
        # arr是處理過的list
        self.arr = flatten(nestedList)
        # n為總長度
        self.n = len(self.arr)
        self.index = -1
        
    def next(self):
        # index加1
        self.index += 1
        return self.arr[self.i]

    def hasNext(self):
        # 如果index小於總長度-1
        return self.index < self.n - 1