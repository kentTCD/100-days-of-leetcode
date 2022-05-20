class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(set)
        for idx, num in enumerate(manager):
            if num > -1:
                graph[num].add(idx)
        
        # print(graph)
        stack, res = [(headID, 0)], 0
        while stack:
            temp = []
            for (idx, time) in stack:
                res = max(res, time)
                for subidx in graph[idx]:
                    temp += [(subidx, time + informTime[idx])]
            stack = temp
        return res