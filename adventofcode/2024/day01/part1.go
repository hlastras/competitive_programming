package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var col_a, col_b []int
	for scanner.Scan() {
		s := strings.Fields(scanner.Text())
		n1, _ := strconv.Atoi(s[0])
		col_a = append(col_a, n1)
		n2, _ := strconv.Atoi(s[1])
		col_b = append(col_b, n2)
	}

	sort.Ints(col_a)
	sort.Ints(col_b)

	total := 0
	for i, v1 := range col_a {
		total += abs(v1 - col_b[i])
	}

	fmt.Println(total)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
