package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Transformer struct {
	SourceStart      int
	SourceEnd        int
	DestinationStart int
	DestinationEnd   int
	Diff             int
}

func main() {
	lines := readFile()
	seeds := parseNumbersIntoSlice(lines[0][strings.Index(lines[0], "seeds: ")+7:])
	lines = lines[3:]
	t := make([][]Transformer, 0)
	current := make([]Transformer, 0)
	for i := 0; i < len(lines); i++ {
		if lines[i] == "" {
			// end of group
			t = append(t, current)
			current = make([]Transformer, 0)
			i++
			continue
		}
		numbers := parseNumbersIntoSlice(lines[i])
		current = append(current, Transformer{
			SourceStart:      numbers[1],
			SourceEnd:        numbers[1] + numbers[2] - 1,
			DestinationStart: numbers[0],
			DestinationEnd:   numbers[0] + numbers[2] - 1,
			Diff:             numbers[0] - numbers[1],
		})
	}
	t = append(t, current)

	total := -1
	for _, seed := range seeds {
		for _, transformer := range t {
			seed = transform(seed, transformer)
		}
		if total == -1 || seed < total {
			total = seed
		}
	}

	fmt.Println(total)
}

func transform(seed int, transformers []Transformer) int {
	for _, t := range transformers {
		if seed >= t.SourceStart && seed <= t.SourceEnd {
			return seed + t.Diff
		}
	}
	return seed
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
