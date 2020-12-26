import math


def drawLine(x1, y1, x2, y2):
    print("Drew a line from ({}, {}) to ({}, {})".format(x1, y1, x2, y2))


def drawHTree(x, y, length, depth):
    h = length / 2
    drawLine(x - h, y, x + h, y)
    drawLine(x - h, y - h, x - h, y + h)
    drawLine(x + h, y - h, x + h, y + h)
    length /= math.sqrt(2)
    depth -= 1
    if depth > 0:
        for (dx, dy) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            drawHTree(x + dx, y + dy, length, depth)


"""
time complexity: O(4^depth)
space complexity: O(depth)
"""

if __name__ == "__main__":
    drawHTree(x=0, y=0, length=1, depth=2)
