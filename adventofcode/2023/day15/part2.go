package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Item struct {
	Label string
	Value int
	Next  *Item
}

func main() {
	commands := strings.Split(readFile()[0], ",")
	fmt.Println(len(commands))

	buckets := make([]*Item, 256)

	for _, command := range commands {
		label, value := parse(command)
		bucket := hash(label)

		if value == -1 {
			deleteLen(buckets, bucket, label)
			continue
		}
		addLen(buckets, bucket, label, value)
	}

	total := 0
	for i, item := range buckets {
		count := 0
		for item != nil {
			count++
			total += (i + 1) * count * item.Value
			item = item.Next
		}
	}
	println(total)
}

func deleteLen(buckets []*Item, bucket int, label string) {
	i := buckets[bucket]
	if i == nil {
		return
	}

	if i.Label == label {
		buckets[bucket] = i.Next
		return
	}

	for i.Next != nil {
		if i.Next.Label == label {
			i.Next = i.Next.Next
			return
		}
		i = i.Next
	}
}

func addLen(buckets []*Item, bucket int, label string, value int) {
	i := buckets[bucket]
	if i == nil {
		buckets[bucket] = &Item{label, value, nil}
		return
	}

	for i.Next != nil {
		if i.Label == label {
			i.Value = value
			return
		}
		i = i.Next
	}

	if i.Label == label {
		i.Value = value
		return
	}

	i.Next = &Item{label, value, nil}
}

func parse(command string) (string, int) {
	idx := strings.Index(command, "=")
	if idx == -1 {
		return command[:len(command)-1], -1
	}
	label := command[:idx]
	value, _ := strconv.Atoi(command[idx+1:])
	return label, value
}

func hash(command string) int {
	total := 0
	for _, c := range command {
		total += int(c)
		total *= 17
		total %= 256
	}
	return total
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
