package main

import (
	"os"
	"encoding/csv"
	"math/rand/v2"
	"strconv"
)


func fisherYates(arr []int){
	for i:=len(arr)-1; i>0; i--{
		j:=rand.IntN(i+1) //Random integer in [0,i]
		arr[i], arr[j] = arr[j], arr[i]
	}
}


func main(){
	var arrLen int = 52
	var reps int = 1000000
	arr := make([]int, arrLen)
	stringForm := make([]string, arrLen)

	f, _ := os.Create("results.csv")
	writer := csv.NewWriter(f)
	defer f.Close()
	defer writer.Flush()

	for deck:=0;deck<reps;deck++{
		for i:=1; i<=arrLen; i++{
			arr[i-1]=i //Set the deck to an ordered deck of cards
		}

		fisherYates(arr) //Shuffle

		for index, value := range arr{
			stringForm[index] = strconv.Itoa(value)
		}

		writer.Write(stringForm)
	}
}
