class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append(point[0]**2 + point[1]**2)
        zip_list = zip(distances, points)
        distances, points = zip(*sorted(zip_list))

        return points[:k]

    ### Other Solution Someone Made
        points.sort(key=lambda x:x[0]**2+x[1]**2)
        return points[:k]