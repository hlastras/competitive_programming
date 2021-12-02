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

	var command string
	var value int
	var h, d, a int
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%s %d", &command, &value)
		if err != nil {
			log.Fatal(err)
		}
		switch command {
		case "forward":
			h += value
			d += (a * value)
		case "up":
			a -= value
		case "down":
			a += value
		}
	}

	fmt.Println(h * d)
}
