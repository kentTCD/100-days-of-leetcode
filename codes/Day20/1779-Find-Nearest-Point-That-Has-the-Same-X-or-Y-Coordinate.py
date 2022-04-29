class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest_distance = None
        sd_index = -1

        for i in range(len(points)):
            if points[i][0] != x and points[i][1] != y: continue
            distance = abs(x - points[i][0]) + abs(y - points[i][1])
            if smallest_distance is None: smallest_distance, sd_index = distance, i
            if distance < smallest_distance: smallest_distance, sd_index = distance, i
        return sd_index