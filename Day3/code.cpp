#include <iostream>
#include <cmath>


float hight_g = 0;
float speed_g = 0;
float mas = 0;
float time_g = 0;
struct spisok_ball* glav_ptr;

struct spisok_ball {
	float speed = 0;
    float hight = 0;
	float time = 0;

	struct spisok_ball* next = NULL;
};

void add_spisok(float& speed_r, float& hight_r, float& time_r) {

	spisok_ball* new_result;
	new_result = new spisok_ball;
	new_result->speed = speed_r;
	new_result->hight = hight_r;
	new_result->time = time_r;

	if (glav_ptr == NULL) glav_ptr = new_result;

	else {
		spisok_ball* cur = glav_ptr;
		while (cur->next != NULL) {
			cur = cur->next;
		}

		cur->next = new_result;
	}
}

void time_all_chaeck() {

	if (speed_g > 0 && hight_g != 0 ) {

		float disk = (speed_g * speed_g) + (2 * 9.8 * hight_g);
		time_g = (((sqrt(disk)) - speed_g) / 9.8);

	}
	else if ((speed_g == 0) && (hight_g != 0)) {
		time_g = sqrt(hight_g / 4.9);
	}
}

void physic_f(float time) {

	float speed = speed_g + 9.8 * time;
	float hight = hight_g - (speed_g * time) - time * time * 4.9;
	std::cout << "Speed " << speed << " " << "Hight " << hight;
	
	add_spisok(speed, hight, time);
}

void test_time_all_chaeck() {
     //До этого руки не дошли
}

int main() {
	setlocale(LC_ALL, "Russian");

	std::cout << "Ведите высоту, начальную скорость и массу в единицах измерениях СИ " << '\n';
	std::cin >> hight_g >> speed_g >> mas;
	time_all_chaeck();
	std::cout << time_g;

	while(true){
		float time_cheack;
		std::cout << '\n' << "new time: ";
		std::cin >> time_cheack;

		if (time_cheack <= time_g && time_cheack > 0)  physic_f(time_cheack);
		
	}
	return 0;
}