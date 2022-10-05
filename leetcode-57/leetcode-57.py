class Solution:
    def merge(self, intervals):
        """
        :param intervals: List[List[int]]
        :return: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged

intervals = [[1,3],[8,10],[2,6],[15,18]]
print(Solution().merge(intervals))