package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/bits-and-blooms/bitset"
)

func searchByLen(values []*bitset.BitSet, l uint) []*bitset.BitSet {
	var result []*bitset.BitSet
	for _, v := range values {
		if v.Count() == l {
			result = append(result, v)
		}
	}
	return result
}

func parse(s string) *bitset.BitSet {
	var b bitset.BitSet
	for _, v := range s {
		b.Set(uint(v - 97))
	}
	return &b
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	total := 0
	for scanner.Scan() {
		numbers := make(map[int]*bitset.BitSet)
		input := strings.Split(scanner.Text(), " | ")
		var tests []*bitset.BitSet
		for _, x := range strings.Split(input[0], " ") {
			tests = append(tests, parse(x))
		}

		// Search known numbers
		numbers[1] = searchByLen(tests, 2)[0]
		numbers[4] = searchByLen(tests, 4)[0]
		numbers[7] = searchByLen(tests, 3)[0]
		numbers[8] = searchByLen(tests, 7)[0]

		// Search 0, 6, and 9
		for _, n := range searchByLen(tests, 6) {
			if n.Intersection(numbers[1]).Count() == 1 {
				numbers[6] = n
			} else if n.Intersection(numbers[4]).Count() == 4 {
				numbers[9] = n
			} else {
				numbers[0] = n
			}
		}

		// Search 2, 3 and 5
		for _, n := range searchByLen(tests, 5) {
			if n.Intersection(numbers[1]).Count() == 2 {
				numbers[3] = n
			} else if n.Intersection(numbers[4]).Count() == 2 {
				numbers[2] = n
			} else {
				numbers[5] = n
			}
		}

		// Calc result
		i := 1000
		for _, x := range strings.Split(input[1], " ") {
			n := parse(x)
			for k, v := range numbers {
				if n.Equal(v) {
					total += i * k
					break
				}
			}
			i = int(i / 10)
		}
	}

	fmt.Println(total)
}
