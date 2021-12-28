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

func calculateValue(typeID int, packets []Packet) int {
	var values []int
	for _, p := range packets {
		values = append(values, p.value)
	}

	var total int
	switch typeID {
	case 0:
		// Sum
		total = 0
		for _, v := range values {
			total += v
		}
	case 1:
		// Product
		total = 1
		for _, v := range values {
			total *= v
		}
	case 2:
		// Minimum
		total = -1
		for _, v := range values {
			if total == -1 || v < total {
				total = v
			}
		}
	case 3:
		// Maximum
		total = -1
		for _, v := range values {
			if v > total {
				total = v
			}
		}
	case 5:
		// Greater than
		if values[0] > values[1] {
			total = 1
		} else {
			total = 0
		}
	case 6:
		// Less than
		if values[0] < values[1] {
			total = 1
		} else {
			total = 0
		}
	case 7:
		// Equal to
		if values[0] == values[1] {
			total = 1
		} else {
			total = 0
		}
	}

	return total
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
			value := calculateValue(typeID, packets)
			return i, Packet{version: version, typeID: typeID, packets: packets, value: value}
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
			value := calculateValue(typeID, packets)
			return i, Packet{version: version, typeID: typeID, packets: packets, value: value}
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

	fmt.Println(p.value)
}
