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
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var input [][]int
	var result [][]int
	for scanner.Scan() {
		line := scanner.Text()
		var row_input []int
		for _, c := range strings.Split(line, "") {
			n, _ := strconv.Atoi(c)
			row_input = append(row_input, n)
		}
		var new_row_input []int
		for i := 0; i < 5; i++ {
			for j := 0; j < len(row_input); j++ {
				val := row_input[j] + i
				if val > 9 {
					val -= 9
				}
				new_row_input = append(new_row_input, val)
			}
		}
		input = append(input, new_row_input)
	}

	end := len(input)
	for i := 1; i < 5; i++ {
		for j := 0; j < end; j++ {
			var r []int
			for k := 0; k < len(input[j]); k++ {
				val := input[j][k] + i
				if val > 9 {
					val -= 9
				}
				r = append(r, val)
			}
			input = append(input, r)
		}
	}

	for i := 0; i < len(input); i++ {
		var row []int
		for j := 0; j < len(input[0]); j++ {
			row = append(row, -1)
		}
		result = append(result, row)
	}

	result[0][0] = 0
	queue := [][2]int{{0, 0}}
	for len(queue) > 0 {
		point := queue[0]
		queue = queue[1:]
		x := point[0]
		y := point[1]

		if x-1 >= 0 {
			val := result[x][y] + input[x-1][y]
			if result[x-1][y] == -1 || result[x-1][y] > val {
				result[x-1][y] = val
				queue = append(queue, [2]int{x - 1, y})
			}
		}

		if y-1 >= 0 {
			val := result[x][y] + input[x][y-1]
			if result[x][y-1] == -1 || result[x][y-1] > val {
				result[x][y-1] = val
				queue = append(queue, [2]int{x, y - 1})
			}
		}

		if x+1 < len(result) {
			val := result[x][y] + input[x+1][y]
			if result[x+1][y] == -1 || result[x+1][y] > val {
				result[x+1][y] = val
				queue = append(queue, [2]int{x + 1, y})
			}
		}

		if y+1 < len(result[0]) {
			val := result[x][y] + input[x][y+1]
			if result[x][y+1] == -1 || result[x][y+1] > val {
				result[x][y+1] = val
				queue = append(queue, [2]int{x, y + 1})
			}
		}
	}

	fmt.Println(result[len(result)-1][len(result[0])-1])

	// for _, row := range input {
	// 	for _, x := range row {
	// 		fmt.Print(x)
	// 	}
	// 	fmt.Println()
	// }
}
