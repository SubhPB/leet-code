/**
 * 2070. Most Beautiful Item for Each Query

You are given a 2D integer array items where items[i] = [price, beauty] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
Example 2:

Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty. 

CMD :- npx ts-node ./src/app/11-24/leetcode-2070.ts
 */

type ItemsAndQueries = [
  number[][],
  number[]
]

const ItemsAndQueries: ItemsAndQueries[] = [
  [
    [[1,2],[3,2],[2,4],[5,6],[3,5]],
    [1,2,3,4,5,6]
  ],
  [
    [[1,2],[1,2],[1,3],[1,4]],
    [1]
  ]
]

const maximumBeauty = (items: number[][], queries: number[]) => {
    const maxBeauty: number[] = []
    queries.forEach(
        (query) => {
            let beauty = 0;
            const itemsWithLessOrEqualPriceAsQuery = items.filter(([price]) => price <= query);
            if (!!itemsWithLessOrEqualPriceAsQuery.length){
                beauty = Math.max(...itemsWithLessOrEqualPriceAsQuery.map(([_price,beauty]) => beauty))
            };
            maxBeauty.push(beauty)
        }
    );
    return maxBeauty
};


const optimizeSolution = (items:number[][], queries: number[]) => {
  items.sort(
    (a, b) => a[0] - b[0] //ascending order according price value
  );
  
  const queriesWithIndex = queries.map(
    (query, index) => [query, index]
  );

  queriesWithIndex.sort( 
    (a, b) => a[0] - b[0]
  );
  
  let j = 0,
  maxBeauty = 0,
  result = Array.from(items, () => 0);

  for(let [query, index] of queriesWithIndex){
    
    while (j < items.length && items[j][0] <= query){
      maxBeauty = Math.max(
        maxBeauty, items[j][1]
      );
      j += 1;
    };

    result[index] = maxBeauty

  };

  return result
}

for(let [items, queries] of ItemsAndQueries){
  console.log(optimizeSolution(items, queries))
}


