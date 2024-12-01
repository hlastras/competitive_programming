package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	lines := readFile()
	times := parseNumbersIntoSlice(lines[0][strings.Index(lines[0], ":")+1:])
	distances := parseNumbersIntoSlice(lines[1][strings.Index(lines[1], ":")+1:])

	total := 1
	for i, t := range times {
		start, end := calculateRange(t, distances[i])
		total *= end - start + 1
	}

	fmt.Println(total)
}

func calculateRange(time, distance int) (int, int) {
	t := float64(time)
	d := float64(distance)
	start := (t - math.Sqrt(math.Pow(t, 2)-4*d)) / 2
	end := (t + math.Sqrt(math.Pow(t, 2)-4*d)) / 2

	return nextInt(start), previousInt(end)
}

func nextInt(x float64) int {
	if x == float64(int(x)) {
		return int(x) + 1
	}
	return int(math.Floor(x)) + 1
}

func previousInt(x float64) int {
	if x == float64(int(x)) {
		return int(x) - 1
	}
	return int(math.Floor(x))
}

func parseNumbersIntoSlice(s string) []int {
	s = strings.Replace(s, " ", "", -1)
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
