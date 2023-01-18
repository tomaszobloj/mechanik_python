'''
System logowania z dekoratorem ktory zapisuje dane logowaniaw pliku.
Program obiektowy(klasy, konstruktory, destruktory, hermetyzacja).
Wykorzysywanie modułów(import...).
Zapisywanie obiektów w liscie.
'''

import dane_logowania
import datetime


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


if system_logowania(wprowadz_nazwe(), wprowadz_haslo()) == True:
  print('''
=======================================
| Co chciałbyś zrobić dalej?          |
=======================================
| 1: Oddać auto do naprawy.           |
=======================================
| 2: Sprawdzić status naprawy.        |
=======================================
| 3: Oddebrać auto po naprawie.       |
=======================================
''')
  dzialanie = int(input("Wybierz opcję: "))
