#include <stdlib.h>
#include "header.h"
#include <time.h>

void Dice::init() {
}

int Dice::cast() {

	return dist1(engine);
}