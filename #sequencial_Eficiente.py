import pandas as pd
import time


#Primo é um numero que só é divisivel por ele proprio e por 1
def prime_number(n):
    for num in range(2, n//2 + 1):
    #Todos os primos têm de ser maiores que um 
        if (num % n) == 0:
            divis.append(num)
        
        
#defini n como 6000 n é até onde a thread vai procurar por numeros primos
try:
    n = int(input("Introduza numero limite para a verificação de numeros primos:"))
except ValueError:
    print('O número introduzido tem de ser um inteiros superiores a 0.\nCorra novamente o programa.')
    exit(1)

divis = [1, n]
#tempo antes da execução
start_time = time.time()
#inicia
prime_number(n)
#tempo final
end_time = time.time()

print('*'*130+'\n'+'*'*130+f'\nConcluiu a execução em {end_time-start_time} segundos')
print('Numero é primo') if len(divis) == 2 else print('Numero não é primo')
input = end_time-start_time

""" Reports automaticos para o Excell a quando da execução do programa """
data = pd.read_excel('Report_Sequencial.xlsx', sheet_name='Report_Sequencial')
df = pd.DataFrame(data)
counter = df['Tempo (Segundos)'].count()
if counter == 0:
    new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input,'N':n} , index= [ i for i in range(counter+1)] )
    new_df.to_excel("Report_Sequencial.xlsx", sheet_name='Report_Sequencial')
else:
    new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input, 'N':n} , index= [ i for i in range(counter, counter+1)] )
    final_df = df.append(new_df)
    del final_df['Unnamed: 0']
    final_df.to_excel("Report_Sequencial.xlsx", sheet_name='Report_Sequencial')
