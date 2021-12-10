package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	pairs := map[rune]rune{
		'(': ')',
		'[': ']',
		'{': '}',
		'<': '>',
	}
	points := map[rune]int{
		')': 1,
		']': 2,
		'}': 3,
		'>': 4,
	}
	var scores []int
	for scanner.Scan() {
		var stack []rune
		var corrupted bool
		for _, n := range scanner.Text() {
			if _, is_open := pairs[n]; is_open {
				stack = append(stack, pairs[n])
			} else if n == stack[len(stack)-1] {
				stack = stack[:len(stack)-1]
			} else {
				corrupted = true
				break
			}
		}

		if !corrupted {
			total := 0
			for i := len(stack) - 1; i >= 0; i-- {
				total = (total * 5) + points[stack[i]]
			}
			scores = append(scores, total)
		}
	}
	sort.Ints(scores)
	fmt.Println(scores[int(len(scores)/2)])
}
