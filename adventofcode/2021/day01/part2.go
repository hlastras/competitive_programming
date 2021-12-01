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

	var m []int
	m = append(m, 0)
	var buffer [3]int
	var x, i int
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d", &x)
		if err != nil {
			log.Fatal(err)
		}
		m = append(m, m[len(m)-1]+x-buffer[i])
		buffer[i] = x
		i = (i + 1) % 3
	}

	m = m[3:]

	result := 0
	for i := 1; i < len(m); i++ {
		if m[i] > m[i-1] {
			result++
		}
	}
	fmt.Println(result)
}
