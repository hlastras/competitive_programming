package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var heightmap [][]int8
	total := 0
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
				total += int(heightmap[i][j]) + 1
			}
		}
	}
	fmt.Println(total)
}
