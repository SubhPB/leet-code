// Byimaan

export function deepCopy<T=any, R=any>(arg: T): R{
    return JSON.parse(JSON.stringify(arg))
};

export function positiveIntToBinary(int:number){
    if (int <= 0){
        if (int<0) throw new Error(`Expected positive integer but got ${int}`);
        return '0'
    };
    let binary = ''
    while (int!==0){
        const remainder = int%2;
        int = Math.floor(int/2);
        binary = remainder.toString() + binary
    };
    return binary
}