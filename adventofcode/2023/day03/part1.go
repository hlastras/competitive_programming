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

	var totalBefore, totalAfter int
	for _, number := range numbers {
		totalBefore += number
	}
	cleanNumbers(numbers, schema)
	for _, number := range numbers {
		totalAfter += number
	}

	fmt.Println(totalBefore - totalAfter)
}

func cleanNumbers(numbers []int, schema [][]int) {
	for i := 0; i < len(schema); i++ {
		for j := 0; j < len(schema[0]); j++ {
			if schema[i][j] == -1 {
				// it is a symbol, check all adjacent numbers (if exists)
				if i > 0 && j > 0 && schema[i-1][j-1] >= 0 {
					numbers[schema[i-1][j-1]] = 0
				}
				if i > 0 && schema[i-1][j] >= 0 {
					numbers[schema[i-1][j]] = 0
				}
				if i > 0 && j < len(schema[0])-1 && schema[i-1][j+1] >= 0 {
					numbers[schema[i-1][j+1]] = 0
				}
				if j > 0 && schema[i][j-1] >= 0 {
					numbers[schema[i][j-1]] = 0
				}
				if j < len(schema[0])-1 && schema[i][j+1] >= 0 {
					numbers[schema[i][j+1]] = 0
				}
				if i < len(schema)-1 && j > 0 && schema[i+1][j-1] >= 0 {
					numbers[schema[i+1][j-1]] = 0
				}
				if i < len(schema)-1 && schema[i+1][j] >= 0 {
					numbers[schema[i+1][j]] = 0
				}
				if i < len(schema)-1 && j < len(schema[0])-1 && schema[i+1][j+1] >= 0 {
					numbers[schema[i+1][j+1]] = 0
				}
			}
		}
	}
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
				newLine[i] = -2
			} else {
				newLine[i] = -1
			}
		}
	}

	if processingNumber {
		newNumber, _ := strconv.Atoi(tmpNumber)
		numbers = append(numbers, newNumber)
	}

	return numbers, newLine
}
