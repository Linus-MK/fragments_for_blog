#include <stdlib.h>
#include "header.h"
#include <time.h>

Dice::Dice():
	engine(seed_gen()),
	dist1(1,6)
{
}

void Dice::init() {
}

int Dice::cast() {

	return dist1(engine);
}