package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

const roundRock = 0
const fixedRock = 1
const empty = 2

func main() {
	matrix := make([][]int, 0)
	for _, line := range readFile() {
		matrix = append(matrix, parseLine(line))
	}
	total := 0

	seen := make(map[int]int)
	reverse := make(map[int]int)

	for count := 0; count < 10000000; count++ {
		total = 0
		for row := 0; row < len(matrix); row++ {
			for col := 0; col < len(matrix[row]); col++ {
				if matrix[row][col] == roundRock {
					total += moveNorth(matrix, row, col)
				}
			}
		}
		//fmt.Println(total)

		total = 0
		for col := 0; col < len(matrix[0]); col++ {
			for row := 0; row < len(matrix); row++ {
				if matrix[row][col] == roundRock {
					total += moveWest(matrix, row, col)
				}
			}
		}
		//fmt.Println(total)

		total = 0
		for row := len(matrix) - 1; row >= 0; row-- {
			for col := 0; col < len(matrix[row]); col++ {
				if matrix[row][col] == roundRock {
					total += moveSouth(matrix, row, col)
				}
			}
		}
		//fmt.Println(total)

		total = 0
		for col := len(matrix[0]) - 1; col >= 0; col-- {
			for row := 0; row < len(matrix); row++ {
				if matrix[row][col] == roundRock {
					total += moveEast(matrix, row, col)
				}
			}
		}

		if v, ok := seen[total]; ok && count-v > 1 {
			le := count - v
			fmt.Println(le, v, count)
			fmt.Println((1000000000 - v) % le)
			fmt.Println(reverse[v-1+(1000000000-v)%le])
			break
		}
		if count-seen[total] > 1 {
			seen[total] = count
			reverse[count] = total
		}
	}
	//fmt.Println(total)
	//fmt.Println(values)
	//fmt.Println(floydsAlgorithm(values))
}

func floydsAlgorithm(sequence []int) (int, int) {
	// Step 1: Initialize tortoise and hare
	tortoise := sequence[0]
	hare := sequence[0]

	// Step 2: Find the meeting point to confirm a cycle exists
	for {
		tortoise = sequence[tortoise]
		hare = sequence[sequence[hare]]
		if tortoise == hare {
			break
		}
	}

	// Step 3: Find the start of the cycle
	tortoise = sequence[0]
	for tortoise != hare {
		tortoise = sequence[tortoise]
		hare = sequence[hare]
	}
	startOfCycle := tortoise

	// Step 4: Find the length of the cycle
	cycleLength := 1
	hare = sequence[tortoise]
	for tortoise != hare {
		hare = sequence[hare]
		cycleLength++
	}

	return startOfCycle, cycleLength
}

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		for _, v := range row {
			switch v {
			case empty:
				fmt.Print(".")
			case fixedRock:
				fmt.Print("#")
			case roundRock:
				fmt.Print("O")
			}
		}
		fmt.Println()
	}
	fmt.Println()

}

func moveNorth(matrix [][]int, row int, col int) int {
	for i := row; i > 0; i-- {
		if matrix[i-1][col] != empty {
			return len(matrix) - i
		}
		matrix[i][col] = empty
		matrix[i-1][col] = roundRock
	}
	return len(matrix)
}

func moveSouth(matrix [][]int, row int, col int) int {
	for i := row; i < len(matrix)-1; i++ {
		if matrix[i+1][col] != empty {
			return len(matrix) - i
		}
		matrix[i][col] = empty
		matrix[i+1][col] = roundRock
	}
	return 1
}

func moveEast(matrix [][]int, row int, col int) int {
	for i := col; i < len(matrix[row])-1; i++ {
		if matrix[row][i+1] != empty {
			return len(matrix) - row
		}
		matrix[row][i] = empty
		matrix[row][i+1] = roundRock
	}
	return len(matrix) - row
}

func moveWest(matrix [][]int, row int, col int) int {
	for i := col; i > 0; i-- {
		if matrix[row][i-1] != empty {
			return len(matrix) - row
		}
		matrix[row][i] = empty
		matrix[row][i-1] = roundRock
	}
	return len(matrix) - row
}

func parseLine(line string) []int {
	var row []int
	for _, char := range line {
		v := 0
		switch char {
		case '.':
			v = empty
		case '#':
			v = fixedRock
		case 'O':
			v = roundRock
		}
		row = append(row, v)
	}
	return row
}

func readFile() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}
