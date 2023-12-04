package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const blueMax = 14
const greenMax = 13
const redMax = 12

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var total int
	var line string
	for scanner.Scan() {
		line = scanner.Text()
		total += Calculate(line)
	}

	fmt.Println(total)
}

func Calculate(s string) int {
	x := strings.Split(s, ": ")
	sets := strings.Split(x[1], "; ")
	for _, set := range sets {
		items := strings.Split(set, ", ")
		for _, item := range items {
			y := strings.Split(item, " ")
			quantity, _ := strconv.Atoi(y[0])
			color := y[1]
			switch color {
			case "blue":
				if quantity > blueMax {
					return 0
				}
			case "green":
				if quantity > greenMax {
					return 0
				}
			case "red":
				if quantity > redMax {
					return 0
				}
			}
		}
	}

	var id int
	fmt.Sscanf(x[0], "Game %d", &id)
	return id
}
