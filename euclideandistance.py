import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (2, 3)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafeleri hesaplama ve saklama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("Minimum Öklid Mesafesi:", min_distance)
