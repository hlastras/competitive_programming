package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func calculatePoints(s [4]int) [][2]int {
	var result [][2]int

	if s[0] == s[2] {
		var inc int
		if s[1] > s[3] {
			inc = -1
		} else {
			inc = 1
		}

		for s[1] != s[3] {
			result = append(result, [2]int{s[0], s[1]})
			s[1] += inc
		}
		result = append(result, [2]int{s[0], s[1]})
	} else {
		var inc int
		if s[0] > s[2] {
			inc = -1
		} else {
			inc = 1
		}

		for s[0] != s[2] {
			result = append(result, [2]int{s[0], s[1]})
			s[0] += inc
		}
		result = append(result, [2]int{s[0], s[1]})
	}

	return result
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var segments [][4]int
	var numbers []int
	var x1, y1, x2, y2 int
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d,%d -> %d,%d", &x1, &y1, &x2, &y2)
		if err != nil {
			log.Fatal(err)
		}
		if x1 == x2 || y1 == y2 {
			segments = append(segments, [4]int{x1, y1, x2, y2})
			numbers = append(numbers, x1)
			numbers = append(numbers, x2)
			numbers = append(numbers, y1)
			numbers = append(numbers, y2)
		}
	}

	m := 0
	for _, v := range numbers {
		if v > m {
			m = v
		}
	}

	matrix := make(map[int]int)
	for _, s := range segments {
		points := calculatePoints(s)
		for _, p := range points {
			i := p[0]*m + p[1]
			matrix[i]++
		}
	}

	total := 0
	for _, v := range matrix {
		if v >= 2 {
			total++
		}
	}

	fmt.Println(total)
}
