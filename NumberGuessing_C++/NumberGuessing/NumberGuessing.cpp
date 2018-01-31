// NumberGuessing.cpp : Defines the entry point for the console application.
//

#include"stdafx.h"
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

//Main
int main()
{
	//Intro
	cout << "Welcome to Numberguessing" <<endl;
	//Get the game settings from the Player
	settings();
	//rand_number = rand() % low + (high - low + 1);
	rand_number = rand() % 10 + 1;
	cout << rand_number << endl << "= randdom";
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

