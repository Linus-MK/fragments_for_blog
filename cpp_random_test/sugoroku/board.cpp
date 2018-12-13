#include "header.h"

Board::Board(Dice & dice_) {
	goal_position = 30;
	dice = &dice_;
}


bool Board::HasEffect(int position)
{
	if (position % 10 == 2 or position % 10 == 7) {
		return true;
	}
	return false;
}

int Board::ApplyEffect(Player * p)
{
	if (p->position % 10 == 2) {
		int num = dice->cast();
		if (num >= 4) {
			p->position += 3;
			std::cout << num << "���o���̂ŁA" << p->name << "�����" << "�Ֆʂ̌��ʂɂ��A"
				<< p->position << "�ɐi�݂܂���\n";
		} else {
			std::cout << num << "���o���̂ŁA�����܂���\n";
		}

	}else if (p->position % 10 == 7) {
		int num = dice->cast();
		if (num >= 4) {
			p->position -= 3;
			std::cout << num << "���o���̂ŁA" << p->name << "�����" << "�Ֆʂ̌��ʂɂ��A"
				<< p->position << "�ɖ߂�܂���\n";
		} else {
			std::cout << num << "���o���̂ŁA�����܂���\n";
		}
	}

	return 0;
}
