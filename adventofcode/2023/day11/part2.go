package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
)

type point [2]int

func main() {
	matrix := readFile()
	emptyCols := make([]int, 0)
	emptyRows := make([]int, 0)
	for row := 0; row < len(matrix); row++ {
		if isEmptyRow(matrix[row]) {
			emptyRows = append(emptyRows, row)
		}
	}
	for col := 0; col < len(matrix[0]); col++ {
		if isEmptyCol(matrix, col) {
			emptyCols = append(emptyCols, col)
		}
	}

	galaxies := make([]point, 0)
	for row := 0; row < len(matrix); row++ {
		for col := 0; col < len(matrix[row]); col++ {
			if matrix[row][col] == '#' {
				galaxies = append(galaxies, point{row, col})
			}
		}
	}

	total := 0
	for i := 0; i < len(galaxies); i++ {
		for j := i + 1; j < len(galaxies); j++ {
			total += distance(galaxies[i], galaxies[j], emptyRows, emptyCols)
		}
	}

	fmt.Println(total)
}

func distance(p1, p2 point, emptyRows, emptyCols []int) int {
	x := int(math.Abs(float64(p1[0]-p2[0]))) + count(p1[0], p2[0], emptyRows)*999999
	y := int(math.Abs(float64(p1[1]-p2[1]))) + count(p1[1], p2[1], emptyCols)*999999
	return x + y
}

func count(a, b int, empty []int) int {
	count := 0
	for _, v := range empty {
		if (v > a && v < b) || (v > b && v < a) {
			count++
		}
	}
	return count
}

func isEmptyRow(row string) bool {
	for _, c := range row {
		if c == '#' {
			return false
		}
	}
	return true
}

func isEmptyCol(matrix []string, col int) bool {
	for row := 0; row < len(matrix); row++ {
		if matrix[row][col] == '#' {
			return false
		}
	}
	return true
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
