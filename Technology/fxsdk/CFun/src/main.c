#include <gint/display.h>
#include <gint/keyboard.h>
#include <fxlibc/printf.h>

int main(void)
{
	font_t const *old_font = dfont(new_font);
	dclear(C_WHITE);
	dtext(1, 1, C_BLACK, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890");
	dupdate();

	getkey();
	return 1;
}
