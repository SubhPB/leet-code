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
    }
)