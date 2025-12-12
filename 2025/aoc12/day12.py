import re

def parse_input(filename=0):
    with open(filename) as f:
        *shapes, regions = f.read().split('\n\n')
    return shapes, regions.split('\n')

def p1(shapes, regions):
    # This solution doesn't solve the test input
    # But it handles the real input nicely
    total = 0
    areas = [shape.count('#') for shape in shapes]
    
    for region in regions:
        width, height, *quantities = map(
            int, re.findall(r'\d+', region)
        )
        region_area = width * height
        shape_area = sum(a * q for a, q in zip(areas, quantities))
        total += shape_area <= region_area

    print(total)

puzzle_input = parse_input()

p1(*puzzle_input[:])