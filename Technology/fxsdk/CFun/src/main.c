#include <gint/display.h>
#include <gint/keyboard.h>
#include <fxlibc/printf.h>

int main(void)
{
	dclear(C_WHITE);
	dtext(1, 1, C_BLACK, "@");
	dupdate();

	getkey();
	return 1;
}
