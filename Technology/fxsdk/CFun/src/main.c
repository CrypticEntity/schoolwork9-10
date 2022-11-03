#include <gint/display.h>
#include <gint/keyboard.h>
//screen size is 384 x 216/32 x 18
struct screen
{
    int x;
    int y;
    char entity;
};

typedef struct screen point;

void updateScreen(point points [512])
{
    dclear(C_WHITE);
	for (int i=0; i<512; i++){
	    for (int i=0; i<512; i++){
		for (int i=0; i<512; i++){
		    dtext(1, 1, C_BLACK, "@!asdf12iik");
		    dupdate();
		}
	    }
	}
}

int main(void)

{
	point points[512]={
	    [0 ... 511] = {0,0,'@'}
	};
	int indexCounter = 0;
	for (int i=0; i<18; i++){
	    for (int k=0; k<32; k++){
		points [indexCounter].x = k*12;
		points [indexCounter].y = i*12;
		points [indexCounter].entity= '@';
		indexCounter++;
	    }
	}
	
	dclear(C_WHITE);
	dtext(1, 1, C_BLACK, "@!asdf12iik");
	dupdate();
	getkey();
	return 1;
}
