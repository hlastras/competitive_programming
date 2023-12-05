package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Span struct {
	Start int
	End   int
	Diff  int
}

func main() {
	lines := readFile()
	seedsNumbers := parseNumbersIntoSlice(lines[0][strings.Index(lines[0], "seeds: ")+7:])
	lines = lines[3:]
	seedSpans := make([]Span, 0)
	for i := 0; i < len(seedsNumbers); i += 2 {
		seedSpans = append(seedSpans, Span{
			Start: seedsNumbers[i],
			End:   seedsNumbers[i] + seedsNumbers[i+1] - 1,
			Diff:  0,
		})
	}

	spanGroups := make([][]Span, 0)
	currentGroup := make([]Span, 0)
	for i := 0; i < len(lines); i++ {
		if lines[i] == "" {
			// end of group
			spanGroups = append(spanGroups, currentGroup)
			currentGroup = make([]Span, 0)
			i++ // skip the tile of the group
			continue
		}
		spanDefinition := parseNumbersIntoSlice(lines[i])
		currentGroup = append(currentGroup, Span{
			Start: spanDefinition[1],
			End:   spanDefinition[1] + spanDefinition[2] - 1,
			Diff:  spanDefinition[0] - spanDefinition[1],
		})
	}
	spanGroups = append(spanGroups, currentGroup)

	for _, group := range spanGroups {
		newSeedSpans := make([]Span, 0)
		for _, seed := range seedSpans {
			for _, span := range group {
				if collides(seed, span) {
					if seed.Start >= span.Start && seed.End <= span.End {
						// seed is inside span
						newSeedSpans = append(newSeedSpans, Span{
							Start: seed.Start + span.Diff,
							End:   seed.End + span.Diff,
							Diff:  0,
						})
						seed.Start = span.End
						seed.End = span.Start
					}
					if seed.Start < span.Start && seed.End > span.End {
						// span is inside seed
						newSeedSpans = append(newSeedSpans, Span{
							Start: span.Start + span.Diff,
							End:   span.End + span.Diff,
							Diff:  0,
						})
						seed.End = span.Start - 1
						seedSpans = append(seedSpans, Span{
							Start: span.End + 1,
							End:   seed.End,
						})
					}

					if seed.Start < span.Start && seed.End <= span.End {
						// span overlaps seed end
						newSeedSpans = append(newSeedSpans, Span{
							Start: span.Start + span.Diff,
							End:   seed.End + span.Diff,
							Diff:  0,
						})
						seed.End = span.Start - 1
					}

					if seed.Start >= span.Start && seed.End > span.End {
						// span overlaps seed start
						newSeedSpans = append(newSeedSpans, Span{
							Start: seed.Start + span.Diff,
							End:   span.End + span.Diff,
							Diff:  0,
						})
						seed.Start = span.End + 1
					}
				}
			}

			// Add the seed if it is still valid
			if seed.Start <= seed.End {
				newSeedSpans = append(newSeedSpans, seed)
			}
		}
		seedSpans = newSeedSpans
	}

	// Search the min start
	m := -1
	for _, seed := range seedSpans {
		if m == -1 || seed.Start < m {
			m = seed.Start
		}
	}
	fmt.Println(m)
}

// check if two ranges overlap in some point
func collides(seed Span, transformer Span) bool {
	if seed.End >= transformer.Start && seed.Start <= transformer.End {
		return true
	}
	return false
}

func parseNumbersIntoSlice(s string) []int {
	var numbers []int
	for _, n := range strings.Split(s, " ") {
		if n == "" {
			continue
		}
		number, _ := strconv.Atoi(n)
		numbers = append(numbers, number)
	}
	return numbers
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
