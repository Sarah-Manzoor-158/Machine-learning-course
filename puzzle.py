{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNiK7pF5aVjqTNvE+B5+3d1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sarah-Manzoor-158/Machine-learning-course/blob/main/puzzle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NAjDzO6uS4tR",
        "outputId": "0d270f25-9cdd-4707-f33d-820cc74b0762"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "README.md ban gayi hai!\n"
          ]
        }
      ],
      "source": [
        "readme_text = \"\"\"# 8-Puzzle Search Solver\n",
        "\n",
        "This project solves the classic 3x3 sliding-tile 8-puzzle using uninformed search algorithms (BFS, DFS, Uniform Cost Search) and informed search algorithms (Greedy Best-First Search and A* with Misplaced Tiles, Manhattan Distance, and Linear Conflict heuristics).\n",
        "\n",
        "## Requirements\n",
        "- Python 3.8 or higher\n",
        "- matplotlib (optional, for generating the comparison graph)\n",
        "\n",
        "## How to Run\n",
        "1. Open a terminal in the project folder (or open the notebook in Google Colab).\n",
        "2. Run the script:\n",
        "   python puzzle.py\n",
        "3. The program will:\n",
        "   - Run a quick verification test on a 10-move shuffled puzzle.\n",
        "   - Execute the 80-puzzle benchmark across shuffle depths of 5, 10, 15, and 20.\n",
        "   - Print the summary tables for average nodes expanded and average solution length, along with a suboptimal Greedy vs. A* example.\n",
        "   - Save the comparison chart as 'nodes_expanded_chart.png'.\n",
        "\"\"\"\n",
        "\n",
        "with open(\"README.md\", \"w\") as f:\n",
        "    f.write(readme_text)\n",
        "\n",
        "print(\"README.md is ready!\")"
      ]
    }
  ]
}