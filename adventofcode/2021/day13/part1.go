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
	var maxX, maxY int
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		var x, y int
		fmt.Sscanf(line, "%d,%d", &x, &y)
		if x > maxX {
			maxX = x
		}
		if y > maxY {
			maxY = y
		}

		points = append(points, &[2]int{x, y})
	}

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
		} else {
			for _, point := range points {
				if point[1] >= value {
					point[1] = value - (point[1] - value)
				}
			}
		}
		break
	}

	seen := make(map[int]bool)
	for _, point := range points {
		val := point[0]*maxX + point[1]
		seen[val] = true
	}
	fmt.Println(len(seen))
}
