
#include "header.h"

Player::Player(std::string n, Board& board_, Dice& dice_){
	position = 0;
	name = n;
	board = &board_;
	dice = &dice_;
	has_ended = false;
}

int Player::turn()
{
	int num = dice->cast();
	
	position += num;

	std::cout << name << "さんは" << num << "が出たので、" << position <<"に進みました\n";

	if (board->HasEffect(position)) {
		board->ApplyEffect(this);
		std::cout << name << "さんは" << "盤面の効果により、" << position << "に移動しました\n";
	}
	if (position >= board->goal_position) {
		std::cout << name << "さんの勝ちです\n";
		has_ended = true;
	}
	
	if (1)3;

	return 0;
}
