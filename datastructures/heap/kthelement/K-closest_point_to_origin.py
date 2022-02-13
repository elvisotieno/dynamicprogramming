import heapq


def k_closest_to_origin(points: list, k: int) -> list:
    for point in points:
        distance = point[0]**2 +point[1]**2
        point.insert(0,distance)
    heapq.heapify(points)
    result = heapq.nsmallest(k,points)
    return result[0][1:]

points=[[1,3],[-2,2]]
k=1
print(k_closest_to_origin(points,k))
