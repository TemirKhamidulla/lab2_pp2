N = int(input())
M = int(input())
x = int(input())
y = int(input())

min_distance_x = min(x, N - x)
min_distance_y = min(y, M - y)

min_distance_to_edge = min(min_distance_x, min_distance_y)

print(min_distance_to_edge)
