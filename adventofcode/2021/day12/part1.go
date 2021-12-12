package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"unicode"
)

func isLower(s string) bool {
	for _, r := range s {
		if !unicode.IsLower(r) && unicode.IsLetter(r) {
			return false
		}
	}
	return true
}

func explore(graph map[string][]string, path []string, visited map[string]bool, seen int) int {
	if path[len(path)-1] == "end" {
		return seen + 1
	}

	for _, next := range graph[path[len(path)-1]] {
		if !visited[next] {
			if isLower(next) {
				visited[next] = true
			}

			path = append(path, next)
			seen = explore(graph, path, visited, seen)
			path = path[:len(path)-1]

			if isLower(next) {
				visited[next] = false
			}
		}
	}

	return seen
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	graph := make(map[string][]string)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "-")
		if line[0] != "end" && line[1] != "start" {
			graph[line[0]] = append(graph[line[0]], line[1])
		}

		if line[1] != "end" && line[0] != "start" {
			graph[line[1]] = append(graph[line[1]], line[0])
		}
	}
	fmt.Println(explore(graph, []string{"start"}, make(map[string]bool), 0))
}
