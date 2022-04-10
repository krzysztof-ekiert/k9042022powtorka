pomidor = ["pomidor", 19, 1, 0, 4, 5.7, 350]
mozarella = ["ser mozarella", 248, 18, 19, 2, 38.32, 325]
salata = ["sałata", 13, 1, 0, 2, 3.15, 350]

produkty = [pomidor, mozarella, salata]

raport = ""
koszt = 0
bialko, tluszcz, wegle, kalorie, waga_calosc = 0,0,0,0,0
for produkt in produkty:
    name = produkt[0]
    waga = produkt[-1]
    cena = waga * produkt[-2] / 1000
    k = produkt[1] / 100 * waga
    b = produkt[2] / 100 * waga
    t = produkt[3] / 100 * waga
    w = produkt[4] / 100 * waga
    
    raport += (f'{name:15}, kalorie: {k:>6.2f}, b: {b:5.2f}, '
    f't: {t:5.2f}, w: {w:5.2f}, waga: {waga:4} g, koszt: {cena:>5.2f} PLN \n')
    
    koszt +=cena
    kalorie += k
    bialko += b
    tluszcz += t 
    wegle += w 
    waga_calosc += waga 
    
raport += "="*80 + "\n"
raport += (f'{"SUMA":15}, kalorie: {kalorie:>6.2f}, b: {bialko:5.2f}, '
    f't: {tluszcz:5.2f}, w: {wegle:5.2f}, waga: {waga_calosc:4} g, koszt: {koszt:>5.2f} PLN \n')

    
print(raport)