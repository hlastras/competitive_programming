package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var number string
	var counters [12]int
	l := 0

	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%s", &number)
		if err != nil {
			log.Fatal(err)
		}

		for i, c := range number {
			if c == '1' {
				counters[i]++
			}
		}

		l++
	}

	gamma := 0
	epsilon := 0
	x := 1
	l = int(l / 2)
	for i := 11; i >= 0; i-- {
		if counters[i] >= l {
			gamma += x
		} else {
			epsilon += x
		}

		x *= 2
	}

	fmt.Println(gamma * epsilon)
}
