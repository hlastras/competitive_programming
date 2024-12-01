package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    for _, line := range readFile() {
        fmt.Println(line)
    }
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

