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
	scanner.Scan()
	template := scanner.Text()
	scanner.Scan()
	scanner.Text()

	changes := make(map[string]string)
	for scanner.Scan() {
		var x, y string
		fmt.Sscanf(scanner.Text(), "%s -> %s", &x, &y)
		changes[x] = string([]byte{x[0], y[0], x[1]})
	}

	for i := 0; i < 10; i++ {
		new_template := ""
		for j := 0; j < len(template)-1; j++ {
			if j == 0 {
				new_template += changes[template[j:j+2]]
			} else {
				new_template += changes[template[j:j+2]][1:]
			}
		}
		template = new_template
	}

	occ := make(map[rune]int)
	for _, c := range template {
		occ[c]++
	}

	min := -1
	max := -1

	for _, val := range occ {
		if min == -1 || val < min {
			min = val
		}
		if max == -1 || val > max {
			max = val
		}
	}

	fmt.Println(max - min)
}
