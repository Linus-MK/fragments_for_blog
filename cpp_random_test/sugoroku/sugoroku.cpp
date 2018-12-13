// sugoroku.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//

#include <iostream>

#include "header.h"

int main()
{
	Board board;
	Dice dice;

	Player PlayerA("A", board, dice);
	Player PlayerB("B", board, dice);



	while (1) {
		PlayerA.turn();
		if (PlayerA.has_ended) break;
		PlayerB.turn();
		if (PlayerB.has_ended) break;
	}

	return 0;
}

