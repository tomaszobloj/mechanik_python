'''
System logowania z dekoratorem ktory zapisuje dane logowaniaw pliku.
Program obiektowy(klasy, konstruktory, destruktory, hermetyzacja).
Wykorzysywanie modułów(import...).
Zapisywanie obiektów w liscie.
'''

import dane_logowania
import datetime
import klasy as k
import csv


# system logowania, przyjmuje nazwe użytkownika i hasło
def system_logowania(inlog, inpass):
  if inlog == dane_logowania.username:
    if inpass == dane_logowania.password:
      print("Zalogowano! Witaj ", dane_logowania.username,
            " miło Cię znowu widzieć.")
      zapisywanie_czasu()
      return True
    else:
      print("Złe dane logowania!")
      return False
  else:
    print("Nie ma takiego użytkownika")
    return False


# wprowadzanie nazwy użytkownika
def wprowadz_nazwe():
  print("==========")
  input_login = input("Podaj nazwę użytkownika: ")
  return input_login


# wprowadzanie hasła użytkownika
def wprowadz_haslo():
  input_password = input("Podaj hasło: ")
  print("==========")
  return input_password


# zapisuje w pliku czas kiedy użytkownik loguje sie do systemu
def zapisywanie_czasu():
  czas = datetime.datetime.now()
  f = open("czas_logowania.txt", "+a")
  f.write(str(czas))
  f.close()


# zapisywanie danych ktore wprowadzi uzytkownik o naprawie samochodu i zapisanie do listy w pliku
def zapisywanie_danych_auta(marka, model, rocznik, tablica, jaki_problem,
                            nazwa_pliku):
  czas = datetime.datetime.now()
  marka = marka
  model = model
  rocznik = rocznik
  tablica = tablica
  jaki_problem = jaki_problem
  plik = str(nazwa_pliku + ".txt")
  with open(plik, 'w', newline="") as dane_auta:
    zapis = csv.writer(dane_auta)
    zapis.writerow([marka, model, rocznik, tablica, jaki_problem, czas])


while system_logowania(wprowadz_nazwe(), wprowadz_haslo()) == True:
  print('''
=============================================
| Co chciałbyś zrobić dalej?                |
=============================================
| 1: Oddać auto do naprawy.                 |
=============================================
| 2: Sprawdzić status naprawy.              |
=============================================
| 3: Oddebrać auto po naprawie.             |
=============================================
''')
  dzialanie = int(input("Wybierz opcję(1,2,3): "))
  if dzialanie == 1:
    print('''
=============================================
| Wybraleś zgłoszenie samochodu do naprawy. |
=============================================
| Wprowadź dane samochodu:                  |
=============================================

''')
    marka = input("Marka: ")
    model = input("Model: ")
    rocznik = input("Rocznik: ")
    tablica = input("Tablica rejestracyjna:")
    jaki_problem = input("Problem: ")
    auto = k.Samochod(marka, model, rocznik, tablica, jaki_problem)
    auto.zgloszenie()
    zapisywanie_danych_auta(marka, model, rocznik, tablica, jaki_problem,
                            tablica)
  elif dzialanie == 2:
    print("Status")
  elif dzialanie == 3:
    print("Odbiór")
