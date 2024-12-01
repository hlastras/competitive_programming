package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type move struct {
	dir   string
	steps int
}

func main() {
	instructions := make([]move, 0)
	maxLenght := 0
	maxHeight := 0
	x := 0
	y := 0
	initX := 0
	initY := 0
	for _, line := range readFile() {
		tmp := strings.Split(line, " ")
		n, _ := strconv.Atoi(tmp[1])
		instructions = append(instructions, move{tmp[0], n})
		switch tmp[0] {
		case "U":
			y -= n
		case "D":
			y += n
		case "L":
			x -= n
		case "R":
			x += n
		}
		if x < 0 {
			maxLenght += x * -1
			initX += x * -1
			x = 0
		}
		if y < 0 {
			maxHeight += y * -1
			initY += y * -1
			y = 0
		}
		if x > maxLenght {
			maxLenght = x
		}
		if y > maxHeight {
			maxHeight = y
		}
	}

	// Create a 2D array
	grid := make([][]int, 0)
	for i := 0; i < maxHeight+1; i++ {
		grid = append(grid, make([]int, maxLenght+1))
	}

	x = initX
	y = initY
	for i, move := range instructions {
		fmt.Println(i, move)
		switch move.dir {
		case "U":
			for i := 0; i < move.steps; i++ {
				y--
				grid[y][x]++
			}
		case "D":
			for i := 0; i < move.steps; i++ {
				y++
				grid[y][x]++
			}
		case "L":
			for i := 0; i < move.steps; i++ {
				x--
				grid[y][x]++
			}
		case "R":
			for i := 0; i < move.steps; i++ {
				x++
				grid[y][x]++
			}
		}
	}

	for _, row := range grid {
		fmt.Println(row)
	}

	fmt.Println()
	total := 0
	for i, row := range grid {
		enabled := false
		for j, col := range row {
			if col >= 1 {
				total++
				grid[i][j] = 1
				if enabled {
					enabled = false
				} else {
					enabled = true
				}
			} else if enabled {
				total++
				grid[i][j] = 1
			}
		}
	}
	for _, row := range grid {
		fmt.Println(row)
	}
	fmt.Println(total)

}

func readFile() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}
