package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	target := map[int]bool{
		2: true,
		3: true,
		4: true,
		7: true,
	}

	total := 0
	for scanner.Scan() {
		b := strings.Split(scanner.Text(), " | ")
		for _, x := range strings.Split(b[1], " ") {
			if target[len(x)] {
				total++
			}
		}
	}

	fmt.Println(total)
}
