// Byimaan

export const fallingFactorial = (n:number, k:number):number => {
    if (k<=0) return k<0 ? 0 : 1
    return n * fallingFactorial(n-1, k-1)
}

export const risingFactorial = (n:number, k:number):number => {
    if (k<=0) return k<0 ? 0 : 1
    return n * risingFactorial(n+1, k-1)
}

export const factorial = (n:number):number => {
    if (n<=0) return n<0 ? 0 : 1
    return n * factorial(n-1)
}

export const permutation = (n:number, k:number) => {
    if (k>n || [n, k].some(v => v<0)) return 0;
    return fallingFactorial(n, n-k)
}

export const combinations = (n:number, k:number) => {
    if (k > n || [n, k].some(v => v<0)) return 0;
    return permutation(n, k) / factorial(k)
}

export const computePermutation = (n:(number|string)[], k=0) => {
    const perms:(typeof n)[] = [];

    for(let i = k; i < n.length; i++){
        [n[k], n[i]] = [n[i], n[k]];
        perms.push(n.slice(0, k).concat(...n));
        
        const remainingPerms = computePermutation(n.slice(1), k+1);
        perms.push(...remainingPerms);
        [n[k], n[i]] = [n[i], n[k]];
    };

    return perms
}