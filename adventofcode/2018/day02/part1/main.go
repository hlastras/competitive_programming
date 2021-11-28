package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)

	total_two := 0
	total_three := 0
	for scanner.Scan() {
		line := scanner.Text()
		freq := make(map[rune]int)
		for _, c := range line {
			freq[c]++
		}

		has_two := false
		has_three := false
		for _, value := range freq {
			if value == 2 {
				has_two = true
			}
			if value == 3 {
				has_three = true
			}
		}

		if has_two {
			total_two++
		}

		if has_three {
			total_three++
		}
	}

	result := total_two * total_three
	fmt.Printf("%d\n", result)
}
