1) BFS will give us an optimal solution, but will use extra space
2) DFS is not guarenteed to be optimal, but uses less space. We don't want
   to use this here


We will use BFS from each of the actors towards Kevin Bacon, since 
as in the spec sheet, we know that he connects all actors.


Furthermore, we will have 2 frontiers, one for each actor searching 
towards Kevin Bacon.

Something we can do to quit early is:
1) check if the node we are adding to the frontier of actor 1 is in the explored
   set of actor 2
2) check if the node we are adding to the frontier of actor 2 is in the explored
   set of actor 1

Base case:
combine number of steps for getting from actor 1 to Kevin Bacon, and from 
actor 2 to Kevin Bacon
