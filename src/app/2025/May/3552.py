'''
3552. Grid Teleportation Traversal
You are given a 2D character grid matrix of size m x n, represented as an array of strings, where matrix[i][j] represents the cell at the intersection of the ith row and jth column. Each cell is one of the following:

'.' representing an empty cell.
'#' representing an obstacle.
An uppercase letter ('A'-'Z') representing a teleportation portal.
You start at the top-left cell (0, 0), and your goal is to reach the bottom-right cell (m - 1, n - 1). You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle.

If you step on a cell containing a portal letter and you haven't used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used at most once during your journey.

Return the minimum number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return -1.

Example 1:

Input: matrix = ["A..",".A.","..."]

Output: 2

Explanation:

Before the first move, teleport from (0, 0) to (1, 1).
In the first move, move from (1, 1) to (1, 2).
In the second move, move from (1, 2) to (2, 2).
Example 2:

Input: matrix = [".#...",".#.#.",".#.#.","...#."]

Output: 13

Explanation:

Constraints:

1 <= m == matrix.length <= 103
1 <= n == matrix[i].length <= 103
matrix[i][j] is either '#', '.', or an uppercase English letter.
matrix[0][0] is not an obstacle.

python ./src/app/2025/May/3552.py
'''



import heapq, math
from itertools import count
from collections import deque

class Solution:
    def minMoves(self, matrix:list[str]):
        m, n = len(matrix), len(matrix[0])

        pq = []
        
        def get_cellid(r,c):
            return r*n + c
        def get_rc(cellid):
            return (math.floor(cellid/n), cellid%n)

        portals = [[] for _ in range(26)]
        used_portals = [False]*26
        
        def get_pid(ch):
            return ord(ch)-65
        for r in range(m):
            for c in range(n):
                ch = matrix[r][c]
                if ch not in ['.', '#']:
                    pid = get_pid(ch)
                    portals[pid].append(
                        get_cellid(r,c)
                    )
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n and matrix[r][c] != '#'

        if not is_valid(m-1, n-1):
            return -1
        
        counter = count()
        dists = [math.inf]*(m*n)
        dists[0]=0

        def push(dist, curr, state):
            if dists[curr] >= dist:
                heapq.heappush( #cnter as tie-breaker if priority found to be same
                    pq, (dist, next(counter), curr, state)
                )
        def pop():
            return heapq.heappop(pq)
        
        push(0, 0, 0)

        while len(pq):
            moves, _, curr, prev  = pop()

            if dists[curr] < moves:
                continue

            dists[curr]=moves

            if curr == m*n-1:
                return moves
            
            r, c = get_rc(curr)
            curr_char = matrix[r][c]
            teleport_possible = curr_char != '.' and not used_portals[get_pid(curr_char)]

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                nxt_curr = get_cellid(nr,nc)
                if is_valid(nr,nc) and nxt_curr != prev:
                    if not (teleport_possible and matrix[nr][nc] == curr_char):
                        push(
                            dist=moves+1,
                            curr=nxt_curr,
                            state=curr
                        )

            if teleport_possible:
                pid = get_pid(curr_char)
                used_portals[pid] = True
                for portal in portals[pid]:
                    if portal not in [prev, curr]:
                        push(
                            dist=moves,
                            curr=portal,
                            state=curr
                        )

        return -1

    def minMovesTopSubmission(self, matrix:list[str]):
        m, n, portals = len(matrix), len(matrix[0]), [[] for _ in range(26)]

        def is_alp(ch:str):
            return ch not in ['.', '#']
        def pid(ch:str):
            return ord(ch)-65
        
        for i in range(m):
            for j in range(n):
                if is_alp(matrix[i][j]): portals[pid(matrix[i][j])].append((i,j))
        
        dist = [[1e9]*n for _ in range(m)]
        dist[0][0], queue, used = 0, deque([(0,0)]), set()

        while len(queue):
            x, y = queue.popleft()
            if (x, y) == (m-1, n-1):
                return dist[x][y]
            ch = matrix[x][y]

            if is_alp(ch) and ch not in used:
                for a, b in portals[pid(ch)]:
                    if dist[a][b] > dist[x][y]:
                        dist[a][b] = dist[x][y]
                    queue.appendleft((a,b))
                used.add(ch)#teleportation used for this letter

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                a, b = x+dx, y+dy
                if (
                    0<=a<m
                    and 0<=b<n
                    and matrix[a][b] != '#'
                    and dist[a][b] > dist[x][y]+1
                ):
                    dist[a][b] = dist[x][y]+1
                    queue.append((a,b))

        return -1
    
if __name__ == '__main__':
    test_cases = [
        # [
        #     "A.AA.CBB.#",
        #     "..BA.CB.BB",
        #     "BCA.C...A.",
        #     ".CAA#.B..B",
        #     "BBA.CC.AAB",
        #     ".A...#BB.."
        # ],
        [".G#AF",".C#.F"],
        [
            ".....J...YR.....",
            ".....O.........B",
            "..T..M.WK..H....",
            ".E......E.#.....",
            ".H..............",
            "..W...FZ........",
            "......I...H.....",
            "....B...........",
            ".I..L...AH...F.Q",
            ".#...........DL.",
            "L...S..Y........",
            "........B.....B.",
            "UG.MG.D..A.....C",
            "..U.......V...Q.",
            "............ZCU.",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................",
            "................"
        ],
        ["....AN...U.....Z..G....QCI...","SV.....C...XRB...........J...",".......OX....Z..K........D...","M.#...K..Q......L..L..PD.....",".X.R.......ZNB.E..........C..","...............MBA.....XN....","U.K...X..............N.....R.","J.....DB.....BY....Q.......NQ",".Z...RV.NK..................H","....#...U#...JQU.......F....H","EW......Z.....P...R..D...A.C.","..EA.......BHZP.U..E..NU..P..","...I.N...X..........HD...T...",".P..W.....K..TH..L.W..G..E...","Z..R..V...#...D..Y...L...K...","...I.....T..........W......L.","..........W......W........UI.","..N.....C.B.....IC.K.........","......M....Z..............Z..","...EY.....E......J..U.Y.P....",".....XMN.W.........K.FR......","........N..J...W.A..#......B.","..T......G..F..OM.......V...K","D.N.X....O......H....GAV.V.H.","..B..I.EH.P..K...K..F..X.....","..BFJ.FF..O....G..J...O...#..","......B.A.J.QMR.Y.X...Q......",".E.......#.......OG.G.U....CF","HZ.I.V...EZ......E...........",".............Y......W........","QP.X.E..QJ..I......YN.Q.E.NL.","......Q.F.....G..W...UN...D..","......NU..B...N....R...G....D","...J..O..H..H.....H.....Q....","O......C..........DC.....T...",".E.ZQ.....N.....DW.....W.J..A",".T.......VV.I....FE...N....N.",".U......CE...G...M.........H.","T.SCT.......#.RP...W.........","......O..N..XWU#IH...S.L..Y..","..Q..I..I.A...CMV....RYV.F.J.","J........Q....H.....W........","....#.F............R...PI....",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................",".............................","............................."]
    ]
    sol = Solution()
    for test_case in test_cases:
        m, n = len(test_case), len(test_case[0])
        print(f'm={m} n={n} moves={sol.minMoves(test_case)}')
