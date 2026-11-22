# 8-Puzzle Search Solver

This project solves the classic 3x3 sliding-tile 8-puzzle using uninformed search algorithms (BFS, DFS, Uniform Cost Search) and informed search algorithms (Greedy Best-First Search and A* with Misplaced Tiles, Manhattan Distance, and Linear Conflict heuristics).

## Requirements
- Python 3.8 or higher
- matplotlib (optional, for generating the comparison graph)

## How to Run
1. Open a terminal in the project folder (or open the notebook in Google Colab).
2. Run the script:
   python puzzle.py
3. The program will:
   - Run a quick verification test on a 10-move shuffled puzzle.
   - Execute the 80-puzzle benchmark across shuffle depths of 5, 10, 15, and 20.
   - Print the summary tables for average nodes expanded and average solution length, along with a suboptimal Greedy vs. A* example.
   - Save the comparison chart as 'nodes_expanded_chart.png'.
