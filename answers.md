# CMPS 2200 Recitation 10## Answers

**Name:**_______Killian Daly___
**Name:**_______Simon Yung_____


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
Work will be $O(n * m)$, as we are essentially combination of nodes and edges, so in the worst case scenario where every node is connected to every other node, n * m is worst case.

- **4)**
Only once. If the reachable fails, the graph is not properly connected.

- **5)**
Work will be $O(n * m)$ + constant length of the graph, as reachable is called once.

- **7)**
Adjacency matrices allow for references between past nodes to be made in constant time. With this in mind, the edges can be processed in constant time, resulting in $O(n)$