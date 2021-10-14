def string_to_list(napis):
  lista = [] 
  for element in napis:
    lista.append(element)
  return lista

def way_to_move(indeks, lista):
  chunk = [lista[0][indeks[1] - 1:indeks[1] + 1], lista[1][indeks[1] - 1:indeks[1] + 1]] 
  if(chunk[0][0] == '0'):
    return [0, indeks[1] - 1]
  if(chunk[0][1] == '0'):
    if(indeks[0] != 1):
      return [1, indeks[1]]
  if(chunk[1][0] == '0'):
    return [1, indeks[1] - 1]
  if(chunk[1][1] == '0'):
    if(indeks[0] != 1):
      return [1, indeks[1]]
  return


def solve():
  liczba_n = int(input())
  row_jeden_string = input() 
  row_dwa_string = input()
  row_jeden_lista = string_to_list(row_jeden_string)
  row_dwa_lista = string_to_list(row_dwa_string)
  lista = [row_jeden_lista, row_dwa_lista]
  indeks = [1, liczba_n - 1]
  while(True):
    ruch = way_to_move(indeks, lista) 
    if(ruch):
      indeks = ruch 
    else:
      print("NO") 
      return  
    if(indeks == [0, 0]):
      print("YES") 
      return

ilosc = int(input()) 

for element in range(ilosc):
  solve()