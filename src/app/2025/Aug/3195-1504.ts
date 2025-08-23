/**
     * 3195. Find the Minimum Area to Cover All Ones I

    You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

    Return the minimum possible area of the rectangle.
    Example 1:

    Input: grid = [[0,1,0],[1,0,1]]

    Output: 6
    Explanation:

    The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

    Example 2:
    Input: grid = [[1,0],[0,0]]
    Output: 1

    Explanation:
    The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.


    1504. Count Submatrices With All Ones

    Given an m x n binary matrix mat, return the number of submatrices that have all ones.

    Example 1:


    Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
    Output: 13
    Explanation: 
    There are 6 rectangles of side 1x1.
    There are 2 rectangles of side 1x2.
    There are 3 rectangles of side 2x1.
    There is 1 rectangle of side 2x2. 
    There is 1 rectangle of side 3x1.
    Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
    Example 2:


    Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
    Output: 24
    Explanation: 
    There are 8 rectangles of side 1x1.
    There are 5 rectangles of side 1x2.
    There are 2 rectangles of side 1x3. 
    There are 4 rectangles of side 2x1.
    There are 2 rectangles of side 2x2. 
    There are 2 rectangles of side 3x1. 
    There is 1 rectangle of side 3x2. 
    Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 */

(
    ()=>{
        function minimumArea(grid: number[][]): number { //3195
            const m = grid.length, n = grid[0].length;
            const R = Array(m).fill(0), C = Array(n).fill(0);
            for(let x=0; x<m; x++){
                for(let y=0; y<n; y++){
                    R[x] |= grid[x][y];
                    C[y] |= grid[x][y]
                }
            };
            let l=0, r=m-1;
            while (!R[l]) l+=1;
            while (!R[r]) r-=1;
            let x = r-l+1;
            l=0; r=n-1;
            while(!C[l]) l+=1;
            while(!C[r]) r-=1;
            let y = r-l+1
            return x*y;
        };

        //1504
        function numSubmat(mat: number[][]): number {
            let res = 0;
            const m = mat.length, n = mat[0].length;
            for(let i=0; i<m; i++){
                const state = Array(n).fill(1);
                for(let j=i; j<m; j++){
                    let csc = 0;
                    for(let x=0; x<n; x++){
                        state[x] &= mat[j][x];
                        csc = (csc+state[x])*state[x]
                        res += csc;
                    }
                };
            };
            return res  
        };
    
    }
)