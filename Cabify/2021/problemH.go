package main

import "fmt"

func main() {
	var c int
	fmt.Scanf("%d", &c)
	n := make([]int, c)
	for i := range n {
		fmt.Scanf("%d", &n[i])
	}

	s := make(map[int]bool)

	for {
		found := false

		max := n[0]
		for i := 1; i < len(n); i++ {
			if max < n[i] {
				max = n[i]
			}
		}

		for v := 2; v <= max; v++ {
			allEq := true
			x := n[0] % v
			for _, j := range n {
				if j%v != x {
					allEq = false
					break
				}
			}

			if allEq {
				found = true
				news := make([]int, 0)
				for k := range s {
					news = append(news, k*v)
				}
				for _, h := range news {
					s[h] = true
				}
				s[v] = true

				for h := range n {
					n[h] /= v
				}
				break
			}
		}

		if !found {
			break
		}
	}
	f := true
	for k := range s {
		if !f {
			fmt.Print(" ")
		}
		fmt.Print(k)
		f = false
	}
	fmt.Println("")
}
