package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Sumatory(x int) int {
	total := 0
	for i := 1; i <= x; i++ {
		total += i
	}
	return total
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var numbers []int
	var max int
	for scanner.Scan() {
		var a string
		fmt.Sscanf(scanner.Text(), "%s", &a)
		b := strings.Split(a, ",")
		for _, x := range b {
			l, _ := strconv.Atoi(x)
			numbers = append(numbers, l)
			if l > max {
				max = l
			}
		}
	}

	best := -1
	for i := 0; i < max; i++ {
		diff := 0
		for _, v := range numbers {
			diff += Sumatory(Abs(v - i))
		}

		if best == -1 || diff < best {
			best = diff
		}
	}

	fmt.Println(best)
}
