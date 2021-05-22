import tkinter
cn = tkinter.Canvas()
cn.pack()
cn.config(height= 265, width= 225, bg = 'gray')

cnt = cn.create_text
cnr = cn.create_rectangle

cislo1 = 0
cislo2 = 0
znamienko = 0
vysledok = 0

cnr(15, 35, 220, 70, outline = 'gray35', fill = 'white', width = 2, tags= 'okno')
cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')

#### CISLA
def c1():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 1
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 1
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c2():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 2
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 2
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c3():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 3
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 3   
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c4():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 4
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 4
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c5():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 5
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 5
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c6():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 6
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 6
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c7():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 7
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 7
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c8():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 8
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 8
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c9():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10 + 9
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10 + 9
        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

def c0():
    global cislo1, cislo2, znamienko

    if (znamienko == 0):
        cislo1 = cislo1 * 10
        cn.delete('cisla')
        cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    else:
        cislo2 = cislo2 * 10

        cn.delete('cisla')
        cnt(115, 53, text= cislo2, font= 'Ariel 20', tags= 'cisla')

#### ZNAMIENKA

def pl():
    global znamienko
    znamienko = 1

def mi():
    global znamienko
    znamienko = 2

def kr():
    global znamienko
    znamienko = 3

def de():
    global znamienko
    znamienko = 4

#### ROVNA SA A ZMAZ FUNKCIE TLACIDIEL
def rov():
    global znamienko, cislo1, cislo2, vysledok
    
    if (znamienko == 1):
        vysledok = cislo1 + cislo2
        
    elif (znamienko == 2):
        vysledok = cislo1 - cislo2

    elif (znamienko == 3):
        vysledok = cislo1 * cislo2
        
    elif (znamienko == 4):
        vysledok = cislo1 / cislo2

    cn.delete('cisla')
    cnt(115, 53, text= vysledok, font= 'Ariel 20', tags= 'cisla')

    vysledok = 0
    znamienko = 0
    
def zmaz():
    global znamienko, cislo1, cislo2
    znamienko = 0
    cislo1 = 0
    cislo2 = 0
    cn.delete('cisla')
    cnt(115, 53, text= cislo1, font= 'Ariel 20', tags= 'cisla')
    

#### TLACIDLA
b1 = tkinter.Button(text = '1', command=c1, width = 5, bg = 'gray75', activebackground = 'snow')
b2 = tkinter.Button(text = '2', command=c2, width = 5, bg = 'gray75', activebackground = 'snow')
b3 = tkinter.Button(text = '3', command=c3, width = 5, bg = 'gray75', activebackground = 'snow')
b4 = tkinter.Button(text = '4', command=c4, width = 5, bg = 'gray75', activebackground = 'snow')
b5 = tkinter.Button(text = '5', command=c5, width = 5, bg = 'gray75', activebackground = 'snow')
b6 = tkinter.Button(text = '6', command=c6, width = 5, bg = 'gray75', activebackground = 'snow')
b7 = tkinter.Button(text = '7', command=c7, width = 5, bg = 'gray75', activebackground = 'snow')
b8 = tkinter.Button(text = '8', command=c8, width = 5, bg = 'gray75', activebackground = 'snow')
b9 = tkinter.Button(text = '9', command=c9, width = 5, bg = 'gray75', activebackground = 'snow')
b0 = tkinter.Button(text = '0', command=c0, width = 5, bg = 'gray75', activebackground = 'snow')

bx = tkinter.Button(text = '*', command=kr, width = 5, bg = 'gray75', activebackground = 'snow')
bd = tkinter.Button(text = '/', command=de, width = 5, bg = 'gray75', activebackground = 'snow')
bm = tkinter.Button(text = '-', command=mi, width = 5, bg = 'gray75', activebackground = 'snow')
bp = tkinter.Button(text = '+', command=pl, width = 5, bg = 'gray75', activebackground = 'snow')

br = tkinter.Button(text = '=', command=rov, width = 5, bg = 'gray75', activebackground = 'snow')
zm = tkinter.Button(text= 'zmaz', command=zmaz, width = 5, bg = 'gray75', activebackground = 'snow')

b1.place(x= 15, y= 100)
b2.place(x= 65, y= 100)
b3.place(x= 115, y= 100)
b4.place(x= 15, y= 140)
b5.place(x= 65, y= 140)
b6.place(x= 115, y= 140)
b7.place(x= 15, y= 180)
b8.place(x= 65, y= 180)
b9.place(x= 115, y= 180)
b0.place(x= 65, y= 220)

bd.place(x= 165, y= 100)
bx.place(x= 165, y= 140)
bm.place(x= 165, y= 180)
bp.place(x= 165, y= 220)

br.place(x= 115, y= 220)
zm.place(x= 15, y= 220)

cn.move('all', -3, 0)
