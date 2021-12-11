package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func isValid(grid [][]int, x, y int) bool {
	return x >= 0 && x < len(grid) && y >= 0 && y < len(grid[0])
}

func adyacents(grid [][]int, x, y int) [][2]int {
	var a [][2]int
	for i := x - 1; i <= x+1; i++ {
		for j := y - 1; j <= y+1; j++ {
			if (i != x || j != y) && isValid(grid, i, j) {
				a = append(a, [2]int{i, j})
			}
		}
	}
	return a
}

func p(grid [][]int) {
	for _, r := range grid {
		fmt.Println(r)
	}
	fmt.Println()
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var grid [][]int
	for scanner.Scan() {
		var line []int
		for _, n := range scanner.Text() {
			line = append(line, int(n-48))
		}
		grid = append(grid, line)
	}

	for n := 1; n < 100000; n++ {

		var full [][2]int
		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[0]); j++ {
				grid[i][j]++
				if grid[i][j] == 10 {
					full = append(full, [2]int{i, j})
				}
			}
		}

		for len(full) > 0 {
			for _, a := range adyacents(grid, full[0][0], full[0][1]) {
				grid[a[0]][a[1]]++
				if grid[a[0]][a[1]] == 10 {
					full = append(full, [2]int{a[0], a[1]})
				}
			}
			full = full[1:]
		}

		all := true
		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[0]); j++ {
				if grid[i][j] > 9 {
					grid[i][j] = 0
				} else {
					all = false
				}
			}
		}

		if all {
			fmt.Println(n)
			break
		}
	}
}
