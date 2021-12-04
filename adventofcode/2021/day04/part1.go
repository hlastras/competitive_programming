package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type board struct {
	matrix map[int][2]int
	total  int
	x, y   int
	col    [5]int
	row    [5]int
}

func newBoard() board {
	var b board
	b.matrix = make(map[int][2]int)
	return b
}

func (b *board) add(i int) {
	b.matrix[i] = [2]int{b.x, b.y}
	b.total += i
	b.col[b.x]++
	b.row[b.y]++
	b.x++
	if b.x == 5 {
		b.x = 0
		b.y++
	}
}

func (b *board) see(i int) (bool, int) {
	v, present := b.matrix[i]
	if present {
		b.total -= i
		b.col[v[0]]--
		if b.col[v[0]] == 0 {
			return true, b.total * i
		}
		b.row[v[1]]--
		if b.row[v[1]] == 0 {
			return true, b.total * i
		}
	}
	return false, 0
}

func parse_numbers(s string) []int {
	values := strings.Split(s, ",")
	var result []int
	for _, v := range values {
		number, _ := strconv.Atoi(v)
		result = append(result, number)
	}
	return result
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	scanner.Scan()
	numbers := parse_numbers(scanner.Text())

	var boards []*board

	for scanner.Scan() {
		// Discard first line
		_ = scanner.Text()

		bo := newBoard()
		for i := 0; i < 5; i++ {
			scanner.Scan()
			var a, b, c, d, e int
			_, err := fmt.Sscanf(scanner.Text(), "%d %d %d %d %d", &a, &b, &c, &d, &e)
			if err != nil {
				// log.Fatal(err)
				fmt.Println(err)
			}
			bo.add(a)
			bo.add(b)
			bo.add(c)
			bo.add(d)
			bo.add(e)
		}
		boards = append(boards, &bo)
	}

	for _, n := range numbers {
		for _, b := range boards {
			finish, score := b.see(n)
			if finish {
				fmt.Println(score)
				return
			}
		}
	}
}
