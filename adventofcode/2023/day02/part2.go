package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

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
	var maxBlue, maxGreen, maxRed int
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
				maxBlue = Max(maxBlue, quantity)
			case "green":
				maxGreen = Max(maxGreen, quantity)
			case "red":
				maxRed = Max(maxRed, quantity)
			}
		}
	}

	return maxBlue * maxGreen * maxRed
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
