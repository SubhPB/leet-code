// Byimaan

export function deepCopy<T=any, R=any>(arg: T): R{
    return JSON.parse(JSON.stringify(arg))
}