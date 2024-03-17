import hashlib
from time import time, sleep
import plotly.express as plotly
from pandas import DataFrame
import timeit

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
        Otwiera stronę w przeglądarce przygotowaną przez bibliotekę "plotly"
        """
        wyniki = {}
        algorytmy = hashlib.algorithms_available
        for algorytm in algorytmy:
            wyniki[algorytm] = timeit.timeit(f"{self.hashuj()}", number=100)

        plot = DataFrame(list(wyniki.items()), columns=['Algorytm', 'Milisekundy'])
        wyniki = plotly.scatter_polar(plot, r="Milisekundy",theta="Algorytm")
        wyniki.show()


def main():
    print("Podaj dane do hashowania")
    wejscie = input()
    h = Hash(wejscie)
    h.czasHashowania()
    sciezka = input("Podej sciezke pliku do sprawdzenia hashu\n")
    h.hash_plik(sciezka)



if __name__ == "__main__":
    main()
    