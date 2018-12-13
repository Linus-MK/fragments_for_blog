#pragma once
#include <iostream>
#include <string>

class Player;

class Dice {
public:
	void init();
	int cast();
	Dice() { init(); }

};

class Board {
public:
	Board();
	bool HasEffect(int position);
	int ApplyEffect(Player * p);

	int goal_position;
};



class Player {
public:
	int position;
	std::string name;
	Board * board;
	Dice * dice;
	bool has_ended;

	Player(std::string n, Board& board_, Dice& dice_);

	int turn();
};


