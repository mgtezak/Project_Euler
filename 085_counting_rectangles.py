'''By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen 
rectangles. Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.'''

# def get_n_of_contained_rectangles(width, height):
#     n_rectangles = 0
#     for w in range(width):
#         for h in range(height):
#             n_rectangles += (width-w) * (height-h)
#     return n_rectangles

def get_n_of_contained_rectangles(width, height):
    return width * (width - 1) * height * (height - 1) // 4

min_diff = float('inf')
area = None
for w in range(10, 100):
    for h in range(w, 100):
        diff = abs(2_000_000 - get_n_of_contained_rectangles(w, h))
        if diff < min_diff:
            min_diff = diff
            area = w * h

print(min_diff)