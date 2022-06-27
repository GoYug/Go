package main

import "fmt"

func main() {
	var conferenceName = "Go Conference"
	const conferenceTickets int = 50
	var remainingTickets uint = 50

	fmt.Printf("conferenceTickets is %T, remainingTickets is %T, conferenceName is %T\n", conferenceTickets, remainingTickets, conferenceName)

	fmt.Printf("Welcome to %v booking application\n", conferenceName)
	fmt.Printf("We have total of %v tickets and %v tickets are still available\n", conferenceTickets, remainingTickets)
	fmt.Println("Get your tickets to attend here")

	//arrays
	//var bookings [50]string

	//slices
	var bookings []string

	//variables
	var firstName string
	var lastName string
	var email string

	//uint means positive vals only!
	var userTickets uint

	//ask user for their name
	fmt.Println("Enter Your First Name:")
	fmt.Scan(&firstName)

	//last name
	fmt.Println("Enter Your Last Name:")
	fmt.Scan(&lastName)

	//email
	fmt.Println("Enter Your email address:")
	fmt.Scan(&email)

	//nr of tickets
	fmt.Println("Enter the nr of tickets:")
	fmt.Scan(&userTickets)

	//rem tcikets
	remainingTickets = remainingTickets - userTickets

	//add to arr
	//bookings[0] = firstName + " " + lastName

	bookings = append(bookings, firstName+" "+lastName)

	fmt.Printf("Thank you %v %v for booking %v tickets. You will recieve a confimation email at %v\n", firstName, lastName, userTickets, email)
	fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceName)

	fmt.Printf("These are all our bookings: %v\n", bookings)
}
