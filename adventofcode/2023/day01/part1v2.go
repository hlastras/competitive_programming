package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	for scanner.Scan() {
		digits := GetDigits2(scanner.Text())
		v, _ := strconv.Atoi(digits[0] + digits[len(digits)-1])
		total += v
	}

	fmt.Println(total)
}

func GetDigits2(s string) []string {
	var values []string
	for _, c := range s {
		if c >= '0' && c <= '9' {
			values = append(values, string(c))
		}
	}
	return values
}
