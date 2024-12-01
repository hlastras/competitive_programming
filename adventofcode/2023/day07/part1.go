package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Hand struct {
	Value int
	Cards []int
	Bid   int
}

func main() {
	hands := make([]Hand, 0)
	for _, line := range readFile() {
		hands = append(hands, parseHand(line))
	}

	// sort
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].Value == hands[j].Value {
			for i, c := range hands[i].Cards {
				if c == hands[j].Cards[i] {
					continue
				}
				return c < hands[j].Cards[i]
			}
		}
		return hands[i].Value < hands[j].Value
	})

	total := 0
	for i, hand := range hands {
		total += hand.Bid * (i + 1)
	}
	fmt.Println(total)
}

func parseHand(line string) Hand {
	result := Hand{}
	x := strings.Split(line, " ")
	bid, _ := strconv.Atoi(x[1])
	result.Bid = bid
	cards := make([]int, 0)
	for _, c := range x[0] {
		switch c {
		case 'A':
			cards = append(cards, 14)
		case 'K':
			cards = append(cards, 13)
		case 'Q':
			cards = append(cards, 12)
		case 'J':
			cards = append(cards, 11)
		case 'T':
			cards = append(cards, 10)
		default:
			v, _ := strconv.Atoi(string(c))
			cards = append(cards, v)
		}
	}
	result.Cards = cards
	freq := sliceToFrequencyMap(cards)
	switch len(freq) {
	case 1:
		//Five of a kind
		result.Value = 7
	case 2:
		if freq[cards[0]] == 1 || freq[cards[0]] == 4 {
			//Four of a kind,
			result.Value = 6
		} else {
			//Full house
			result.Value = 5
		}
	case 3:
		three := false
		for _, v := range freq {
			if v == 3 {
				three = true
				break
			}
		}
		if three {
			//Three of a kind
			result.Value = 4
		} else {
			//Two pair
			result.Value = 3
		}
	case 4:
		//One pair
		result.Value = 2
	default:
		//High card
		result.Value = 1
	}

	return result
}

func sliceToFrequencyMap(slice []int) map[int]int {
	result := make(map[int]int)
	for _, v := range slice {
		result[v]++
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
