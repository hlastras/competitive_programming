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
	expandedMatrix := expandMatrix(matrix)

	galaxies := make([]point, 0)
	for row := 0; row < len(expandedMatrix); row++ {
		for col := 0; col < len(expandedMatrix[row]); col++ {
			if expandedMatrix[row][col] {
				galaxies = append(galaxies, point{row, col})
			}
		}
	}

	total := 0
	for i := 0; i < len(galaxies); i++ {
		for j := i + 1; j < len(galaxies); j++ {
			total += int(math.Abs(float64(galaxies[i][0]-galaxies[j][0])) + math.Abs(float64(galaxies[i][1]-galaxies[j][1])))
		}
	}

	fmt.Println(total)
}

func expandMatrix(matrix []string) [][]bool {
	colsToExpand := make(map[int]bool)
	for col := 0; col < len(matrix[0]); col++ {
		anyItem := false
		for row := 0; row < len(matrix); row++ {
			if matrix[row][col] == '#' {
				anyItem = true
				break
			}
		}
		if !anyItem {
			colsToExpand[col] = true
		}
	}
	expandedMatrix := make([][]bool, 0)
	for row := 0; row < len(matrix); row++ {
		if isEmptyRow(matrix[row]) {
			expandedMatrix = append(expandedMatrix, make([]bool, len(matrix[row])+len(colsToExpand)))
			expandedMatrix = append(expandedMatrix, make([]bool, len(matrix[row])+len(colsToExpand)))
			continue
		}
		newRow := make([]bool, 0)
		for col := 0; col < len(matrix[row]); col++ {
			if colsToExpand[col] {
				newRow = append(newRow, false)
			}
			newRow = append(newRow, matrix[row][col] == '#')
		}
		expandedMatrix = append(expandedMatrix, newRow)
	}
	return expandedMatrix
}

func isEmptyRow(row string) bool {
	for _, c := range row {
		if c == '#' {
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
