# -*- coding: utf-8 -*-
import curses
import locale
locale.setlocale(locale.LC_ALL, '') # 日本語の文字化け対策

def curses_main(args):
	w = curses.initscr()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
	curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLUE)
	w.bkgd(curses.color_pair(1))
	curses.noecho() # 入力された文字非表示
	curses.cbreak() # 文字が打たれたら即反応
	curses.curs_set(0) # カーソル非表示

	lists = ['じょいあ', 'ora', 'hoge', 'hyahhaa']
	i = 0
	swin = []
	for l in lists:
		swin.append(w.subwin(1,20,i,0))
		swin[i].addnstr(0,0,l,10)
		i += 1
	w.move(0,0)

	x = 0
	y = 0
	ordy = 0
	while 1:
		swin[ordy].bkgd(curses.color_pair(1)) # 選択されてた場所の色を戻す
		swin[y].bkgd(curses.color_pair(2)) # 選択している場所の色変更
		swin[ordy].refresh()
		swin[y].refresh()

		key = w.getkey()
		if key == 'j':
			if y < i - 1:
				ordy = y
				y += 1
				w.move(y, x)
		if key == 'k':
			if y > 0:
				ordy = y
				y -= 1
				w.move(y, x)

		if key == 'd':
			w.deleteln()

		if key == 'q':
			break
curses.wrapper(curses_main)
