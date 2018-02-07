#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

//Define functions
void settings();

//Variables
int low = 0;
int high = 0;
int tries = 0;
int found = 0;
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
	srand (time(NULL));
	rand_number = rand() % 99 + 1;
	cout << "Random number = " << rand_number;
	cin >> Break;
	return 0;
}

//Asks the settings
void settings() {
	cout << "Set the range:" << endl << "Lowest possible number: ";
	cin >> low;
	cout << endl << "Highest possible number: ";
	cin >> high;
	cout << endl << "Tries: ";
	cin >> tries;
	return;
}

void Game() {
	do {
		cout << "Guess a number: ";
		cin >> number;

	} while (found == 0);
}
