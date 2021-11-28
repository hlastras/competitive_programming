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
	var s []int
	x := 0
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d", &x)
		if err != nil {
			log.Fatal(err)
		}
		s = append(s, x)

	}

	frecuency := 0
	m := make(map[int]bool)
	m[0] = true
	i := 0
	for {
		x = s[i]
		frecuency += x
		if m[frecuency] {
			fmt.Println(frecuency)
			return
		} else {
			m[frecuency] = true
		}

		i += 1
		i %= len(s)
	}
}
