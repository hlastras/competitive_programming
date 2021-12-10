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
	defer file.Close()
	scanner := bufio.NewScanner(file)
	pairs := map[rune]rune{
		'(': ')',
		'[': ']',
		'{': '}',
		'<': '>',
	}
	points := map[rune]int{
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137,
	}
	total := 0
	for scanner.Scan() {
		var stack []rune
		for _, n := range scanner.Text() {
			if _, is_open := pairs[n]; is_open {
				stack = append(stack, pairs[n])
			} else if n == stack[len(stack)-1] {
				stack = stack[:len(stack)-1]
			} else {
				total += points[n]
				break
			}
		}
	}
	fmt.Println(total)

}
