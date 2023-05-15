import threading as t
import time
import pandas as pd

primos = []

#defini n como 60000 n é até onde a thread vai procurar por numeros primso
try:
    n = int(input("Introduza numero limite para a verificação de numeros primos:"))
    cores = int(input("Introduza o numero de Threads para processamento concorrente:"))
except ValueError:
    print('O número introduzido tem de ser um inteiros superiores a 0.\nCorra novamente o programa.')
    exit(1)

piece =  n // cores
start = 2
end = piece
if n % cores == 0:
    gap = 0
else:
    gap = n - piece * cores 



#Primo é um numero que só é divisivel por ele proprio e por 1
def prime_number(i, start, end):
    for num in range(start, end+1):
    #Todos os primos têm de ser maiores que um 
        for j in range(2, num):
            if (num % j) == 0:
                break
        else:
            if num is not 1 and num not in primos : primos.append(num)     

      
#tempo antes da execução    
start_time = time.time()
threads = []
for i in range(cores):
    # cria a nova thread
    new_t = t.Thread(target=prime_number, args=(i, start, end))
    #inicia
    threads.append(new_t)
    new_t.start()
    start = end
    if i == cores-2:
        end = end + piece + gap
    else:
        end = end + piece
    
for th in threads:
    th.join()

#tempo final
end_time = time.time()


print('*'*130+'\n'+'*'*130+f'\nConcluiu a execução em {end_time-start_time} segundos')
print('Numero é primo') if n in primos else print('Numero não é primo')

input = end_time-start_time
""" Reports automaticos para o Excell a quando da execução do programa """
data = pd.read_excel('Report_Concorrente.xlsx', sheet_name='Report_Concorrente')
df = pd.DataFrame(data)
counter = df['Tempo (Segundos)'].count()
if counter == 0:
    new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input, 'Cores':cores, 'N':n} , index= [ i for i in range(counter+1)] )
    new_df.to_excel("Report_Concorrente.xlsx", sheet_name='Report_Concorrente')
else:
    new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input, 'Cores':cores, 'N':n} , index= [ i for i in range(counter, counter+1)] )
    final_df = df.append(new_df)
    del final_df['Unnamed: 0']
    final_df.to_excel("Report_Concorrente.xlsx", sheet_name='Report_Concorrente')

    