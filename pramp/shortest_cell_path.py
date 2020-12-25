import copy


def get_shortest_cell_path(grid, sr, sc, tr, tc):
    if (sr == tr) and (sc == tc):
        return 0
    else:
        distance = 0
        queue = []
        queue.append((grid, sr, sc, tr, tc, distance))
        while queue:
            distance += 1
            grid, sr, sc, tr, tc, shortest_distance = queue.pop()
            if (sr == tr) and (sc == tc):
                return shortest_distance
            for (mr, mc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ar = sr + mr
                ac = sc + mc
                if (
                    (0 <= ar < len(grid))
                    and (0 <= ac < len(grid[0]))
                    and (grid[ar][ac] == 1)
                ):
                    grid_next = copy.deepcopy(grid)
                    grid_next[sr][sc] = 0
                    queue.append((grid_next, ar, ac, tr, tc, distance))
        return -1


def shortestCellPath(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    return get_shortest_cell_path(grid, sr, sc, tr, tc)


''' Depth-first Search (if any path which is not shortest is ok)
import copy


def p(grid, sr, sc, tr, tc, sp):
    if (sr == tr) and (sc == tc):
        return sp
    else:
        for (mr, mc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ar = sr + mr
            ac = sc + mc
            if (
                (0 <= ar < len(grid))
                and (0 <= ac < len(grid[0]))
                and (grid[ar][ac] == 1)
            ):
                grid_copy = copy.deepcopy(grid)
                grid_copy[sr][sc] = 0
                sp = p(grid_copy, ar, ac, tr, tc, sp + 1)
                if sp >= 0:
                    return sp
        return -1


def shortestCellPath(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
    return p(grid, sr, sc, tr, tc, 0)
'''