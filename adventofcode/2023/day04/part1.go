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
	var total int
	for _, line := range readFile() {
		content := line[strings.Index(line, ": ")+2:]
		splitIdx := strings.Index(content, " | ")
		winnerNumbers := parseNumbersIntoSet(content[:splitIdx])
		myNumbers := parseNumbersIntoSet(content[splitIdx+3:])

		counter := 0
		for num, _ := range myNumbers {
			if _, ok := winnerNumbers[num]; ok {
				counter++
			}
		}
		// Pow of 2
		if counter > 0 {
			total += 1 << (counter - 1)
		}
	}

	fmt.Println(total)
}

func parseNumbersIntoSet(s string) map[int]bool {
	set := make(map[int]bool)
	for _, n := range strings.Split(s, " ") {
		if n == "" {
			continue
		}
		number, _ := strconv.Atoi(n)
		set[number] = true
	}
	return set
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
