import Osobnik
import Populacja

# fenotyp - 365 dni w roku w których trzeba kosić trawę
# genotyp ciąg 365 bitów, 0 -  nie kosimy, 1 - kosimy
# funkcja celu: trawa ma być krótsza niż 10cm, kara za koszenie w niedziele
# niedziele: bity o numerze podzielnym przez 7
# wzrost trawy: losowa liczba większa od zera z rozkładu normalnego o średniej zależnej od pory roku; małe odchylenie rozkł
# średnie rozkładu wzrostu: lista zdefiniowana na twardo

goowno = Populacja.Populacja()
#print(goowno.listaOsobnikow[2].genom)
goowno.wylicz_funkcje_celu()
goowno.printPop()
goowno.krzyzowanie()
goowno.printPop()