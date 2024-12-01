package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

const up = 1
const down = 2
const left = 3
const right = 4

type pointer struct {
	X         int
	Y         int
	Direction int
}

func main() {
	matrix := readFile()

	total := 0
	for x := 0; x < len(matrix[0]); x++ {
		pointers := []*pointer{{X: x, Y: 0, Direction: down}}
		x := solve(pointers, matrix)
		total = max(total, x)

		pointers = []*pointer{{X: x, Y: len(matrix) - 1, Direction: up}}
		x = solve(pointers, matrix)
		total = max(total, x)
	}

	for y := 0; y < len(matrix); y++ {
		pointers := []*pointer{{X: 0, Y: y, Direction: right}}
		x := solve(pointers, matrix)
		total = max(total, x)

		pointers = []*pointer{{X: len(matrix[0]) - 1, Y: y, Direction: left}}
		x = solve(pointers, matrix)
		total = max(total, x)
	}
	fmt.Println(total)
}

func solve(pointers []*pointer, matrix []string) int {
	anyMove := false
	seen := make(map[int]map[int]bool)
	for {
		newPointers := []*pointer{}
		for _, pointer := range pointers {
			moved, splited := move(pointer, matrix, seen)
			anyMove = anyMove || moved
			if splited != nil {
				newPointers = append(newPointers, splited)
			}
		}
		pointers = append(pointers, newPointers...)

		if !anyMove {
			break
		}
		anyMove = false
	}
	return len(seen)
}

func move(p *pointer, matrix []string, seen map[int]map[int]bool) (bool, *pointer) {
	if seen[p.Y*len(matrix[0])+p.X][p.Direction] {
		return false, nil
	}
	if p.X < 0 || p.X >= len(matrix[0]) || p.Y < 0 || p.Y >= len(matrix) {
		// Cant move
		return false, nil
	}
	if seen[p.Y*len(matrix[0])+p.X] == nil {
		seen[p.Y*len(matrix[0])+p.X] = make(map[int]bool)
	}
	seen[p.Y*len(matrix[0])+p.X][p.Direction] = true
	if matrix[p.Y][p.X] == '.' {
		nX, nY := nextPoint(p.X, p.Y, p.Direction)
		p.X = nX
		p.Y = nY
		return true, nil
	}

	if matrix[p.Y][p.X] == '/' || matrix[p.Y][p.X] == '\\' {
		nX, nY, nD := nextPointMirror(p.X, p.Y, p.Direction, matrix[p.Y][p.X])
		p.X = nX
		p.Y = nY
		p.Direction = nD
		return true, nil
	}

	if matrix[p.Y][p.X] == '-' || matrix[p.Y][p.X] == '|' {
		nX, nY, nD, nnX, nnY, nnD := nextPointSplit(p.X, p.Y, p.Direction, matrix[p.Y][p.X])

		var newPointer *pointer = nil

		if nnD != -10 {
			newPointer = &pointer{X: nnX, Y: nnY, Direction: nnD}
		}

		p.X = nX
		p.Y = nY
		p.Direction = nD
		return true, newPointer
	}
	return false, nil
}

func nextPointSplit(x int, y int, direction int, u uint8) (int, int, int, int, int, int) {
	switch direction {
	case up:
		if u == '|' {
			return x, y - 1, direction, -10, -10, -10
		}
		return x - 1, y, left, x + 1, y, right
	case down:
		if u == '|' {
			return x, y + 1, direction, -10, -10, -10
		}
		return x - 1, y, left, x + 1, y, right
	case left:
		if u == '-' {
			return x - 1, y, direction, -10, -10, -10
		}
		return x, y - 1, up, x, y + 1, down
	case right:
		if u == '-' {
			return x + 1, y, direction, -10, -10, -10
		}
		return x, y - 1, up, x, y + 1, down
	}
	return -10, -10, -10, -10, -10, -10
}

func nextPointMirror(x int, y int, direction int, u uint8) (int, int, int) {
	switch direction {
	case up:
		if u == '/' {
			return x + 1, y, right
		}
		return x - 1, y, left
	case down:
		if u == '/' {
			return x - 1, y, left
		}
		return x + 1, y, right
	case left:
		if u == '/' {
			return x, y + 1, down
		}
		return x, y - 1, up
	case right:
		if u == '/' {
			return x, y - 1, up
		}
		return x, y + 1, down
	}
	return x, y, direction
}

func nextPoint(x int, y int, direction int) (int, int) {
	switch direction {
	case up:
		return x, y - 1
	case down:
		return x, y + 1
	case left:
		return x - 1, y
	case right:
		return x + 1, y
	}
	return x, y
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
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
