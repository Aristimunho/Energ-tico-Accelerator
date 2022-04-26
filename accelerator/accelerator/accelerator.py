#Gerador de notas fiscais com tributações.

print('╔═════════════════════════════════════╗')
print('║ NOTA FISCAL ENERGÉTICOS ACCELERATOR ║')
print('╚═════════════════════════════════════╝')
print()

#Laço de repetição para verificação dos dados adicionados. 
x = 1
empresa = {}
empresas = []
mercadoria = 0
impostos = 0
geral = 0
cont = 0
while(x == 1):
 #tenta executar o seguinte código.
 try:
  nome = input('Digite o nome da empresa referente a nota fiscal: ')
  print()
  valor = int(input('Digite a QUANTIDADE de latas do energético: '))*4.5
  print()
  # Cálculo dos impostos. 
  empresa['empresa'] = nome
  empresa['ICMS'] = round(valor*0.18,2)
  empresa['IPI'] = round(valor*0.04,2)
  empresa['PIS'] = round(valor*0.0186,2)
  empresa['COFINS'] = round(valor*0.0854,2)

  # Cálculo dos totais.
  mercadoria = mercadoria + valor 
  geral = round(geral + valor + empresa['ICMS'] + empresa['IPI'] + empresa['PIS'] + empresa['COFINS'],2)
  impostos = round((geral - mercadoria),2)
  empresas.append(empresa.copy())

  print("Digite F para finalizar a nota ou qualquer caractere para adicionar mais empresas.")
  c = input()
  print()

  #Impressão dos dados.
  if(c == 'F' or c == 'f'):
      print("═"*25)
      for i in empresas:
          for a,b in i.items():
            cont = cont + 1
            print('{}: {}'.format(a,b))

            # Cálculo da bonificação para a próxima compra.
            if(a == 'COFINS'):
                if(b >= 854):# Quando COFINS é >= 854 o valor em produtos é >= 10 mil.
                    print('╔════════════════════════╗')
                    print('║ A empresa comprou mais ║')
                    print('║ de 10 mil em produtos. ║')   
                    print('║ Bonificação de 10 %    ║')
                    print('║       LIBERADA         ║')
                    print('║ para a próxima compra! ║')
                    print('╚════════════════════════╝')
            if(cont % 5 == 0):
                print("═"*25)

      # Impressão dos cálculos totais.
      print("═"*25)
      print('Total mercadoria:',mercadoria)
      print('Total impostos:',impostos)
      print('Total geral:',geral)
      print("═"*25)
      x = 0  # Sai do laço de repetição.

 # Caso o valor digitado seja diferente do esperado retorna ao laço de repetição.
 except:
  print()
  print('Dados não conferem com o sistema!')
  print('Verifique se o valor total de latas apresenta apenas números inteiros e tente novamente')
  print()