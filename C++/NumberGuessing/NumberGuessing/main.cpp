#include<iostream>
#include<string>
#include<time.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

//Define functions
void settings();
void game();


//Variables
int low = 0;
int high = 0;
int tries = 0;
bool found = false;
bool win = false;
int number = 0;
int rand_number = 0;
string Break = "";
int i = 0;

//Main
int main()
{
	//Intro
	cout << "Welcome to Numberguessing" << endl;
	//Get the game settings from the Player
	settings();
	srand (time_t(NULL));
	rand_number = rand() % high + low;
	game();
	getline(cin, Break);
	return 0;
}

//Ask the settings
void settings() {
	cout << "Set the range:" << endl << "Lowest possible number: ";
	cin >> low;
	cout << endl << "Highest possible number: ";
	cin >> high;
	cout << endl << "Tries: ";
	cin >> tries;
	return;
}
//The game
void game() {
	for (int count = 0; count <= tries; count++) {
		cout << "Hallo" << endl;
		//Ask for an input
		cout << "Guess a number: ";
		cin >> number;
		//Check is it the righ number
		if (number = rand_number) {
			found = true;
			win = true;
			cout << "You have won!" << endl;
		}
		//Have you enough tries left
		if (tries = 0) {
			found = true;
			cout << "You have no tries left." << endl;
		}
		//Remove a try
		tries = tries - 1;
	}
	return;
}
