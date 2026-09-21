#Entrada
tipo_imovel = input("Qual o tipo de imóvel? (Opções: comercial, casa ou apartamento) ")
consumo_mensal = float(input("Qual o consumo mensal (em m³)? "))

#Saída
match tipo_imovel:
    case "comercial"|"Cormercial":
        print("Tarifa comercial aplicada - Consulte o plano corporativo!")
    case "apartamento"|"Apartamento":
        if consumo_mensal < 10:
            print("Consumo econômico - Excelente controle de água!")
        elif consumo_mensal <= 25:
            print("Consumo moderado - Dentro do padrão residencial!")
        else:
            print("Consumo excessivo - Adote medidas de economia e verifique possíveis vazamentos!")
    case "casa"|"Casa":
        if consumo_mensal <=25:
            print("Consumo moderado - Dentro do padrão residencial!")
        else:
            print("Consumo excessivo - Adote medidas de economia e verifique possíveis vazamentos!")