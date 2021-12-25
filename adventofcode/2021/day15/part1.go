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
		var row_result []int
		for _, c := range strings.Split(line, "") {
			n, _ := strconv.Atoi(c)
			row_input = append(row_input, n)
			row_result = append(row_result, -1)
		}
		input = append(input, row_input)
		result = append(result, row_result)
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
}
