class Solution:
   def shortestWay(self, source: str, target: str) -> int:
          for j in target:
              if j not in source:
                  return -1
          i, j = 0,0
          count = 1
          while i<len(target):
              if j == len(source):
                  j = 0
                  count+=1
              if target[i] == source[j]:
                  i+=1
              j+=1
          return count
