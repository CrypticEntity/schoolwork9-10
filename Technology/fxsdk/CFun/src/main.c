#include <gint/display.h>
#include <gint/keyboard.h>
//screen size is 384 x 216/32 x 18
#define dimensionY 18
#define dimensionX 32
#define pointNumber 576
#define pointNumberMinusOne 575

typedef struct hero
{
    int x;
    int y;
}hero;

typedef struct screen
{
    int x;
    int y;
    char entity;
}point;


void updateScreen(point points [pointNumber])
{
    dclear(C_WHITE);
    for (int i=0; i<pointNumber; i++){
	dtext(points[i].x, points[i].y, C_BLACK, &points[i].entity);
    }
    dupdate();
}

int main(void)

{
	hero hero={
	    9,16
	};	
	point points[pointNumber]={
	    [0 ... pointNumberMinusOne] = {0,0,'.'}
	};
	int indexCounter = 0;
	for (int i=0; i<dimensionY; i++){
	    for (int k=0; k<dimensionX; k++){
		points [indexCounter].x = k*12 + 6;
		points [indexCounter].y = i*12 + 4;
		points [indexCounter].entity= '.';
		indexCounter++;
	    }
	}
	updateScreen(points);
	getkey();
	return 1;
}
