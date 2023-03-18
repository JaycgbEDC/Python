#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """ others """
        if start > destination:
            start, destination = destination, start
        overall = sum(distance)
        d1 = sum(distance[start:destination])
        return min(d1, overall - d1)
    
    def func1(self, distance: List[int], start: int, destination: int) -> int:
        """ bymyself """
        start, destination = min(start, destination), max(start,destination)
        return min(sum(distance[start:destination]), sum(distance[0:start] + distance[destination:]))

# @lc code=end

