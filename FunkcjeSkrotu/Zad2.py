import hashlib
import string
import plotly.express as plotly
from pandas import DataFrame
import timeit
import random

class Hash:
    def __init__(self, daneWejsciowe):
        self.daneWejsciowe = daneWejsciowe
        self.wynik = {}
    

    def hashuj(self):
        """
        Hashuje dane podane z konsoli

        Parametry:
        self.daneWejsciowe (str) - tekstowe dane wejsciowe z konsoli

        Zwraca:
        (str) Obliczony hash
        """
        algorytmy = hashlib.algorithms_available
        dane = self.daneWejsciowe.encode()
        for algorytm in algorytmy:
            if "shake" not in algorytm:
                hashlib.new(algorytm, dane).hexdigest()
            else:
                hashlib.new(algorytm, dane).hexdigest(20)

    def hash_plik(self, sciezka):
        """
        Hashuje plik ze ścieżki podanej w konsoli

        Parametry:
        sciezka (str) - sciezka do pliku

        Zwraca:
        (str) Obliczony hash pliku lub błąd ścieżki
        """
        try:
            with open(sciezka, "rb") as f:
                hasher = hashlib.file_digest(f, "sha256")
            obliczony = hasher.hexdigest()
            print(f"Hash pliku: {obliczony}")
        except:
            print("Błędna ścieżka")
    
    
    def czasHashowania(self):
        """
        Oblicza czas hashowania dla danych z konsoli

        Parametry:
        Funkcja wywołuje inną funkcję "hash()" w pętli w celu obliczenia czasu wykonania

        Zwraca:
        Otwiera stronę w przeglądarce przygotowaną przez bibliotekę "plotly" z czasem hashowania dla danych wejściowych
        """
        wyniki = {}
        algorytmy = hashlib.algorithms_available
        sprawdzCzasFunkcji = timeit.Timer(lambda: self.hashuj())
        for algorytm in algorytmy:
            wyniki[algorytm] = sprawdzCzasFunkcji.timeit(number=1000)
        plot = DataFrame(list(wyniki.items()), columns=['Algorytm', 'Milisekundy'])
        wyniki = plotly.scatter_polar(plot, r="Milisekundy",theta="Algorytm")
        wyniki.show()
    

    def rozneRozmiary(self, n):
        """
        Oblicza czas hashowania dla roznej dlugoci stringow

        Parametry:
        (int) n - liczba potęgi liczby 10 do której ma być sprawdzany czas hashowania

        Zwraca:
        Otwiera stronę w przeglądarce przygotowaną przez bibliotekę "plotly" z porównaniem czasu hashowania
        """
        dlugosci = [10**k for k in range(n)]
        wyniki = {}
        for dlugosc in dlugosci:
            losowyString = ''.join(random.choices(string.ascii_uppercase + string.digits, k=dlugosc))
            sprawdzCzasFunkcji = timeit.Timer(lambda: hashlib.new("sha512", losowyString.encode()).hexdigest())
            wyniki[dlugosc] = sprawdzCzasFunkcji.timeit(number=1000)
        plot = DataFrame(list(wyniki.items()), columns=["Długość Słowa", "Milisekundy"])
        wyniki = plotly.line(plot, y="Milisekundy", x="Długość Słowa")
        wyniki.show()


def main():
    print("Podaj dane do hashowania")
    wejscie = input()
    h = Hash(wejscie)
    h.czasHashowania()
    sciezka = input("Podej sciezke pliku do sprawdzenia hashu\n")
    h.hash_plik(sciezka)
    ile = input("Podaj długość n we wzorze (10^n) do sprawdzenia\n")
    try:
        h.rozneRozmiary(int(ile))
    except ValueError:
        print("Nie podano liczby")



if __name__ == "__main__":
    main()
    