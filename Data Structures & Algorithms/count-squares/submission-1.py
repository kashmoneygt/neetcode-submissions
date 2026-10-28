class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.pts.keys()):
            
            # check if not diagonal or x,y are in same line as point 
            if abs(py - y) != abs(px - x) or x == px or y == py: 
                continue

            # num of occurences depends on dupes of (x, y), (x, py) and (px, y)
            # If one of them don't exist, defaultdict will return 0
            res += self.pts[(x, y)] * self.pts[(x, py)] * self.pts[(px, y)]
        
        return res
            

