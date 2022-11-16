#include <gint/display.h>
#include <gint/keyboard.h>
//screen size is 384 x 216/32 x 18
#define dimensionX 32
#define dimensionY 18
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

typedef struct heroDirection
{
    int x;
    int y;
}heroDirection;

void updateScreen(point points [pointNumber])
{
    dclear(C_WHITE);
    for (int i=0; i<pointNumber; i++){
	dtext(points[i].x, points[i].y, C_BLACK, &points[i].entity);
    }
    dupdate();
}

void moveHero(heroDirection offset, hero* heropoint)
{
    points
    heropoint->x += offset.x;
    heropoint->y += offset.y;
}

void updateHero(point points [pointNumber], hero heropoint)
{
    points[heropoint.x + heropoint.y * dimensionX].entity = '@';
}

int main(void)

{
	hero heropoint={
	    31,17
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
	updateHero(points, heropoint);
	updateScreen(points);

	while(1){
	    getkey();
	    if(keydown(KEY_UP)){
		heroDirection offset={0,-1};
		moveHero(offset, &heropoint);
	    }
	    if(keydown(KEY_DOWN)){
		heroDirection offset={0,1};
		moveHero(offset, &heropoint);
	    }
	    if(keydown(KEY_LEFT)){
		heroDirection offset={-1,0};
		moveHero(offset, &heropoint);
	    }
	    if(keydown(KEY_RIGHT)){
		heroDirection offset={1,0};
		moveHero(offset, &heropoint);
	    }
	    if(keydown(KEY_EXIT)) {
		return 1;
	    }
	updateHero(points, heropoint);
	updateScreen(points);
	}
}
