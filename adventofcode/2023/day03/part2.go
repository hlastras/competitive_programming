package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var line string
	var numbers []int
	var schema [][]int
	for scanner.Scan() {
		line = scanner.Text()
		n, l := process(line, len(numbers))
		numbers = append(numbers, n...)
		schema = append(schema, l)
	}

	total := calculate(numbers, schema)

	fmt.Println(total)
}

func calculate(numbers []int, schema [][]int) int {
	var total int
	for i := 0; i < len(schema); i++ {
		for j := 0; j < len(schema[0]); j++ {
			if schema[i][j] == -2 {
				// it is potential gear, check all adjacent positions
				seen := make(map[int]bool)
				if i > 0 && j > 0 && schema[i-1][j-1] >= 0 {
					seen[schema[i-1][j-1]] = true
				}
				if i > 0 && schema[i-1][j] >= 0 {
					seen[schema[i-1][j]] = true
				}
				if i > 0 && j < len(schema[0])-1 && schema[i-1][j+1] >= 0 {
					seen[schema[i-1][j+1]] = true
				}
				if j > 0 && schema[i][j-1] >= 0 {
					seen[schema[i][j-1]] = true
				}
				if j < len(schema[0])-1 && schema[i][j+1] >= 0 {
					seen[schema[i][j+1]] = true
				}
				if i < len(schema)-1 && j > 0 && schema[i+1][j-1] >= 0 {
					seen[schema[i+1][j-1]] = true
				}
				if i < len(schema)-1 && schema[i+1][j] >= 0 {
					seen[schema[i+1][j]] = true
				}
				if i < len(schema)-1 && j < len(schema[0])-1 && schema[i+1][j+1] >= 0 {
					seen[schema[i+1][j+1]] = true
				}

				if len(seen) == 2 {
					x := 1
					for k, _ := range seen {
						x *= numbers[k]
					}
					total += x
				}
			}
		}
	}
	return total
}

func process(line string, offset int) ([]int, []int) {
	processingNumber := false
	tmpNumber := ""
	newLine := make([]int, len(line))
	numbers := make([]int, 0)
	for i, r := range line {
		if r >= '0' && r <= '9' {
			processingNumber = true
			tmpNumber += string(r)
			newLine[i] = len(numbers) + offset
		} else {
			if processingNumber {
				// Stop processing number
				processingNumber = false
				newNumber, _ := strconv.Atoi(tmpNumber)
				numbers = append(numbers, newNumber)
				tmpNumber = ""
			}
			if r == '.' {
				newLine[i] = -1
			} else if r == '*' {
				newLine[i] = -2
			} else {
				newLine[i] = -3
			}
		}
	}

	if processingNumber {
		newNumber, _ := strconv.Atoi(tmpNumber)
		numbers = append(numbers, newNumber)
	}

	return numbers, newLine
}
