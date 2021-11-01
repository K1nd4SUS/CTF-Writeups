package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Pezzo struct {
	up int
	down int
	left int
	right int
	letter string
}

func main(){
	log.Println("Inizio programma")
	pezzi := make([]Pezzo, 40000)
	f, err := os.Open("puzzle.txt")
	check(err)
    scanner := bufio.NewScanner(f)
	var k int = 0
    for scanner.Scan() {
		split := strings.Split(scanner.Text(), " ")
		up,_ := strconv.Atoi(split[0])
		down,_ := strconv.Atoi(split[1])
		left,_ := strconv.Atoi(split[2])
		right,_ := strconv.Atoi(split[3])
		pezzi[k] = Pezzo{up, down, left, right, split[4]}
	  	k ++
    }
	fmt.Printf("%v pezzi caricati in memoria!\n", len(pezzi))

	var pezzoIniziale Pezzo

	for k := 0; k < len(pezzi); k++{
		up := 0
		left := 0
		for i := 0; i < len(pezzi); i++{
			if (pezzi[k].up == pezzi[i].down){
				up++
			}
			if (pezzi[k].left == pezzi[i].right){
				left++
			}
		} 
		if (up == 0 && left == 0){
			pezzoIniziale = pezzi[k]
			pezzi[k] = pezzi[k-1]
			pezzi = pezzi[:len(pezzi)-1]
		}
	}
	fmt.Printf("Pezzo iniziale -> %v\n", pezzoIniziale)

	//costruisco il puzzle
	for y := 0; y < 200; y++{
		pezzoIniziale, pezzi = trovaPrimoPezzo(y, pezzoIniziale, pezzi)
		pezzoInizialeTemp := pezzoIniziale
		for x := 0; x < 199; x++{
			for elem := 0; elem < len(pezzi); elem++{
				if(pezzoInizialeTemp.right == pezzi[elem].left){
					if(pezzi[elem].letter != ""){
						fmt.Printf("%v", pezzi[elem].letter)
					}
					pezzoInizialeTemp = pezzi[elem]
					pezzi[elem] = pezzi[len(pezzi)-1]
					pezzi = pezzi[:len(pezzi)-1]
					break
				}
			}
		}
	}
	
	fmt.Println("")
	log.Println("Fine")
}

func trovaPrimoPezzo(y int, pezzoIniziale Pezzo, pezzi []Pezzo) (Pezzo, []Pezzo){
	if(y == 0){
		return pezzoIniziale, pezzi
	}
	var pezzoDaRitornare Pezzo
	for k := 0; k < len(pezzi); k++{
		if(pezzoIniziale.down == pezzi[k].up){
			pezzoDaRitornare = pezzi[k]
			pezzi[k] = pezzi[len(pezzi)-1]
		}
	}
	return pezzoDaRitornare, pezzi[:len(pezzi)-1]
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}
