#pragma once
#include <iostream>
#include <string>
#include <random>

class Player;

class Dice {
public:
	void init();
	int cast();
	Dice() { init(); }

	std::random_device seed_gen;
	std::default_random_engine engine{ seed_gen() };
	std::uniform_int_distribution<> dist1{1,6};
};

class Board {
public:
	Dice * dice;

	Board(Dice& dice_);
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


