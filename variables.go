package main

import "fmt"

func main() {
	//Note to self (vars):
	// can be written as:
	Name1 := "Yug"
	var Name2 string = "Yug"

	fmt.Println(Name1)
	fmt.Println(Name2)

	//constants
	const Surname string = "Yug"

	//arrays
	var Ages [2]uint //type of array

	Ages[0] = 1 //add to an array (fixed)
	Ages[1] = 2

	//slices (better than array as length isnt fixed)
	var Names []string //type of string and length is empty

	Names = append(Names, "Yug", "John", "James")
}
