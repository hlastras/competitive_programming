package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	commands := strings.Split(readFile()[0], ",")

	total := 0
	for _, command := range commands {
		total += hash(command)
	}
	fmt.Println(total)
}

func hash(command string) int {
	total := 0
	for _, c := range command {
		total += int(c)
		total *= 17
		total %= 256
	}
	return total
}

func readFile() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}
