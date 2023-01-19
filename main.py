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
      print("| Witaj ", dane_logowania.username,
            " miło Cię znowu widzieć.      |")
      print("=============================================")
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
  print("=============================================")
  input_login = input("| Podaj nazwę użytkownika: ")
  return input_login


# wprowadzanie hasła użytkownika
def wprowadz_haslo():
  input_password = input("| Podaj hasło: ")
  print("=============================================")
  return input_password


# zapisuje w pliku czas kiedy użytkownik loguje sie do systemu
def zapisywanie_czasu():
  czas = datetime.datetime.now()
  f = open("czas_logowania.txt", "+a")
  f.write(str(czas))
  f.close()


# zapisywanie danych które wprowadził użytkownik o naprawie samochodu i zapisanie do listy w pliku
def zapisywanie_danych_auta(marka, model, rocznik, tablica, jaki_problem,
                            nazwa_pliku):
  x = datetime.datetime.now()
  dzien = x.day
  miesiac = x.month
  rok = x.year
  marka = marka
  model = model
  rocznik = rocznik
  tablica = tablica
  jaki_problem = jaki_problem
  plik = str(nazwa_pliku + ".txt")
  with open(plik, 'w', newline="") as dane_auta:
    zapis = csv.writer(dane_auta)
    zapis.writerow(
      [marka, model, rocznik, tablica, jaki_problem, dzien, miesiac, rok])


# odczytywanie danych z pliku
def odczytywanie_danych_auta(nazwa_pliku):
  nazwa_pliku += ".txt"
  with open(nazwa_pliku) as txt_file:
    wypisywacz = csv.reader(txt_file, delimiter=",")

    for linia in wypisywacz:
      marka = linia[0]
      model = linia[1]
      rocznik = linia[2]
      tablica = linia[3]
      jaki_problem = linia[4]
      print("Problem :", jaki_problem,
            " został naprawiony w samochodzie marki ", marka, model,
            " z rocznika ", rocznik, " o tablicach ", tablica)


# sprawdzanie statusu samochodu
def status_auta(nazwa_pliku):
  nazwa_pliku += ".txt"
  with open(nazwa_pliku) as status_check:
    wypisywacz = csv.reader(status_check, delimiter=",")
    for linia in wypisywacz:
      dzien = linia[5]
      miesiac = linia[6]
      rok = linia[7]
      nowy_dzien = int(linia[5]) + 7
      nowy_miesiac = int(linia[6])
      nowy_rok = int(linia[7])
      print("Oddany samochód do naprawy", dzien, ".", miesiac, ".", rok,
            " będzie gotowy na ", nowy_dzien, ".", nowy_miesiac, ".", nowy_rok)


# główna pętla z funkcjami programu, działa gdy użytkownik poprawnie się zaloguje
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
  try:
    dzialanie = int(input("Wybierz opcję: "))
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
      break
    elif dzialanie == 2:
      print('''
=============================================
| Podaj numer rejestracyjny samochodu.      |
=============================================
''')
      status = input("Podaj numery tablicy rejestracyjnej:")
      status_auta(status)
      break
    elif dzialanie == 3:
      print('''
=============================================
| Wybraleś odbiór samochodu.                |
=============================================
''')
      auto_odbierane = input("Podaj numery tablicy rejestracyjnej:")
      odczytywanie_danych_auta(auto_odbierane)
      break
    else:
      print("Wybrałeś złą opcję!")
  except:
    print("Podaj wartość liczbową.")
