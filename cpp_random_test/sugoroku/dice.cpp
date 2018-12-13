#include <stdlib.h>
#include "header.h"
#include <time.h>

void Dice::init() {
	srand((unsigned)time(NULL));
}

int Dice::cast() {
	return rand() % 6 + 1;
}