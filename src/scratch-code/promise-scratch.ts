/**
 * Byimaan
 * 
 * Key points about promises
 * 1. States = i) pending ii) fulfilled iii) rejected
 * 2. Executors = resolve & reject
 * 3. Then & catch = would need to implement these methods
 * 4. Callbacks = onFulfilled and onRejected are stored until the promise is not settled
 */

type ResolveFn<T> = (value: T) => void;
type RejectFn = (reason: any) => void;

type Executor<T> = (resolve: ResolveFn<T>, reject: RejectFn) => void;

type ThenCallback<T, R> = (value: T) => R | Bromise<R> ;
type CatchCallback = (reason: any) => any;

enum BromiseState {
    Pending="pending",
    Fulfilled="fulfilled",
    Rejected="rejected"
}

// Let's gave it name of `Bromise` which starts with letter as of my nickname

class Bromise<T> {
    #state:BromiseState = BromiseState.Pending;
    #value: T | null = null;
    #reason: any = null;
    #onFulfilledCallbacks: ResolveFn<T>[] = [];
    #onRejectedCallbacks: RejectFn[] = [];

    constructor(executor: Executor<T>) {
        /** 
         * Remember it would like this from outside:
         * new Bromise<any>( (resolve, reject) => {
         *      const data = something
         *      resolve(data)
         * } ).then( ...{} ).catch( ...{} )
        */

        try {
            executor(
                this.#resolve.bind(this),
                this.#reject.bind(this)
            )
        } catch (error) {
            this.#reject(error)
        }
    }

    #resolve(value: T){
        if (this.#state !== BromiseState.Pending) return;

        // To achieve actual Promise like execution:
        // We want Bromise to go in micro-task queue but must have higher priority than ordinary task queue jobs e.g WebAPI methods.
        queueMicrotask(
            () => {
                this.#state = BromiseState.Fulfilled;
                this.#value = value;
        
                this.#onFulfilledCallbacks.forEach(
                    callbackFn => callbackFn(value)
                );
            }
        );

    }

    #reject(reason: any){
        if (this.#state !== BromiseState.Pending) return;

        queueMicrotask(
            () => {
                this.#state = BromiseState.Rejected;
                this.#reason = reason;
        
                this.#onRejectedCallbacks.forEach(
                    callbackFn => callbackFn(reason)
                )
            }
        )

    }

    then<R>(onFulfilled?: ThenCallback<T, R>, onRejected?: CatchCallback): Bromise<R>{

        return new Bromise<R>(
            (resolve, reject) => {
                if (this.#state === BromiseState.Fulfilled && onFulfilled){
                    //isFulfilled
                    try {
                        const result = onFulfilled(this.#value as T);
                        resolve(result as R);
                    } catch (error) {
                        reject(error)
                    };

                } else if (this.#state === BromiseState.Rejected && onRejected){
                    //isRejected
                    try{
                        const result = onRejected(this.#reason);
                        resolve(result as R)
                    } catch (error) {
                        reject(error)
                    };

                } else {

                    this.#onFulfilledCallbacks.push(
                        value => {
                            if (onFulfilled){
                                
                                try {
                                    const result = onFulfilled(value);
                                    resolve(result as R)
                                } catch (error) {
                                    reject(error)
                                }

                            }
                        }
                    );

                    this.#onRejectedCallbacks.push(
                        reason => {
                            if (onRejected){

                                try {
                                    const result = onRejected(reason);
                                    resolve(result as R)
                                } catch (error) {
                                    reject(error)
                                }

                            }
                        }
                    )
                }
            }
        )
    }

    catch<R>(onRejected: CatchCallback){
        return this.then<R>(
            undefined,
            onRejected
        )
    }
}