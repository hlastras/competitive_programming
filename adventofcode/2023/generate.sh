#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Format the directory name
dir_name=$(printf "day%02d" "$1")

# Create the directory
mkdir -p "$dir_name"

# Move to the directory
cd "$dir_name"

# Create an empty file
touch input.txt

# Common content for part1.go and part2.go
go_content='package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    for _, line := range readFile() {
        fmt.Println(line)
    }
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
'

# Create part1.go and part2.go with the specified content
echo "$go_content" > part1.go
echo "$go_content" > part2.go
