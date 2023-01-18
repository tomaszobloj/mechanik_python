'''
System logowania z dekoratorem ktory zapisuje dane logowaniaw pliku.
Program obiektowy(klasy, konstruktory, destruktory, hermetyzacja).
Wykorzysywanie modułów(import...).
Zapisywanie obiektów w liscie.
'''

import dane_logowania

# system logowania, przyjmuje nazwe użytkownika i hasło
def system_logowania(inlog, inpass):
    if inlog == dane_logowania.username:
      if inpass == dane_logowania.password:
        print("Zalogowano!")
      else:
        print("Złe dane logowania!")
    else:
      print("Nie ma takiego użytkownika")

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

system_logowania(wprowadz_nazwe(), wprowadz_haslo())