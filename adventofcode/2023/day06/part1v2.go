package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	} else {
		defer readFile.Close()
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	speed_distance := make([][2]int, 0)
	fileScanner.Scan()
	line_1 := strings.Split(fileScanner.Text(), ":")[1]
	fileScanner.Scan()
	line_2 := strings.Split(fileScanner.Text(), ":")[1]
	numbers_line1 := getNumbersFromStr(line_1)
	numbers_line2 := getNumbersFromStr(line_2)

	for i := 0; i < len(numbers_line1); i++ {
		tmp := [2]int{numbers_line1[i], numbers_line2[i]}
		speed_distance = append(speed_distance, tmp)
	}
	fmt.Println(speed_distance)

	// We have to find the number of combinations of two numbers where added are exactly one amount, and multiplied are more than a quantity
	total := 1
	for _, race := range speed_distance {
		combinations := getNumberOfCombinations(race)
		fmt.Println("race: ", race, " combinations: ", combinations)
		total *= combinations
	}
	fmt.Println("total: ", total)
}

func getNumberOfCombinations(input [2]int) int {
	ret := 0
	for x := 1; x <= input[0]/2; x++ {
		y := input[0] - x
		if x*y > input[1] {
			// fmt.Println("x: ", x, " y: ", y, " yes")
			ret++
		} else {
			// fmt.Println("x: ", x, " y: ", y, " no")
		}
	}

	if input[0]%2 == 0 {
		return ret*2 - 1
	} else {
		return ret * 2
	}
}

func getNumbersFromStr(s string) []int {
	numbers := make([]int, 0)
	var number_s string
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			number_s = number_s + string(s[i])
		}
	}
	if len(number_s) > 0 {
		n, _ := strconv.Atoi(number_s)
		numbers = append(numbers, n)
	}
	return numbers
}
