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

	var points []*[2]int
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		var x, y int
		fmt.Sscanf(line, "%d,%d", &x, &y)
		points = append(points, &[2]int{x, y})
	}

	var maxX, maxY int
	for scanner.Scan() {
		line := scanner.Text()
		var axis string
		var value int

		fmt.Sscanf(line, "fold along %s", &axis)
		fmt.Sscanf(axis[2:], "%d", &value)
		axis = axis[:1]

		if axis == "x" {
			for _, point := range points {
				if point[0] >= value {
					point[0] = value - (point[0] - value)
				}
			}
			if maxX == 0 || value < maxX {
				maxX = value
			}
		} else {
			for _, point := range points {
				if point[1] >= value {
					point[1] = value - (point[1] - value)
				}
			}
			if maxY == 0 || value < maxY {
				maxY = value
			}
		}
	}

	var matrix [][]string
	for i := 0; i < maxY; i++ {
		var line []string
		for j := 0; j < maxX; j++ {
			line = append(line, ".")
		}
		matrix = append(matrix, line)
	}

	for _, point := range points {
		matrix[point[1]][point[0]] = "#"
	}

	for _, line := range matrix {
		fmt.Println(line)
	}
}
