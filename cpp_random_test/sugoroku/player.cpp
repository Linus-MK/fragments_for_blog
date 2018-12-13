
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

	if (position >= board->goal_position) {
		std::cout << name << "さんの勝ちです\n";
		has_ended = true;
	}

	if (board->HasEffect(position)) {
		board->ApplyEffect(this);
	}
	// 改めてゴール判定はしない：3マス進んでゴールに行くことは無いことを暗黙裏に仮定
	// 改めて効果判定はしない：効果マスで進んだり戻ったりした先が効果マスでないことを暗黙裏に仮定

	return 0;
}
