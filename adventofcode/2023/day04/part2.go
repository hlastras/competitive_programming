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
	lines := readFile()
	cards := make([]int, len(lines), len(lines))
	for i, _ := range cards {
		cards[i] = 1
	}

	for i, line := range lines {
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

		for x := 0; x < counter; x++ {
			cards[i+x+1] += cards[i]
		}
	}

	sum := 0
	for _, v := range cards {
		sum += v
	}
	fmt.Println(sum)
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
