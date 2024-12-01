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
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var col_a []int
	set_b := map[int]int{}
	for scanner.Scan() {
		s := strings.Fields(scanner.Text())
		n1, _ := strconv.Atoi(s[0])
		col_a = append(col_a, n1)
		n2, _ := strconv.Atoi(s[1])
		set_b[n2]++
	}

	total := 0
	for _, v1 := range col_a {
		total += set_b[v1] * v1
	}

	fmt.Println(total)
}
