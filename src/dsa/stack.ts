// Byimaan

interface StackTS<T> {
    pop(): T | null;
    push(value: T): void;
    updateHeight(): void;
    top(): T | null
}

export class Stack<T=number> implements StackTS<T> {
    private stack : T[];
    public height : number;

    constructor(){
        this.stack = []
        this.height = 0
    };

    updateHeight(){
        this.height = this.stack.length
    }

    pop(): T | null {
        const poppedValue = this.stack.pop();
        if (poppedValue === undefined){
            return null
        };
        this.updateHeight();
        return poppedValue
    };

    push(value: T): void {
        this.stack.push(value);
        this.updateHeight()
    };

    top(){
        return this.stack[this.height-1]
    }
};