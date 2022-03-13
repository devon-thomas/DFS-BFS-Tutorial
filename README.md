# DFS-BFS-Tutorial
Simple introduction to DFS-BFS using collections.deque

Some ideas:
For DFS, we use a stack. The attached code implements a recursive method of DFS where the stack is implicit. The element stack is represented by the function stack of the 'for' loop. 
The idea of DFS is to follow along a direction until there are no more neighbors. 
In psuedo-code: 
Start at a node
Mark that node as visited
Visit its' neighbors, and if they haven't been visited, visit their neighbors. 

When implemented in a for loop:
for neighbors in graph[node]

We look at one node, then look at its first neighbor, then the first neighbors neighbor and in this way we follow a single direction until the end. When the end is reached, we move to the next neighbor of the calling loop.

BFS is a bit easier to understand in this code because it is not implemented recursively (impossible from what I understand). 
BFS uses a queue and FIFO type of data structure. 
Starting at a node, we mark it as current and add its' neighbors to the queue. By adding its' neighbors to the queue, we are determining an order of traversal that is layer by layer. 

