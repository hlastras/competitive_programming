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
	var measurements []int
	var x int
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d", &x)
		if err != nil {
			log.Fatal(err)
		}
		measurements = append(measurements, x)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	result := 0
	for i := 1; i < len(measurements); i++ {
		if measurements[i] > measurements[i-1] {
			result++
		}
	}
	fmt.Println(result)
}
