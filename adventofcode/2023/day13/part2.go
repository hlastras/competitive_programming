package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type point []int

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
		rows += searchHorizontal(pattern)
		cols += searchVertical(pattern)
	}

	fmt.Println(rows*100 + cols)
}

func searchHorizontal(pattern [][]bool) int {
	for i := 0; i < len(pattern)-1; i++ {
		allEqual := true
		singleDiff := point{-1, -1}
		for a, b := i, i+1; a >= 0 && b < len(pattern); a, b = a-1, b+1 {
			result := isEqualRow(a, b, pattern)
			if result == -2 {
				// diff more than 1
				allEqual = false
				break
			}
			if result >= 0 {
				// one diff
				if singleDiff[0] == -1 {
					// No previous diff
					singleDiff = point{a, result}
				} else {
					// Already one diff
					allEqual = false
					break
				}
			}
		}
		if allEqual && singleDiff[0] != -1 {
			return i + 1
		}
	}
	return 0
}

func searchVertical(pattern [][]bool) int {
	for i := 0; i < len(pattern[0])-1; i++ {
		allEqual := true
		singleDiff := point{-1, -1}
		for a, b := i, i+1; a >= 0 && b < len(pattern[0]); a, b = a-1, b+1 {
			result := isEqualCol(a, b, pattern)
			if result == -2 {
				// diff more than 1
				allEqual = false
				break
			}
			if result >= 0 {
				// one diff
				if singleDiff[0] == -1 {
					// No previous diff
					singleDiff = point{a, result}
				} else {
					// Already one diff
					allEqual = false
					break
				}
			}
		}
		if allEqual && singleDiff[0] != -1 {
			return i + 1
		}
	}
	return 0
}

// return: -2 if more than one diff, -1 if all equal, >= 0 if one diff (this is the diff point)
func isEqualRow(i, j int, pattern [][]bool) int {
	diff := 0
	diffPoint := -1
	for k := 0; k < len(pattern[i]); k++ {
		if pattern[i][k] != pattern[j][k] {
			if diff > 0 {
				return -2
			}
			diff++
			diffPoint = k
		}
	}
	return diffPoint
}

// return: -2 if more than one diff, -1 if all equal, >= 0 if one diff (this is the diff point)
func isEqualCol(i, j int, pattern [][]bool) int {
	diff := 0
	diffPoint := -1
	for k := 0; k < len(pattern); k++ {
		if pattern[k][i] != pattern[k][j] {
			if diff > 0 {
				return -2
			}
			diff++
			diffPoint = k
		}
	}
	return diffPoint
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
