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
	var minX, maxX, minY, maxY int
	scanner.Scan()
	fmt.Sscanf(scanner.Text(), "target area: x=%d..%d, y=%d..%d", &minX, &maxX, &minY, &maxY)

	total := 0
	minY = -minY
	for i := 1; i < minY; i++ {
		total += i
	}
	fmt.Println(total)
}
