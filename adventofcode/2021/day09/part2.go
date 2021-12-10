package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func isValid(heightmap [][]int8, x, y int) bool {
	return x >= 0 && x < len(heightmap) && y >= 0 && y < len(heightmap[0])
}

func explore(heightmap [][]int8, x, y int) int {
	queue := [][2]int{{x, y}}
	total := 1
	seen := make(map[int]bool)
	l := len(heightmap[0])
	seen[x*l+y] = true

	for len(queue) > 0 {
		point := queue[0]

		if isValid(heightmap, point[0]-1, point[1]) && !seen[(point[0]-1)*l+point[1]] && heightmap[point[0]-1][point[1]] != 9 {
			queue = append(queue, [2]int{point[0] - 1, point[1]})
			seen[(point[0]-1)*l+point[1]] = true
			total++
		}

		if isValid(heightmap, point[0]+1, point[1]) && !seen[(point[0]+1)*l+point[1]] && heightmap[point[0]+1][point[1]] != 9 {
			queue = append(queue, [2]int{point[0] + 1, point[1]})
			seen[(point[0]+1)*l+point[1]] = true
			total++
		}

		if isValid(heightmap, point[0], point[1]-1) && !seen[(point[0])*l+point[1]-1] && heightmap[point[0]][point[1]-1] != 9 {
			queue = append(queue, [2]int{point[0], point[1] - 1})
			seen[(point[0])*l+point[1]-1] = true
			total++
		}

		if isValid(heightmap, point[0], point[1]+1) && !seen[(point[0])*l+point[1]+1] && heightmap[point[0]][point[1]+1] != 9 {
			queue = append(queue, [2]int{point[0], point[1] + 1})
			seen[(point[0])*l+point[1]+1] = true
			total++
		}

		queue = queue[1:]
	}
	return total
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var heightmap [][]int8
	var values []int
	for scanner.Scan() {
		var line []int8
		for _, n := range scanner.Text() {
			line = append(line, int8(n-48))
		}
		heightmap = append(heightmap, line)
	}

	for i := 0; i < len(heightmap); i++ {
		for j := 0; j < len(heightmap[0]); j++ {
			is_min := true
			// up
			if i-1 >= 0 {
				if heightmap[i-1][j] <= heightmap[i][j] {
					is_min = false
				}
			}

			// right
			if j+1 < len(heightmap[0]) {
				if heightmap[i][j+1] <= heightmap[i][j] {
					is_min = false
				}
			}

			// down
			if i+1 < len(heightmap) {
				if heightmap[i+1][j] <= heightmap[i][j] {
					is_min = false
				}
			}

			// left
			if j-1 >= 0 {
				if heightmap[i][j-1] <= heightmap[i][j] {
					is_min = false
				}
			}

			if is_min {
				values = append(values, explore(heightmap, i, j))
			}
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(values)))
	fmt.Println(values[0] * values[1] * values[2])
}
