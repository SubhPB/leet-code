/**
 * Byimaan
 */

export class BSTNodeError extends Error {
    constructor(message: string, name = "Invalid BST node") {
      super(message);
      this.name = name; 
    }
}

class BSTNode<T=number> {
    constructor (public val: T, public left: BSTNode | null = null, public right: BSTNode | null = null){
        this.val = val;
        if (left && left >= val){
            throw new BSTNodeError(`[Invalid BST Left Node | ${left} >= ${val} ] Left node was expected to be less than ${val} but found ${left}`)
        };
        this.left = left;
        if (right && right <= val){
            throw new BSTNodeError(`[Invalid BST Right Node | ${right} <= ${val} ] Right node was expected to be lmore than ${val} but found ${left}`)
        };
        this.right = right
    };
    isValidBSTNode(){
        const val = this.val, left = this.left, right = this.right;
        try {
            if (right && right <= val){
                throw new BSTNodeError(`[Invalid BST Right Node | ${right} <= ${val} ] Right node was expected to be lmore than ${val} but found ${left}`)
            };
            if (left && left >= val){
                throw new BSTNodeError(`[Invalid BST Left Node | ${left} >= ${val} ] Left node was expected to be less than ${val} but found ${left}`)
            };
        } catch {
            return false
        }

        return true
    }
};

export class BSTTree {
    public root: BSTNode | null = null; 

    /** such as arr = [5,1,4,null,null,3,6] */
    constructor(arr:(number|null)[]){
        this.root = BSTTree.init(arr)
    };

    /** So its task is to init the BSt node out of array */
    private static init(arr: (number|null)[]){
        
        /** 
         * According to pattern we are following in array:
         * Let's index = 0 where 0 <= index < arr.length
         * So this means we have node whose value is arr[index]
         *  # whose left node's index in the arr equals 2*index + 1 means holding the value of arr[2*index+1]
         *  # So in the same way we can figure out the index of right node which is 2*(index+1)
         * 
         * Let's start the work by initializing the BSt node as a root representing tree
         * 
         */
        const rec = (index:number) => {

            if (index >= arr.length || arr[index] === null){
                return null
            };

            const leftIndex = 2 * index + 1;
            const rightindex = leftIndex + 1; /** OR 2*(index+1) */

            const currNode = new BSTNode(arr[index]);
            currNode.left = rec(leftIndex);
            currNode.right = rec(rightindex);

            return currNode
        };
        const root = rec(0);

        return root
    };

    insert(val: number){
        const newNode = new BSTNode(val);
        if (!this.root){
            this.root = newNode
        } else {
            this.insertNode(this.root, newNode)
        }
    };

    private insertNode(root:BSTNode, newNode: BSTNode){
        if (newNode.val < root.val){
            root.left ? this.insertNode(root.left, newNode) : (root.left = newNode);
        } else {
            root.right ? this.insertNode(root.right, newNode) : root.right = newNode
        }
    }
}