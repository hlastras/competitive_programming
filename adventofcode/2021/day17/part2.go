package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func intersect(velX, velY, startX, endX, startY, endY int) bool {
	var x, y int
	for x <= endX && y >= endY {
		if x >= startX && x <= endX && y <= startY && y >= endY {
			return true
		}
		y += velY
		velY--
		x += velX
		if velX > 0 {
			velX--
		}
	}
	return false
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var minX, maxX, minY, maxY int
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "target area: x=%d..%d, y=%d..%d", &minX, &maxX, &minY, &maxY)

	maxVelY := -minY - 1
	minVelY := minY
	minVelX := 0
	maxVelX := maxX
	acc := 0
	for acc < minX {
		minVelX++
		acc += minVelX
	}

	total := 0
	for i := minVelX; i <= maxVelX; i++ {
		for j := minVelY; j <= maxVelY; j++ {
			if intersect(i, j, minX, maxX, maxY, minY) {
				total++
			}
		}
	}

	fmt.Println(total)
}
