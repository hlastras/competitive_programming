package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	patterns := make([][][]bool, 0)
	current := make([][]bool, 0)
	for _, line := range readFile() {
		if line == "" {
			patterns = append(patterns, current)
			current = make([][]bool, 0)
			continue
		}
		current = append(current, parseLine(line))
	}
	patterns = append(patterns, current)

	cols := 0
	rows := 0
	for _, pattern := range patterns {
		cols += searchVertical(pattern)
		rows += searchHorizontal(pattern)
	}

	fmt.Println(rows*100 + cols)
}

func searchHorizontal(pattern [][]bool) int {
	for i := 0; i < len(pattern)-1; i++ {
		allEqual := true
		for a, b := i, i+1; a >= 0 && b < len(pattern); a, b = a-1, b+1 {
			if !isEqualRow(a, b, pattern) {
				allEqual = false
				break
			}
		}
		if allEqual {
			return i + 1
		}
	}
	return 0
}

func searchVertical(pattern [][]bool) int {
	for i := 0; i < len(pattern[0])-1; i++ {
		allEqual := true
		for a, b := i, i+1; a >= 0 && b < len(pattern[0]); a, b = a-1, b+1 {
			if !isEqualCol(a, b, pattern) {
				allEqual = false
				break
			}
		}
		if allEqual {
			return i + 1
		}
	}
	return 0
}

func isEqualRow(i, j int, pattern [][]bool) bool {
	for k := 0; k < len(pattern[i]); k++ {
		if pattern[i][k] != pattern[j][k] {
			return false
		}
	}
	return true
}

func isEqualCol(i, j int, pattern [][]bool) bool {
	for k := 0; k < len(pattern); k++ {
		if pattern[k][i] != pattern[k][j] {
			return false
		}
	}
	return true
}

func parseLine(line string) []bool {
	result := make([]bool, 0)
	for _, c := range line {
		if c == '#' {
			result = append(result, true)
		} else {
			result = append(result, false)
		}
	}
	return result
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
