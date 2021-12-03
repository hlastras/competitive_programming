package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func index_of_last_zero(numbers []string, pos int) int {
	low := 0
	high := len(numbers) - 1

	for low <= high {
		median := (low + high) / 2

		if numbers[median][pos] == '0' {
			low = median + 1
		} else {
			high = median - 1
		}
	}
	return high
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var number string
	var numbers []string

	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%s", &number)
		if err != nil {
			log.Fatal(err)
		}

		numbers = append(numbers, number)
	}

	sort.Strings(numbers)

	numbers2 := numbers
	p := 0
	for len(numbers) > 1 {
		i := index_of_last_zero(numbers, p)
		if i >= (len(numbers) / 2) {
			numbers = numbers[:i+1]
		} else {
			numbers = numbers[i+1:]
		}
		p++
	}
	gamma, err := strconv.ParseInt(numbers[0], 2, 64)

	p = 0
	numbers = numbers2
	for len(numbers) > 1 {
		i := index_of_last_zero(numbers, p)
		if i < (len(numbers) / 2) {
			numbers = numbers[:i+1]
		} else {
			numbers = numbers[i+1:]
		}
		p++
	}
	epsilon, err := strconv.ParseInt(numbers[0], 2, 64)

	fmt.Println(gamma * epsilon)
}
