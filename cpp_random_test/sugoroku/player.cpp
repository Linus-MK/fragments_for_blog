
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

	std::cout << name << "�����" << num << "���o���̂ŁA" << position <<"�ɐi�݂܂���\n";

	if (board->HasEffect(position)) {
		board->ApplyEffect(this);
		std::cout << name << "�����" << "�Ֆʂ̌��ʂɂ��A" << position << "�Ɉړ����܂���\n";
	}
	if (position >= board->goal_position) {
		std::cout << name << "����̏����ł�\n";
		has_ended = true;
	}
	
	if (1)3;

	return 0;
}
