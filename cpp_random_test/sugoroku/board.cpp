#include "header.h"

Board::Board() {
	goal_position = 30;
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
		p->position += 3;
	}else if (p->position % 10 == 7) {
		p->position -= 3;
	}

	return 0;
}
