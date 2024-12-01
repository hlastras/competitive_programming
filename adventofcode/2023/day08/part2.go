package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Node struct {
	Name  string
	Left  *Node
	Right *Node
}

func main() {
	lines := readFile()
	path := lines[0]
	lines = lines[2:]
	nodes := buildTree(lines)
	numbers := make([]int, 0)
	for _, node := range nodes {
		numbers = append(numbers, findCycleLength(node, path))
	}
	fmt.Println(numbers)
	fmt.Println(lcmMultiple(numbers))
}

func findCycleLength(node *Node, path string) int {
	count := 0
	idx := 0
	for {
		if path[idx] == 'L' {
			node = node.Left
		} else {
			node = node.Right
		}

		count++
		if strings.HasSuffix(node.Name, "Z") {
			break
		}
		idx = (idx + 1) % len(path)
	}
	return count
}

func buildTree(lines []string) []*Node {
	tmp := make(map[string]*Node)
	for _, line := range lines {
		var name, left, right string
		fmt.Sscanf(line, "%s = (%3s, %3s)", &name, &left, &right)
		root := createIfNoExist(tmp, name)
		root.Left = createIfNoExist(tmp, left)
		root.Right = createIfNoExist(tmp, right)
	}
	var initialNodes []*Node
	for k, v := range tmp {
		if strings.HasSuffix(k, "A") {
			initialNodes = append(initialNodes, v)
		}
	}
	return initialNodes
}

func createIfNoExist(tmp map[string]*Node, name string) *Node {
	if _, ok := tmp[name]; !ok {
		tmp[name] = &Node{Name: name}
	}
	return tmp[name]
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func lcmMultiple(numbers []int) int {
	result := numbers[0]
	for _, num := range numbers[1:] {
		result = lcm(result, num)
	}
	return result
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
