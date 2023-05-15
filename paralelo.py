from multiprocessing import Manager, Process
import pandas as pd
import time

#Primo é um numero que só é divisivel por ele proprio e por 1
def prime_number(primos, j, start, end):
    for num in range(start, end+1):
    #Todos os primos têm de ser maiores que um 
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            if num != 1 and num not in primos : primos.append(num)      


if __name__ == "__main__":

    try:
        n = int(input("Introduza numero limite para a verificação de numeros primos:"))
        cores = int(input("Introduza o numero de Processos para processamento paralelo:"))
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
        

    processes = []
    with Manager() as manager:
        primos = manager.list()  # criacao de lista que pode ser partilhada por processos.
        #tempo antes da execução    
        start_time = time.time()
        for j in range(cores):
            p = Process(target=prime_number, args=(primos, j, start, end))
            processes.append(p)
            p.start() 
            start = end
            if j == cores-2:
                end = end + piece + gap
            else:
                end = end + piece

        for p in processes:
            p.join() 

        #tempo final
        end_time = time.time() 
         
        

        print('*'*130+'\n'+'*'*130+f'\nConcluiu a execução em {end_time-start_time} segundos')
        print('Numero é primo') if n in primos else print('Numero não é primo')
        
    input = end_time-start_time
    data = pd.read_excel('Report_Paralelo.xlsx', sheet_name='Report_Paralelo')
    df = pd.DataFrame(data)
    counter = df['Tempo (Segundos)'].count()
    if counter == 0:
        new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input, 'Cores':cores, 'N':n} , index= [ i for i in range(counter+1)] )
        new_df.to_excel("Report_Paralelo.xlsx", sheet_name='Report_Paralelo')
    else:
        new_df = pd.DataFrame( {'Tentativa': counter+1, 'Tempo (Segundos)': input, 'Cores':cores, 'N':n} , index= [ i for i in range(counter, counter+1)] )
        final_df = df.append(new_df)
        del final_df['Unnamed: 0']
        final_df.to_excel("Report_Paralelo.xlsx", sheet_name='Report_Paralelo')