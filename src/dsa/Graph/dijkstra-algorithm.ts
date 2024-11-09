/**
 * Byimaan
 * 
 *  ************** Dijkstra algorithm **************
 * You are given with a graph made up of nodes (directed or undirected) has some weights and your goal is to go from one node to another with minimum weight cost.
 *  
 * Solution Approach: 
 * 1. Create a table representing the distance b/w one node to another. Nodes that are not been traversed yet then their distance could be assumed as `Infinity`.
 * 2. Let's say your starting node is `a` then update the table regarding its neighbors, after then among its neighbors select a neighbor who has minimum weight value in total. The total minimum weight means distance from node `a` to the selected new node.
 * 3. Repeat the step 2 until you do not reach teh destination node and keep updating the table on the way.
 * 4. The moment you select a node, consider following:
 *      - you can't reselect a node.
 *      - That node should have traversed from node `a`
 * 5. Even if you have found a path from `a` to destination but it is still not sure that it is most minimum. To ensure that the answer is minimum it is important that you go through all the nodes and traverse them all before declaring an answer.
 * 
 * 
 * What is the time complexity of this algorithm:  O(n^2)  W n = # of nodes.
 * 
 * Edge-cases: 
 * 1. This algorithm may give unexpected results if distance b/w one to another node is in negative. So make sure all the distances should be positive. 
 * 
 * ^This information may not be understandable to complete beginner. but it would be helpful to implement dijkstra algorithm in code for who is already familiar with this topic theoretically
 * 
 * 
 * CMD: npx ts-node ./src/dsa/Graph/dijkstra-algorithm.ts
 */

 type Graph = { [node: string]: { [neighbor: string]: number } };

// Example graph data structure
const graph: Graph = {
  A: { B: 4, C: 2 } as const,
  B: { A: 4, C: 1, D: 5 } as const,
  C: { A: 2, B: 1, D: 8, E: 10 } as const,
  D: { B: 5, C: 8, E: 2, Z: 6 } as const,
  E: { C: 10, D: 2, Z: 3 } as const,
  Z: { D: 6, E: 3 } as const
} as const;

const Dijkstra = (G: typeof graph, startingPoint: keyof typeof graph, endPoint: keyof typeof graph) => {

    const table : {[key: keyof typeof  graph]: number} = Object.fromEntries(
        Object.keys(G).map( ([key, _]) => [             
            key, // object key
            Infinity // object value        
        ])
    );

    
    // It takes 0 distance to go from `a` to `a`
    table[startingPoint] = 0;
    
    Object.entries(graph[startingPoint]).forEach(
        ([neighborNode, distance]) => {
            table[neighborNode] = distance
        }
    );
    

    const traversedNodes: (keyof typeof graph)[] = [startingPoint]

    const traverse = () => {
        // Base case
        if (traversedNodes.length === Object.keys(graph).length){
            return
        };

        const nodesNotTraversedAndLinkedToPrev = Object.entries(table).filter(
            ([node, _]) => !traversedNodes.includes(node)
        );

        const nodeWithLeastCost = nodesNotTraversedAndLinkedToPrev.find(
             ([ _, distance]) =>  distance === Math.min(...nodesNotTraversedAndLinkedToPrev.map(([n, d]) => d))
            );


        if (nodeWithLeastCost){

            const [node, distance] = nodeWithLeastCost;
            Object.entries(graph[node]).forEach(
                ([neighborNode, neighborDist]) => {
                    //Relaxation
                    if (table[neighborNode] > distance + neighborDist){
                        table[neighborNode] = distance + neighborDist;

                    };
                }
            );
            // This node is considered to be traversed now
            traversedNodes.push(node);

            // Let's traverse others too
            traverse()
        }
    };

    traverse();

    console.log("\r\n DEBUG ", table);
    return table[endPoint];

};

console.log(Dijkstra(graph, "A", "Z"))