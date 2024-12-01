package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	root := buildTree(lines)
	count := 0
	idx := 0
	for {
		if path[idx] == 'L' {
			root = root.Left
		} else {
			root = root.Right
		}
		count++
		if root.Name == "ZZZ" {
			break
		}
		idx = (idx + 1) % len(path)
	}
	fmt.Println(count)
}

func buildTree(lines []string) *Node {
	tmp := make(map[string]*Node)
	for _, line := range lines {
		var name, left, right string
		fmt.Sscanf(line, "%s = (%3s, %3s)", &name, &left, &right)
		root := createIfNoExist(tmp, name)
		root.Left = createIfNoExist(tmp, left)
		root.Right = createIfNoExist(tmp, right)
	}
	return tmp["AAA"]
}

func createIfNoExist(tmp map[string]*Node, name string) *Node {
	if _, ok := tmp[name]; !ok {
		tmp[name] = &Node{Name: name}
	}
	return tmp[name]
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
