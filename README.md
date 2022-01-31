# Maze resolver when maze's map is unknown
App, which finds path from maze (maze's code is borrowed) by using DFS algorithm. Maze's map is unknown. Agent tries to find right path by trying new directions (priority is right and up, because it is most often place of gold). If agent visits the cell, it is icluded into visited array. If all cells around are used, agent goes back till it finds unvisited cell. All algorithm is in start_b file.

# Preview 
![maze picture](https://github.com/Jolka-JoJo/maze_resolver_maze_unknown/blob/main/maze.jpg)
