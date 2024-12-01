package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

type Item struct {
	X         int
	Y         int
	value     int
	Direction int
	Row       int
	index     int
	priority  int
}

type point struct {
	X int
	Y int
}

const up = 0
const down = 1
const left = 2
const right = 3

func add(queue []*Item, item *Item) []*Item {
	added := false
	for i, v := range queue {
		if v.X == item.X && v.Y == item.Y {
			added = true
			if v.value >= item.value {
				queue[i] = item
			}
		}
	}
	if !added {
		queue = append(queue, item)
	}

	sort.Slice(queue, func(i, j int) bool {
		return queue[i].value < queue[j].value
		//return queue[i].value+queue[i].Row < queue[j].value+queue[j].Row
	})

	return queue
}

func main() {
	matrix := parse(readFile())
	pq := make([]*Item, 0)
	seen := make(map[point]bool)
	final := make(map[point]*Item)

	pq = add(pq, &Item{0, 0, 0, right, 0, 0, 0})
	//pq = add(pq, &Item{1, 0, matrix[0][1], right, 1, 0, matrix[0][1]})
	//pq = add(pq, &Item{0, 1, matrix[1][0], down, 1, 0, matrix[1][0]})

	for {
		fmt.Println(len(pq), len(seen))
		//for _, v := range pq {
		//	fmt.Println(">>>>>>", v)
		//}
		if len(pq) == 0 {
			break
		}
		item := pq[0]
		pq = pq[1:]
		//fmt.Println(item)
		if seen[point{item.X, item.Y}] {
			fmt.Println("VISTOOO", item)
			continue
		}

		seen[point{item.X, item.Y}] = true
		final[point{item.X, item.Y}] = item
		if item.X == len(matrix[0])-1 && item.Y == len(matrix)-1 {
			fmt.Println(item.value)
			break
		}

		// Move right
		if item.Direction != left && item.X+1 < len(matrix[0]) && !seen[point{item.X + 1, item.Y}] {
			value := item.value + matrix[item.Y][item.X+1]
			if item.Direction == right {
				if item.Row < 2 {
					pq = add(pq, &Item{item.X + 1, item.Y, value, right, item.Row + 1, 0, value})
				}
			} else {
				pq = add(pq, &Item{item.X + 1, item.Y, value, right, 0, 0, value})
			}
		}

		// Move left
		if item.Direction != right && item.X-1 >= 0 && !seen[point{item.X - 1, item.Y}] {
			value := item.value + matrix[item.Y][item.X-1]
			if item.Direction == left {
				if item.Row < 2 {
					pq = add(pq, &Item{item.X - 1, item.Y, value, left, item.Row + 1, 0, value})
				}
			} else {
				pq = add(pq, &Item{item.X - 1, item.Y, value, left, 0, 0, value})
			}
		}

		// Move down
		if item.Direction != up && item.Y+1 < len(matrix) && !seen[point{item.X, item.Y + 1}] {
			value := item.value + matrix[item.Y+1][item.X]
			if item.Direction == down {
				if item.Row < 2 {
					pq = add(pq, &Item{item.X, item.Y + 1, value, down, item.Row + 1, 0, value})
				}
			} else {
				pq = add(pq, &Item{item.X, item.Y + 1, value, down, 0, 0, value})
			}
		}

		// Move up
		if item.Direction != down && item.Y-1 >= 0 && !seen[point{item.X, item.Y - 1}] {
			value := item.value + matrix[item.Y-1][item.X]
			if item.Direction == up {
				if item.Row < 2 {
					pq = add(pq, &Item{item.X, item.Y - 1, value, up, item.Row + 1, 0, value})
				}
			} else {
				pq = add(pq, &Item{item.X, item.Y - 1, value, up, 0, 0, value})
			}
		}
	}
	item := final[point{len(matrix[0]) - 1, len(matrix) - 1}]
	for {
		fmt.Println(item)
		if item.X == 0 && item.Y == 0 {
			break
		}
		matrix[item.Y][item.X] = item.Direction - 4
		switch item.Direction {
		case up:
			item = final[point{item.X, item.Y + 1}]
		case down:
			item = final[point{item.X, item.Y - 1}]
		case left:
			item = final[point{item.X + 1, item.Y}]
		case right:
			item = final[point{item.X - 1, item.Y}]
		}
	}

	colorReset := "\033[0m"
	colorRed := "\033[31m"
	for _, row := range matrix {
		for _, col := range row {
			if col < 0 {
				switch col {
				case -1:
					fmt.Print(colorRed, ">", colorReset)
				case -2:
					fmt.Print(colorRed, "<", colorReset)
				case -3:
					fmt.Print(colorRed, "v", colorReset)
				case -4:
					fmt.Print(colorRed, "^", colorReset)
				}
			} else {
				fmt.Print(col)
			}

		}
		fmt.Println()
	}
}

func parse(lines []string) [][]int {
	var matrix [][]int
	for _, line := range lines {
		var row []int
		for _, char := range line {
			n, _ := strconv.Atoi(string(char))
			row = append(row, n)
		}
		matrix = append(matrix, row)
	}
	return matrix
}

func readFile() []string {
	file, err := os.Open("/Users/hector.arranz/competitive_programming/adventofcode/2023/day17/input.txt")
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
