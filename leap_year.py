def leap_year():
    ano = int(input())
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
      print("Yes")
    else:
      print("No")

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


leap_year()