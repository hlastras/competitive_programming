package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
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
		r, _ := regexp.Compile("\\d")
		digits := r.FindAllString(line, -1)
		v, _ := strconv.Atoi(digits[0] + digits[len(digits)-1])
		total += v
	}

	fmt.Println(total)
}
