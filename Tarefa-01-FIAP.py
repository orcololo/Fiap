tamanhos_milho = []
tamanhos_soja = []
areas_milho = []
areas_soja = []
ruaslist_milho = []
ruaslist_soja = []
fertilizantesrua_milho = []
fertilizantesrua_soja = []
fertilizantetotal_milho = []
fertilizantetotal_soja = []
while True:
    print("====BEM VINDO AO PROGRAMA TECNOLÓGICO DE MELHORA AGRÍCULA====")
    print("MENU")
    print("Escolha uma das opções:")
    print("1 - Cálculo de área e de insumos")
    print("2 - Mostrar dados ")
    print("3 - Editar dados")
    print("4 - Excluir dados")
    print("5 - Sair do programa")
    escolha = int(input("Escolha uma das opções acima: \n"))
    if escolha == 1:    
        cultura = str(input("Digite Milho para informar o comprimento do plantio para saber a área e a quantidade de Litros de fertilizante necessárias por rua ou digite Soja para saber o mesmo: \n"))
        if cultura.upper() == "MILHO":
            tamanho1 = float(input("Digite em Metros, o comprimento do seu plantio de Milho: "))
            area1 = tamanho1 ** 2
            print(f"A área do seu plantio de Milho é de {area1} Metros quadrados")
            fertilizante1 = int(input("Agora diga quantas Ruas há na sua plantação para saber a quantidade de fertilizante necessária para cada uma e no total: \n"))
            fertilizanterua_milho = tamanho1 * 0.300
            fertilizantetot_milho = fertilizanterua_milho * fertilizante1
            print(f"Sendo 300 ml por metro, por rua serão necessários {fertilizanterua_milho} litros de fertilizantes, e no total, serão necessários {fertilizantetot_milho} litros")
            tamanhos_milho.append(tamanho1)
            areas_milho.append(area1)
            ruaslist_milho.append(fertilizante1)
            fertilizantesrua_milho.append(fertilizanterua_milho)
            fertilizantetotal_milho.append(fertilizantetot_milho)
        elif cultura.upper() == "SOJA":
            tamanho2 = float(input("Digite em Metros, o comprimento do seu plantio de Soja: "))
            area2 = tamanho2 ** 2
            print(f"A área do seu plantio de Soja é de {area2} Metros quadrados")
            fertilizante2 = int(input("Agora diga quantas Ruas há na sua plantação para saber a quantidade de fertilizante necessária para cada uma e no total: \n"))
            fertilizanterua_soja = tamanho2 *0.200
            fertilizantetot_soja = fertilizanterua_soja * fertilizante2
            print(f"Sendo 200 ml por metro, por rua serão necessários {fertilizanterua_soja} litros de fertilizantes, e no total, serão necessários {fertilizantetot_soja} litros")
            tamanhos_soja.append(tamanho2)
            areas_soja.append(area2)
            ruaslist_soja.append(fertilizante2)
            fertilizantesrua_soja.append(fertilizanterua_soja)
            fertilizantetotal_soja.append(fertilizantetot_soja)
        else:
            print("A palavra digitada está incorreta ou digitada da forma errada, tente Milho ou Soja")
            continue

    elif escolha == 2:
        if len(tamanhos_milho) == 0:
            print("Não há dados ainda")
            continue
        print("\n=== Dados do Milho ===")
        for i in range(len(tamanhos_milho)):
            print(f"Posição {i}")
            print("Tamanho = ", tamanhos_milho[i])
            print("Área = ", areas_milho[i])
            print("Ruas = ", ruaslist_milho[i])
            print("Fertilizantes por rua = ", fertilizantesrua_milho[i])
            print("Fertilizante total = ", fertilizantetotal_milho[i])
        print("\n=== Dados do Soja ===")
        for i in range(len(tamanhos_soja)):
            print(f"Posição {i}")
            print("Tamanho = ", tamanhos_soja[i])
            print("Área = ", areas_soja[i])
            print("Ruas = ", ruaslist_soja[i])
            print("Fertilizantes por rua = ", fertilizantesrua_soja[i])
            print("Fertilizante total = ", fertilizantetotal_soja[i])
    
    elif escolha == 3:
        if len(tamanhos_milho) == 0:
            print("Não há dados ainda")
            continue
        cultura = input("Editar os dados de Milho ou Soja ?\n")
        if cultura.upper() == "MILHO":
            posicao1 = int(input("Digite a posição de registro: "))
            if posicao1 < len(tamanhos_milho):
                tamanho3 = float(input("Novo tamanho: "))
                ruas1 = int(input("Novo número de ruas: "))
                area3 = tamanho3 ** 2
                fert_rua1 =  tamanho3 * 0.300
                fert_tot1 = fert_rua1 * ruas1
                tamanhos_milho[posicao1] = tamanho3
                areas_milho[posicao1] = area3
                ruaslist_milho[posicao1] = ruas1
                fertilizantesrua_milho[posicao1] = fert_rua1
                fertilizantetotal_milho[posicao1] = fert_tot1
                print("Dados atualizados com sucesso")

            else:
                print("Posição inválida")
        elif cultura.upper() == "SOJA":
            posicao2 = int(input("Digite a posição de registro: "))
            if posicao2 < len(tamanhos_soja):
                tamanho4 = float(input("Novo tamanho: "))
                ruas2 = int(input("Novo número de ruas: "))
                area4 = tamanho4 ** 2
                fert_rua2 =  tamanho4 * 0.200
                fert_tot2 = fert_rua2 * ruas2
                tamanhos_soja[posicao2] = tamanho4
                areas_soja[posicao2] = area4
                ruaslist_soja[posicao2] = ruas2
                fertilizantesrua_soja[posicao2] = fert_rua2
                fertilizantetotal_soja[posicao2] = fert_tot2
                print("Dados atualizados com sucesso")
            else:
                print("Dados inválidos")
    elif escolha == 4:
        if len(tamanhos_milho) == 0:
            print("Não há dados ainda")
            continue
        cultura = input("Excluir os dados de Milho ou Soja ?\n")
        if cultura.upper() == "MILHO":
            posicao3 = int(input("Digite a posição de registro: "))
            if posicao3 < len(tamanhos_milho):
                tamanhos_milho.pop(posicao3) 
                areas_milho.pop(posicao3) 
                ruaslist_milho.pop(posicao3) 
                fertilizantesrua_milho.pop(posicao3) 
                fertilizantetotal_milho.pop(posicao3) 
                print("Dados deletados com sucesso")
            else:
                print("Posição inválida")

        elif cultura.upper() == "SOJA":
            posicao4 = int(input("Digite a posição de registro: "))
            if posicao4 < len(tamanhos_soja):
                tamanhos_soja.pop(posicao4)
                areas_soja.pop(posicao4)
                ruaslist_soja.pop(posicao4)
                fertilizantesrua_soja.pop(posicao4)
                fertilizantetotal_soja.pop(posicao4)
                print("Dados deletados com sucesso")
            else:
                print("Dados inválidos")
        else:
            print("Opção inválida")
            continue
    elif escolha == 5:
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")