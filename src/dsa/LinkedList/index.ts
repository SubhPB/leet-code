/**
 * Byimaan
 */

export class LinkedNode<T> {
    public next : LinkedNode<T> | null = null
    constructor(public value:T){
        this.value = value
    };
}

export class LinkedList<T=number> {
    head : LinkedNode<T> | null = null;

    insert(value: T){
        const newNode = new LinkedNode<T>(value);
        if (this.head === null){
            this.head = newNode
        } else {
            this.insertNode(this.head, newNode)
        }
    };

    private insertNode (head: LinkedNode<T>, newNode: LinkedNode<T>){
        if (head.next === null){
            head.next = newNode
        } else {
            this.insertNode(head.next, newNode)
        }
    };

    delete(value: T){
        if (this.head){
            const node = new LinkedNode(value)
            if (this.head.value === node.value){
                this.head = this.head.next
            } else {
                this.deleteNode(this.head, node)
            }
        }
    }

    traverse(){
        const arr:T[] = []
        let currNode = this.head;
        while (currNode !== null){
            arr.push(currNode.value);
            currNode = currNode.next
        };
        return arr
    }

    private deleteNode(currNode: LinkedNode<T>, node: LinkedNode<T>){
        if (!currNode){
            return
        };

        if (currNode.next && currNode.next.value === node.value){
            currNode.next = currNode.next.next
            return
        };
        if (currNode.next) {
            this.deleteNode(currNode.next, node)
        }
    }
}