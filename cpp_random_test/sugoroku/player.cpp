
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

	if (position >= board->goal_position) {
		std::cout << name << "����̏����ł�\n";
		has_ended = true;
	}

	if (board->HasEffect(position)) {
		board->ApplyEffect(this);
	}
	// ���߂ăS�[������͂��Ȃ��F3�}�X�i��ŃS�[���ɍs�����Ƃ͖������Ƃ��Öٗ��ɉ���
	// ���߂Č��ʔ���͂��Ȃ��F���ʃ}�X�Ői�񂾂�߂����肵���悪���ʃ}�X�łȂ����Ƃ��Öٗ��ɉ���

	return 0;
}
