from datetime import datetime

class analiseExame:

    def __init__(self):
        self.analise = ""

    def analisar(self):
        print("")
        print("_" * 30)
        print("QUAL EXAME DESEJA FAZER ? ")
        print("_" * 30)
        print("")

        # Obter a data atual
        data_atual = datetime.now()

        # Imprimir a data no formato YYYY-MM-DD HH:MM:SS
        #print("Data atual:", data_atual)

        # Se você quiser apenas a data no formato YYYY-MM-DD
        data_formatada = data_atual.strftime("%d-%m-%y")
        #print("Data formatada:", data_formatada)

        exames = {
        1: "Glicemia",
        2: "Hemograma",
        3: "Colesterol",
        4: "Ureia e Creatinina",
        5: "Sair"
        }

        for num, nome in exames.items():
            print(f"{num}: {nome}")

        print("")
        esc = int(input("Digite o número do exame desejado: "))
        print("")

        if esc == 1:
            print("GLICEMIA")
            print("")
            print("fazer a coleta de sangue.")
            print("")

            resultado_glicemia = int(input("Glicemia em Jejum: "))#(65,120)
            print(f"Seu exame de Glicemia em jejum deu___________{resultado_glicemia} mg/dl                             Data: {data_formatada}")

            resultado_glicemia2 = int(input("Glicemia após 60 minutos: "))#(110,210)
            print(f"Seu exame de Glicemia após 60 min deu________{resultado_glicemia2} mg/dl ")

            resultado_glicemia3 = int(input("Glicemia após 120 minutos: "))#(65,160)
            print(f"Seu exame de Glicemia após 120 min deu_______{resultado_glicemia3} mg/dl ")
            print("")


            if resultado_glicemia >= 70 and resultado_glicemia <= 110:
                print("Sua Glicemia em jejum deu está normal ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia > 115:
                print("Sua Glicemia em jejum deu deu alta ! ")
                print("Recomedamos que observe sua alimentação, ")
                print("diminua o açucar e refaça o exame !!")
                print("")
            elif resultado_glicemia < 70 :
                print("Cuidado !!")
                print("Sua Glicemia em jejum está baixa , procure um  ")
                print("médico ou refaça o teste para ter certeza ")
                print("")

            if resultado_glicemia2 <= 200 and resultado_glicemia2 >= 125:
                print("Sua Glicemia após 60 min está normal ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia2 < 125:
                print("Sua Glicemia após 60 min deu Beixa ! ")
                print("Recomedamos que observe sua alimentação, procure um especialista ! ")
                print("")
            elif resultado_glicemia2 > 200:
                print("Cuidado !!")
                print("Sua Glicemia após 60 min deu Alta, procure um  ")
                print("médico ou refaça o teste para ter certeza")
                print("")

            if resultado_glicemia3 >= 75 and resultado_glicemia3 <= 140:
                print("Sua Glicemia após 120 min deu está normal ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia3 < 70:
                print("Sua Glicemia após 120 min deu Beixa ! ")
                print("Recomedamos que observe sua alimentação, procure um especialista ! ")
                print("")
            elif resultado_glicemia3 > 140:
                print("Cuidado !!")
                print("Sua Glicemia após 120 min deu Alta, procure um  ")
                print("médico ou refaça o teste para ter certeza")
                print("")

            self.analisar()

        elif esc == 2:
            print("HEMOGRAMA")
            print("")

            eritrocitos = float(input("Eritrocitos: ")) # 4.5 a 5.9 milhões/mm³

            hemoglobina = float(input("Hemoglobina: ")) # 12 a 15.5 g%

            hematocrito = float(input("Hematocrito: ")) # 40 a 52 %


            print("ERITROGRAMA ")
            print("")
            print(f"Eritrócitos___________{eritrocitos:.3f} mihões/mm³                             Data: {data_formatada}  ")
            print(f"Hemoglobina___________{hemoglobina:.3f} g%")
            print(f"Hematócrito___________{hematocrito} % ")
            print("Observações: ")

            if eritrocitos < 4.5 and hemoglobina < 12 or hemoglobina < 12 and hematocrito < 40:
                print("      Os seus níveis do exame de Eritrócitos estão baixos")
                print("       portanto seu resultado é ANEMICA")
            elif eritrocitos > 5.9 and hemoglobina > 15.5 or hemoglobina > 15.5 and hematocrito > 52:
                print(f"     Os seus níveis do exame de Eritrócitos estão altos")
                print("       portanto seu resultado é POLICITAMIA")
            else:
                print("      Seus resultados não deram nada alterado, Parabéns ")

            print("_" * 60)
            print("")



            leucocitos = float(input("Leucocitos: ")) # 4.5 a 11 /mm³

            eosinofilos =  float(input("Eosinifilos: ")) # 0 a 4 %

            linfocitos = float(input("Linfocitos: ")) # 20 a 40 %

            monocitos = float(input("Monócitos: ")) # 2 a 8 %

            print("LEUCOGRAMA ")
            print("")
            print(f"Leucócitos____________{leucocitos:.3f} /mm³")
            print(f"Eosinófilos___________{eosinofilos} %")
            print(f"Linfócitos____________{linfocitos} % ")
            print(f"Monócitos_____________{monocitos} %")
            print("Observações: ")


            if leucocitos > 11:
                print("      Seu nível dos Leucócitos estão alto, pode ser ")
                print("       alguma inflamação ou infeção ! Recomendamos que procure um especialista !! ")
            elif leucocitos < 4.5:
                print("      Seu nível dos Leucócitos estão baixo, pode ser ")
                print("       Imunidade suprimida ! Recomendamos que procure um especialista !!")
            else:
                print("      Seus níveis de Leucócitos estão normais, parabéns !!")


            if eosinofilos > 4:
                print("      Seu nível dos Eosinofilos estão alto, pode ser ")
                print("       alergia ou infeção parasitária  ! Recomendamos que procure um especialista !! ")
            elif eosinofilos < 0:
                print("      Seu nível dos Eosinofilos estão baixo, pode ser ")
                print("       alergia ou infeção parasitária) ! Recomendamos que procure um especialista !!")
            else:
                print("      Seus níveis de Eosinofilos estão normais, parabéns !!")


            if linfocitos > 40:
                print("      Seu nível dos Linfócitos estão alto, pode ser ")
                print("       infeção Viral ou Produção de anticorpos ! Recomendamos que procure um especialista !! ")
            elif linfocitos < 20:
                print("      Seu nível dos Linfócitos estão baixo, pode ser ")
                print("       infeção Viral ou Produção de anticorpos ! Recomendamos que procure um especialista !!")
            else:
                print("      Seus níveis de Linfócitos estão normais, parabéns !!")


            if monocitos > 8:
                print("      Seu nível dos Monócitos estão alto, pode ser ")
                print("       infeções por bactérias ou Parasítas ! Recomendamos que procure um especialista !! ")
            elif monocitos < 2:
                print("      Seu nível dos Monócitos estão baixo, pode ser ")
                print("       infeções por bactérias ou Parasítas ! Recomendamos que procure um especialista !!")
            else:
                print("      Seus níveis de Monócitos estão normais, parabéns !!")

            print("_" * 60)
            print("")

            plaquetas = float(input("Plaquetas: ")) # 150.000 a 400.00 /mm³

            print("PLAQUETOGRAMA ")
            print("")
            print(f"Plaquetas_____________{plaquetas:.3f} /mm³ ")
            print("Observações: ")

            if plaquetas > 400:
                print("      Seu nível das Plaquetas estão alto, cuidado ! ")
                print("       Você corre o risco de ter uma trombose !")
                print("        Recomendamos que procure um especialista !! ")
            elif plaquetas < 150:
                print("      Seu nível das Plaquetas estão baixo, cuidado ! ")
                print("       Você corre o risco de ter uma Hemorragia trombocitopenia ! ")
                print("        Recomendamos que procure um especialista !! ")
            else:
                print("      Seus níveis das Plaquetas estão normais, parabéns !!")

            print("_" * 60)
            print("")

            self.analisar()

        elif esc == 3:
            
            print("")
            print("COLESTEROL")
            print("")

            colesterolldl = int(input("Colesterol LDL: "))# 60 a 130 mg/dl colesterol ruim

            colesterolhdl = int(input("Colesterol HDL: ")) # acima de 40 colesterol bom

            colesterolTotal = (colesterolldl + colesterolhdl) # 200 a 240

            print(f"Colesterol Total______{colesterolTotal} mg/dL                              Data: {data_formatada}")
            print(f"Colesterol LDL________{colesterolldl} mg/dL")
            print(f"Colesterol HDL________{colesterolhdl} mg/dL")
            print("")

            print("CATEGORIA DE RISCO ")
            print("Colesterol LDL")
            print("")
            print("Baixo:            < 130 mg/dL")
            print("Intermediario:    < 100 mg/dL")
            print("Alto:             <  70 mg/dL")
            print("Muito Alto:       <  50 mg/dL")

            self.analisar()

        elif esc == 4:
            print("Exame de Ureia e Creatinina ")
            
            self.analisar()
            
        elif esc == 5:
            print("Obrigado e Volte sempre !! ('-') 👍")


ct = analiseExame()
ct.analisar()
