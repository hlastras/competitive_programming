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

	for i := 0; i < 80; i++ {
		var to_add []int
		for j := 0; j < len(numbers); j++ {
			if numbers[j] == 0 {
				numbers[j] = 7
				to_add = append(to_add, 8)
			}
			numbers[j]--
		}
		numbers = append(numbers, to_add...)
	}

	fmt.Println(len(numbers))
}
