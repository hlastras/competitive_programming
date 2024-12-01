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
	file, err := os.Open("inputBig.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var total int
	for scanner.Scan() {
		digits := GetDigits(scanner.Text())
		v, _ := strconv.Atoi(digits[0] + digits[len(digits)-1])
		total += v
	}

	fmt.Println(total)
}

func GetDigits(s string) []string {
	transformations := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
		"1":     "1",
		"2":     "2",
		"3":     "3",
		"4":     "4",
		"5":     "5",
		"6":     "6",
		"7":     "7",
		"8":     "8",
		"9":     "9",
	}
	var values []string
	for i := 0; i <= len(s); i++ {
		for k, v := range transformations {
			if strings.HasPrefix(s[i:], k) {
				values = append(values, v)
			}
		}
	}

	return values
}
