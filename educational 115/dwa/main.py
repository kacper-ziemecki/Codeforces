def usun_spacje(napis):
  nowy_napis = ''
  for element in napis:
    if(element != " "):
      nowy_napis += element 
  return nowy_napis

def solve():
  powtarzanie = int(input()) 
  lista = []
  for i in range(powtarzanie):
    napis = usun_spacje(input()) 
    lista.append(napis) 

  pasuje = {}
  for indeks in range(len(lista[0])):
    pasuje[indeks] = []
    indeks_napisu = -1
    for element in lista:
      indeks_napisu += 1
      if(element[indeks] == '1'):
        pasuje[indeks].append(indeks_napisu)
  poprawnie_pasuje = {}
  ilosc_grupy = len(lista) / 2
  indeks = -1
  for element in pasuje.values():
    indeks += 1
    if(len(element) >= ilosc_grupy):
      poprawnie_pasuje[indeks] = element

  for glowny_element in poprawnie_pasuje.values():
    for poboczny_element in poprawnie_pasuje.values():
      poprawny_poboczny_element = [] 
      for element in poboczny_element:
        if(element not in glowny_element):
          poprawny_poboczny_element.append(element)
      if(len(poprawny_poboczny_element) >= ilosc_grupy):
        print("YES") 
        return
  print("NO") 
  return


ilosc = int(input()) 
for element in range(ilosc):
  solve()