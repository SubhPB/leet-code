// Byimaan

// CMD = npx ts-node ./src/dsa/BT.ts

type NodeTS = BTNode | null;

class BTNode {
    
    constructor(public value: number, public left: NodeTS = null, public right: NodeTS = null){
        this.value = value;
        this.left = left;
        this.right = right;
    }

    isLeaf(){
        return !this.left && !this.right
    };

}

class BinaryTree {
    constructor(public root: BTNode){
        this.root = root
    };

    postOrder(){
        
        const stack = [this.root];
        const postO : BTNode[] = []

        while (stack.length !== 0){
            const node = stack[stack.length - 1];
            if (node.isLeaf()){
                postO.push(stack.pop() as BTNode)
            }
            if (node.left){
                console.log(node.left !== postO[postO.length - 1])
                node.left !== postO[postO.length - 1] && stack.push(node.left);
            };
            if (node.right) {
                node.right !== postO[postO.length - 1] && stack.push(node.right)
            };
            console.log(postO);
        };
        return postO
    }
};

type CreateTS = {
    val : number,
    left: number | NodeTS,
    right: number | NodeTS,
}

const create = ({val, left=null, right=null}: CreateTS) => {
    if (typeof left === 'number'){
        left = new BTNode(left)
    };
    if (typeof right === 'number'){
        right = new BTNode(right)
    };
    return new BTNode(val, left, right)
};

const main = () => {
    const root = new BTNode(1);
    const tree = new BinaryTree(root);

    tree.root.left = create({val: 2, left: 4, right: create({val: 5, left: 8, right: 9})});
    tree.root.right = create({val: 3, left: 6, right: 7});
    console.log(tree.postOrder())
};

main()