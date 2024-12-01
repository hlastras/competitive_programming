package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const operational = 0
const damaged = 1
const unknown = 2

func main() {
	total := 0
	for _, line := range readFile() {
		v := strings.Split(line, " ")
		r := v[0]
		n := parseNumbersIntoSlice(v[1])
		for i := 0; i < 5; i++ {
			r += "?" + v[0]
			n = append(n, parseNumbersIntoSlice(v[1])...)
		}
		re := regexp.MustCompile(`\.+`)
		r = re.ReplaceAllString(r, ".")
		if r[len(r)-1] == '.' {
			r = r[:len(r)-1]
		}
		fmt.Println(r)
		fmt.Println(strings.Split(r, "."))
		fmt.Println(n)
		fmt.Println(len(strings.Split(r, ".")), len(n), len(strings.Split(r, ".")) == len(n))

	}
	fmt.Println(total)
}

func solve(i int, records []int, n []int, result int) int {
	if i == len(records) {
		if validate(records, n) {
			result++
		}
		return result
	}

	if records[i] == unknown {
		records[i] = operational
		result = solve(i+1, records, n, result)
		records[i] = damaged
		result = solve(i+1, records, n, result)
		records[i] = unknown
	} else {
		result = solve(i+1, records, n, result)
	}
	return result
}

func validate(records []int, n []int) bool {
	damagedLenGroups := make([]int, 1)

	for i := 0; i < len(records); i++ {
		if records[i] == damaged {
			damagedLenGroups[len(damagedLenGroups)-1]++
		} else if damagedLenGroups[len(damagedLenGroups)-1] > 0 {
			damagedLenGroups = append(damagedLenGroups, 0)
		}
	}

	if damagedLenGroups[len(damagedLenGroups)-1] == 0 {
		damagedLenGroups = damagedLenGroups[:len(damagedLenGroups)-1]
	}

	return areEqual(damagedLenGroups, n)
}

func areEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if b[i] != v {
			return false
		}
	}
	return true
}

func parseRecords(s string) []int {
	result := make([]int, 0)
	for _, c := range s {
		if c == '#' {
			result = append(result, damaged)
		} else if c == '.' {
			result = append(result, operational)
		} else {
			result = append(result, unknown)
		}
	}
	return result
}
func parseNumbersIntoSlice(s string) []int {
	var numbers []int
	for _, n := range strings.Split(s, ",") {
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
