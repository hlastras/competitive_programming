package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	matrix := readFile()
	sx, sy := searchSCoords(matrix)
	p1x, p1y, p2x, p2y := searchInitPathCoords(matrix, sx, sy)
	// coords of the previous point
	p1px := sx
	p1py := sy
	p2px := sx
	p2py := sy

	count1 := 1
	count2 := 1
	steps := make(map[int]int)
	for {
		// Move p1
		p1x, p1y, p1px, p1py = updatePath(matrix, p1y, p1x, p1py, p1px)
		count1++
		id1 := p1y*len(matrix[0]) + p1x
		if v, ok := steps[id1]; ok {
			if count1 < v {
				steps[id1] = count1
			}
			break
		} else {
			steps[id1] = count1
		}

		// Move p2
		p2x, p2y, p2px, p2py = updatePath(matrix, p2y, p2x, p2py, p2px)
		count2++
		id2 := p2y*len(matrix[0]) + p2x
		if v, ok := steps[id2]; ok {
			if count2 < v {
				steps[id2] = count2
			}
			break
		} else {
			steps[id2] = count2
		}
	}

	total := 0
	for _, v := range steps {
		if v > total {
			total = v
		}
	}
	fmt.Println(total)

}

func searchInitPathCoords(matrix []string, sx int, sy int) (int, int, int, int) {
	tmp := make([]int, 0)
	if sx+1 < len(matrix[0]) {
		if matrix[sy][sx+1] == '7' || matrix[sy][sx+1] == '-' || matrix[sy][sx+1] == 'J' {
			tmp = append(tmp, sy)
			tmp = append(tmp, sx+1)
		}
	}
	if sx-1 >= 0 {
		if matrix[sy][sx-1] == 'F' || matrix[sy][sx-1] == '-' || matrix[sy][sx-1] == 'L' {
			tmp = append(tmp, sy)
			tmp = append(tmp, sx-1)
		}
	}
	if sy+1 < len(matrix) {
		if matrix[sy+1][sx] == 'L' || matrix[sy+1][sx] == '|' || matrix[sy+1][sx] == 'J' {
			tmp = append(tmp, sy+1)
			tmp = append(tmp, sx)
		}
	}
	if sy-1 >= 0 {
		if matrix[sy-1][sx] == '7' || matrix[sy-1][sx] == '|' || matrix[sy-1][sx] == 'F' {
			tmp = append(tmp, sy-1)
			tmp = append(tmp, sx)
		}
	}
	p1x := tmp[1]
	p1y := tmp[0]
	p2x := tmp[3]
	p2y := tmp[2]
	return p1x, p1y, p2x, p2y
}

func searchSCoords(matrix []string) (int, int) {
	var sx, sy int
	for y, line := range matrix {
		for x, c := range line {
			if c == 'S' {
				sx = x
				sy = y
			}
		}
	}
	return sx, sy
}

func updatePath(matrix []string, py int, px int, ppy int, ppx int) (int, int, int, int) {
	var tmpx, tmpy int
	if matrix[py][px] == '7' {
		if py == ppy && px > ppx {
			// Enter from the left -> exit from below
			tmpx = px
			tmpy = py + 1
		} else {
			// Enter from below -> exit from left
			tmpx = px - 1
			tmpy = py
		}
	}
	if matrix[py][px] == 'F' {
		if py == ppy && px < ppx {
			// Enter from the right -> exit from below
			tmpx = px
			tmpy = py + 1
		} else {
			// Enter from below -> exit from right
			tmpx = px + 1
			tmpy = py
		}
	}
	if matrix[py][px] == 'L' {
		if py == ppy && px < ppx {
			// Enter from the right -> exit from above
			tmpx = px
			tmpy = py - 1
		} else {
			// Enter from above -> exit from right
			tmpx = px + 1
			tmpy = py
		}
	}
	if matrix[py][px] == 'J' {
		if py == ppy && px > ppx {
			// Enter from the left -> exit from above
			tmpx = px
			tmpy = py - 1
		} else {
			// Enter from above -> exit from left
			tmpx = px - 1
			tmpy = py
		}
	}
	if matrix[py][px] == '-' {
		if py == ppy && px > ppx {
			// Enter from the left -> exit from right
			tmpx = px + 1
			tmpy = py
		} else {
			// Enter from right -> exit from left
			tmpx = px - 1
			tmpy = py
		}
	}
	if matrix[py][px] == '|' {
		if py < ppy && px == ppx {
			// Enter from below -> exit from above
			tmpx = px
			tmpy = py - 1
		} else {
			// Enter from above -> exit from below
			tmpx = px
			tmpy = py + 1
		}
	}

	return tmpx, tmpy, px, py
}

func readFile() []string {
	file, err := os.Open("/Users/hector.arranz/competitive_programming/adventofcode/2023/day10/input.txt")
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
