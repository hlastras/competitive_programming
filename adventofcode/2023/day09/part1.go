package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	total := 0
	for _, line := range readFile() {
		lineTotal := 0
		numbers := parseNumbersIntoSlice(line)
		for {
			lineTotal += numbers[len(numbers)-1]
			newNumbers := make([]int, len(numbers)-1)
			for i := 0; i < len(numbers)-1; i++ {
				newNumbers[i] = numbers[i+1] - numbers[i]
			}
			if isAllZeroes(newNumbers) {
				break
			}
			numbers = newNumbers
		}
		total += lineTotal
	}
	fmt.Println(total)
}

func isAllZeroes(numbers []int) bool {
	for _, n := range numbers {
		if n != 0 {
			return false
		}
	}
	return true
}

func parseNumbersIntoSlice(s string) []int {
	var numbers []int
	for _, n := range strings.Split(s, " ") {
		if n == "" {
			continue
		}
		number, _ := strconv.Atoi(n)
		numbers = append(numbers, number)
	}
	return numbers
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
