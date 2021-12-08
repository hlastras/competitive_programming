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
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var numbers []int
	for scanner.Scan() {
		var a string
		fmt.Sscanf(scanner.Text(), "%s", &a)
		b := strings.Split(a, ",")
		for _, x := range b {
			l, _ := strconv.Atoi(x)
			numbers = append(numbers, l)
		}
	}

	counters := [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

	for _, v := range numbers {
		counters[v]++
	}

	for i := 0; i < 256; i++ {
		counters[9] = counters[7]
		counters[7] = counters[8]
		counters[8] = counters[i%7]
		counters[i%7] += counters[9]
	}

	total := 0
	for i := 0; i < 9; i++ {
		total += counters[i]
	}

	fmt.Println(total)
}
