/* Byimaan
391. Perfect Rectangle

Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.


Example 1:

Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
Example 2:


Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
Example 3:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other

CMD  npx ts-node ./src/app/9-24/perfect-rectangle-391.ts 
*/

const positive = (int:number) => int < 0 ? -int : int

class Rectangle {
    public cors : number[];
    public height: number;
    public width: number
    constructor(corrdinates:number[]){
        this.cors = corrdinates
        this.height = positive(corrdinates[0] - corrdinates[2]);
        this.width = positive(corrdinates[1] - corrdinates[3])
    };
    
    area (){
        return this.height * this.width
    }
}


function perfectRectangle (rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]) : boolean {
    /**
     * ideas :-
     *      1) If perfectRectangle exists then sum of areas of all rectangles should be equal to the
*               area of perfect rectangle.
     *      2) If we managed ourselves to find the farthest edges possible (all 4 edges) 
     *          then we consider that as rectangle (does not matter whether it is truly a rectangle or not)
     *          then find area of that and then compare with sum of areas of all rectangles if it is exact same than it means it is a perfect rectangle
     *          else-if area of this assumed rectangle is smaller then  it means it is not a perfect rectangle and may have overlapped somewhere else 
*               else we found it greater then we again can say that it is not a perfect rectangle and it is possible that multiple rectangles has been formed rather than one.  
     */

    const sumOfAllRectangles = rectangles.reduce(
        (acc, rec) => acc + new Rectangle(rec).area(),0
    )

    /**
     * Farthest edges possible
     *  left-top
     *  left-bottom
     *  right-top
     *  right-bottom
     * 
     * rectangleToForm = [ y-bottom, x-left, y-top, x-right ]
     */

    /** find such a value of y and x such that they are farthest to the left side that means we need to focus on rectandgle[0] and rectange[1]   */
    const farthestLeftYX = rectangles.reduce(
        (acc, rec) => rec[1] < acc[1] ? rec.slice(0,2) : acc , [Infinity, Infinity]
    );

    /** find such a value of y and x such that they are farthest to right side */
    const fearthestRightYX = rectangles.reduce(
        (acc, rec) => rec[3] >= acc[1] ? rec.slice(2) : acc , [-Infinity, -Infinity]
    )

    const assumedRectangle = new Rectangle(farthestLeftYX.concat(fearthestRightYX))

    console.log(" ---- DEBUG ---- ")
    console.log("Assumed Triangle ", [farthestLeftYX, fearthestRightYX])
    console.log("Area of assumedRectangle ", assumedRectangle.area())
    console.log("SumofAllTriangles ", sumOfAllRectangles)

    return assumedRectangle.area() === sumOfAllRectangles
};

/** Remember we are accepting this format --> [y, x, y1, x1]  not [x, y, x1, y1]*/
console.log(perfectRectangle())