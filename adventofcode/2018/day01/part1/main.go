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
	result := 0
	x := 0
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d", &x)
		if err != nil {
			log.Fatal(err)
		}
		result = result + x
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}
