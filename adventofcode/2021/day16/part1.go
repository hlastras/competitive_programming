package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Packet struct {
	version int
	typeID  int
	packets []Packet
	value   int
}

func binToInt(s string) int {
	value, _ := strconv.ParseInt(s, 2, 64)
	return int(value)
}

func parse(messageBin string) (int, Packet) {
	version := binToInt(messageBin[:3])
	typeID := binToInt(messageBin[3:6])

	if typeID == 4 {
		// Literal value
		bitsReaded := 6
		valueBin := ""
		for i := 6; i < len(messageBin); i += 5 {
			chunk := messageBin[i : i+5]
			valueBin += chunk[1:]
			bitsReaded += 5
			if chunk[0:1] == "0" {
				break
			}
		}
		value := binToInt(valueBin)
		return bitsReaded, Packet{version: version, typeID: typeID, value: value}
	} else {
		// Operator
		if messageBin[6:7] == "1" {
			// next 11 bits are a number that represents the number of sub-packets immediately contained
			numberPackets := binToInt(messageBin[7:18])
			var packets []Packet
			i := 18
			for x := 0; x < numberPackets; x++ {
				readed, packet := parse(messageBin[i:])
				packets = append(packets, packet)
				i += readed
			}
			return i, Packet{version: version, typeID: typeID, packets: packets}
		} else {
			// next 15 bits are a number that represents the total length in bits
			length := binToInt(messageBin[7:22])
			i := 22
			var packets []Packet
			for i-22 < length {
				readed, packet := parse(messageBin[i:])
				packets = append(packets, packet)
				i += readed
			}

			return i, Packet{version: version, typeID: typeID, packets: packets}
		}
	}
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	hexValues := map[string]string{
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"A": "1010",
		"B": "1011",
		"C": "1100",
		"D": "1101",
		"E": "1110",
		"F": "1111",
	}

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	messageHex := scanner.Text()
	messageBin := ""
	for _, c := range strings.Split(messageHex, "") {
		messageBin += hexValues[c]
	}

	_, p := parse(messageBin)

	queue := []Packet{p}
	total := 0
	for len(queue) > 0 {
		x := queue[0]
		queue = queue[1:]
		total += x.version
		queue = append(queue, x.packets...)
	}
	fmt.Println(total)
}
