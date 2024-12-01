package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

const roundRock = 0
const fixedRock = 1
const empty = 2

func main() {
	matrix := make([][]int, 0)
	for _, line := range readFile() {
		matrix = append(matrix, parseLine(line))
	}

	total := 0
	for row := 0; row < len(matrix); row++ {
		for col := 0; col < len(matrix[row]); col++ {
			if matrix[row][col] == roundRock {
				total += move(matrix, row, col)
			}
		}
	}
	fmt.Println(total)
}

func move(matrix [][]int, row int, col int) int {
	for i := row; i > 0; i-- {
		if matrix[i-1][col] != empty {
			return len(matrix) - i
		}
		matrix[i][col] = empty
		matrix[i-1][col] = roundRock
	}
	return len(matrix)
}

func parseLine(line string) []int {
	var row []int
	for _, char := range line {
		v := 0
		switch char {
		case '.':
			v = empty
		case '#':
			v = fixedRock
		case 'O':
			v = roundRock
		}
		row = append(row, v)
	}
	return row
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
