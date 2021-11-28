package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func diff(value1, value2 string) int {
	result := 0
	for i := 0; i < len(value1); i++ {
		if value1[i] != value2[i] {
			result++
		}
	}
	return result
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	var ids []string

	for scanner.Scan() {
		line := scanner.Text()
		ids = append(ids, line)
	}

	for i := 0; i < len(ids); i++ {
		for j := i + 1; j < len(ids); j++ {
			if diff(ids[i], ids[j]) == 1 {
				result := ""
				for k := 0; k < len(ids[i]); k++ {
					if ids[i][k] == ids[j][k] {
						result += string(ids[i][k])
					}
				}
				fmt.Printf("%s\n", result)
				return
			}
		}
	}
}
