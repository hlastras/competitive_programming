package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
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

func main() {
	matrix := parse(readFile())
	pq := make(PriorityQueue, 0)

	heap.Init(&pq)
	heap.Push(&pq, &Item{0, 0, 0, -1, 0, 0, 0})

	seen := make(map[point]bool)

	for {
		fmt.Println(len(pq), len(seen))
		//fmt.Println(len(seen))
		if len(pq) == 0 {
			break
		}
		item := heap.Pop(&pq).(*Item)
		seen[point{item.X, item.Y}] = true
		if item.X == len(matrix[0])-1 && item.Y == len(matrix)-1 {
			fmt.Println(item.value)
			break
		}

		// Move right
		if item.Direction != left && item.X+1 < len(matrix[0]) && !seen[point{item.X + 1, item.Y}] {
			value := item.value + matrix[item.Y][item.X+1]
			if item.Direction == right {
				if item.Row < 3 {
					heap.Push(&pq, &Item{item.X + 1, item.Y, value, right, item.Row + 1, 0, value})
				}
			} else {
				heap.Push(&pq, &Item{item.X + 1, item.Y, value, right, 0, 0, value})
			}
		}

		// Move left
		if item.Direction != right && item.X-1 >= 0 && !seen[point{item.X - 1, item.Y}] {
			value := item.value + matrix[item.Y][item.X-1]
			if item.Direction == left {
				if item.Row < 3 {
					heap.Push(&pq, &Item{item.X - 1, item.Y, value, left, item.Row + 1, 0, value})
				}
			} else {
				heap.Push(&pq, &Item{item.X - 1, item.Y, value, left, 0, 0, value})
			}
		}

		// Move down
		if item.Direction != up && item.Y+1 < len(matrix) && !seen[point{item.X, item.Y + 1}] {
			value := item.value + matrix[item.Y+1][item.X]
			if item.Direction == down {
				if item.Row < 3 {
					heap.Push(&pq, &Item{item.X, item.Y + 1, value, down, item.Row + 1, 0, value})
				}
			} else {
				heap.Push(&pq, &Item{item.X, item.Y + 1, value, down, 0, 0, value})
			}
		}

		// Move up
		if item.Direction != down && item.Y-1 >= 0 && !seen[point{item.X, item.Y - 1}] {
			value := item.value + matrix[item.Y-1][item.X]
			if item.Direction == up {
				if item.Row < 3 {
					heap.Push(&pq, &Item{item.X, item.Y - 1, value, up, item.Row + 1, 0, value})
				}
			} else {
				heap.Push(&pq, &Item{item.X, item.Y - 1, value, up, 0, 0, value})
			}
		}
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

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the lowest, not highest, priority so we use less than here.
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value int, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}
