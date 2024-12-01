package main

import (
	"bufio"
	"container/heap"
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

type bestItem struct {
	value     int
	direction int
	row       int
}

const up = 0
const down = 1
const left = 2
const right = 3

//func add(pq *PriorityQueue, item *Item, seen map[point]bool) {
//	if !seen[point{item.X, item.Y}] {
//		heap.Push(pq, item)
//		seen[point{item.X, item.Y}] = true
//	}
//}

func add(queue []*Item, item *Item, seen map[point]int) []*Item {
	if v, ok := seen[point{item.X, item.Y}]; !ok || v > item.value {
		queue = append(queue, item)
		seen[point{item.X, item.Y}] = item.value
		sort.Slice(queue, func(i, j int) bool {
			return queue[i].value < queue[j].value
		})
	}
	return queue
}

//func add(pq *PriorityQueue, item *Item, best map[point][4]*Item) {
//	b := best[point{item.X, item.Y}]
//	if b[item.Direction] == nil {
//		heap.Push(pq, item)
//		b[item.Direction] = item
//	}
//
//	// If on the direction, value is less, or row is less
//	if item.value < b[item.Direction].value {
//		heap.Push(pq, item)
//	}
//
//	//	Only if value is less we update
//	if item.value < b[item.Direction].value {
//		b[item.Direction] = item
//	}
//}

//func add(pq *PriorityQueue, item *Item, best map[point][4]*Item) {
//	b := best[point{item.X, item.Y}]
//	if b[item.Direction] == nil {
//		heap.Push(pq, item)
//		b[item.Direction] = item
//		best[point{item.X, item.Y}] = b
//		return
//	}
//
//	// If on the direction, value is less, or row is less
//	if item.value <= b[item.Direction].value || item.Row < b[item.Direction].Row {
//		heap.Push(pq, item)
//	}
//
//	//	Only if value is less we update
//	if item.value < b[item.Direction].value || (item.value == b[item.Direction].value && item.Row < b[item.Direction].Row) {
//		b[item.Direction] = item
//		best[point{item.X, item.Y}] = b
//	}
//}

//func add(pq *PriorityQueue, item *Item, best map[point][4]*Item) {
//	heap.Push(pq, item)
//}

func main() {
	matrix := parse(readFile())
	//pq := make(PriorityQueue, 0)
	pq := make([]*Item, 0, 1000000)
	best := make(map[point]int)

	//heap.Init(&pq)
	//heap.Push(&pq, &Item{0, 0, 0, right, 0, 0, 0})
	pq = add(pq, &Item{0, 0, 0, right, 0, 0, 0}, best)

	for {
		fmt.Println(len(pq))
		if len(pq) == 0 {
			break
		}
		//item := heap.Pop(&pq).(*Item)
		item := pq[0]
		pq = pq[1:]
		//if item.X == 12 && item.Y > 6 {
		//	fmt.Println(item)
		//}
		//fmt.Println(item.X, item.Y, item)
		if item.X == len(matrix[0])-1 && item.Y == len(matrix)-1 {
			fmt.Println(item.value)
			break
		}

		// Move right
		if item.Direction != left && item.X+1 < len(matrix[0]) {
			value := item.value + matrix[item.Y][item.X+1]
			if item.Direction == right {
				if item.Row < 3 {
					pq = add(pq, &Item{item.X + 1, item.Y, value, right, item.Row + 1, 0, value}, best)
				}
			} else {
				pq = add(pq, &Item{item.X + 1, item.Y, value, right, 0, 0, value}, best)
			}
		}

		// Move left
		if item.Direction != right && item.X-1 >= 0 {
			value := item.value + matrix[item.Y][item.X-1]
			if item.Direction == left {
				if item.Row < 3 {
					pq = add(pq, &Item{item.X - 1, item.Y, value, left, item.Row + 1, 0, value}, best)
				}
			} else {
				pq = add(pq, &Item{item.X - 1, item.Y, value, left, 0, 0, value}, best)
			}
		}

		// Move down
		if item.Direction != up && item.Y+1 < len(matrix) {
			value := item.value + matrix[item.Y+1][item.X]
			if item.Direction == down {
				if item.Row < 3 {
					pq = add(pq, &Item{item.X, item.Y + 1, value, down, item.Row + 1, 0, value}, best)
				}
			} else {
				pq = add(pq, &Item{item.X, item.Y + 1, value, down, 0, 0, value}, best)
			}
		}

		// Move up
		if item.Direction != down && item.Y-1 >= 0 {
			value := item.value + matrix[item.Y-1][item.X]
			if item.Direction == up {
				if item.Row < 3 {
					pq = add(pq, &Item{item.X, item.Y - 1, value, up, item.Row + 1, 0, value}, best)
				}
			} else {
				pq = add(pq, &Item{item.X, item.Y - 1, value, up, 0, 0, value}, best)
			}
		}
	}
	fmt.Println(best[point{len(matrix[0]) - 1, len(matrix) - 1}])
	//fmt.Println(cal(best[point{0, 0}]))
	//fmt.Println(cal(best[point{1, 0}]))
	//fmt.Println(cal(best[point{2, 0}]))
	//fmt.Println(cal(best[point{2, 1}]))
	//fmt.Println(cal(best[point{3, 1}]))
	//fmt.Println(cal(best[point{4, 1}]))
	//fmt.Println(cal(best[point{5, 1}]))
	//fmt.Println(cal(best[point{5, 0}]))
	//fmt.Println(cal(best[point{6, 0}]))
	//fmt.Println(cal(best[point{7, 0}]))
	//fmt.Println(cal(best[point{8, 0}]))
	//fmt.Println(cal(best[point{8, 1}]))
	//fmt.Println(cal(best[point{8, 2}]))
	//fmt.Println(cal(best[point{9, 2}]))
	//fmt.Println(cal(best[point{10, 2}]))
	//fmt.Println(cal(best[point{10, 3}]))
	//fmt.Println(cal(best[point{10, 4}]))
	//fmt.Println(cal(best[point{11, 4}]))
	//fmt.Println(cal(best[point{11, 5}]))
	//fmt.Println(cal(best[point{11, 6}]))
	//fmt.Println(cal(best[point{11, 7}]))
	//fmt.Println(cal(best[point{12, 7}]))
	//fmt.Println(cal(best[point{12, 8}]))
	//fmt.Println(cal(best[point{12, 9}]))
	//fmt.Println(cal(best[point{12, 10}]))
	//fmt.Println(cal(best[point{11, 10}]))
	//fmt.Println(cal(best[point{11, 11}]))
	//fmt.Println(cal(best[point{11, 12}]))
	//fmt.Println(cal(best[point{12, 12}]))

}

//0
//4
//5
//6
//11
//15
//20
//23
//25
//28
//29
//32
//37
//41
//43
//47
//52
//55
//60
//66
//71
//74
//81
//84
//87
//93
//96
//99
//102

func cal(x [4]*Item) Item {
	//find the item with the lowest value (be careful, item could be null)
	var lowest *Item
	for _, item := range x {
		if item != nil {
			if lowest == nil {
				lowest = item
			} else {
				if item.value < lowest.value {
					lowest = item
				}
			}
		}
	}
	return *lowest
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
