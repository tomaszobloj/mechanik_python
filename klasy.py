class Samochod():

  def __init__(self, mark, mod, rocznik, tablica, jaki_problem):
    self.marka = mark
    self.model = mod
    self.rocznik = rocznik
    self.tablica = tablica
    self.jaki_problem = jaki_problem

  def zgloszenie(self):
    print(
      f'Samochód {self.marka} {self.model} z roku {self.rocznik} o tablicach {self.tablica}. Zgłoszony do mechanika z powodu: {self.jaki_problem}'
    )

  def zapisanie_danych(self):
    return self.marka, self.model, self.rocznik, self.tablica, self.jaki_problem
