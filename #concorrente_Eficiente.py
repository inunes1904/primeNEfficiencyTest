import threading as t
import time
import pandas as pd



#defini n como 60000 n é até onde a thread vai procurar por numeros primso
try:
    n = int(input("Introduza numero limite para a verificação de numeros primos:"))
    cores = int(input("Introduza o numero de Threads para processamento concorrente:"))
except ValueError:
    print('O número introduzido tem de ser um inteiros superiores a 0.\nCorra novamente o programa.')
    exit(1)

divis = [1, n]
piece =  n // cores // 2
start = 2
end = piece
if n % cores == 0:
    gap = 0
else:
    gap = n // 2 - piece * cores 



#Primo é um numero que só é divisivel por ele proprio e por 1
def prime_number(i):
    global piece, start, end
    for num in range(start, end + 1):
    #Todos os primos têm de ser maiores que um 
        if (num % n) == 0:
            divis.append(num)
    
            
    start = end
    if i == cores-1:
        end = end + piece + gap
    else:
        end = end + piece

      
#tempo antes da execução    
start_time = time.time()
threads = []
for i in range(cores):
    # cria a nova thread
    new_t = t.Thread(target=prime_number, args=(i,))
    #inicia
    threads.append(new_t)
    new_t.start()
    
for th in threads:
    th.join()

#tempo final
end_time = time.time()

#print(primos)
print('*'*130+'\n'+'*'*130+f'\nConcluiu a execução em {end_time-start_time} segundos')
print('Numero é primo') if len(divis) == 2 else print('Numero não é primo')

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

    