from datetime import datetime

import random

class Exames:
    def __init__(self,exame,consulta):
        self.exame = exame
        self.consulta = consulta

    def escolha(self):
        print("")
        print("_" * 30)
        print("QUAL EXAME DESEJA FAZER ? ")
        print("_" * 30)
        print("")

  
        data_atual = datetime.now()

        data_formatada = data_atual.strftime("%d-%m-%y")




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

            resultado_glicemia = random.randint(65,120)
            print(f"Seu exame de Glicemia em jejum deu___________{resultado_glicemia} mg/dl                             Data: {data_formatada}")

            resultado_glicemia2 = random.randint(110,210)
            print(f"Seu exame de Glicemia após 60 min deu________{resultado_glicemia2} mg/dl ")

            resultado_glicemia3 = random.randint(65,160)
            print(f"Seu exame de Glicemia após 120 min deu_______{resultado_glicemia3} mg/dl ")
            print("")


            if resultado_glicemia >= 70 and resultado_glicemia <= 110:
                print("Sua Glicemia em jejum apresentou valores normais ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia > 115:
                print("A Glicemia em jejum apresentou valores elevados !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")
            elif resultado_glicemia < 70 :
                print("Cuidado !!")
                print("A Glicemia em jejum apresentou valores baixos !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")

            if resultado_glicemia2 <= 200 and resultado_glicemia2 >= 125:
                print("Sua Glicemia após 60 min, apresentou valores normais ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia2 < 125:
                print("A Glicemia após 60 min, apresentou valores baixos !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")
            elif resultado_glicemia2 > 200:
                print("Cuidado !!")
                print("A Glicemia após 60 min, apresentou valores elevados !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")

            if resultado_glicemia3 >= 75 and resultado_glicemia3 <= 140:
                print("Sua Glicemia após 120 min apresentou valores normais ")
                print("Parabens !!")
                print("")
            elif resultado_glicemia3 < 70:
                print("A Glicemia após 120 min apresentou valores baixos !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")
            elif resultado_glicemia3 > 140:
                print("Cuidado !!")
                print("A Glicemia após 120 min apresentou valores elevados !")
                print("Sendo aconselhável a observação da dieta. ")
                print("")

            self.escolha()


        elif esc == 2:

            print("HEMOGRAMA")
            print("")
            eritrocitos = random.uniform(3.8,6.5) # 4.5 a 5.9 milhões/mm³

            hemoglobina = random.uniform(11,18.3) # 12 a 15.5 g%

            hematocrito = random.randint(35,57) # 40 a 52 %


            print("ERITROGRAMA ")
            print("")
            print(f"Eritrócitos___________{eritrocitos:.3f} mihões/mm³                              Data: {data_formatada} ")
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



            leucocitos = random.uniform(2.000,13.000) # 4.5 a 11 /mm³

            eosinofilos =  random.randint(0,5) # 0 a 4 %

            linfocitos = random.randint(17,45) # 20 a 40 %

            monocitos = random.randint(0,10) # 2 a 8 %

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

            plaquetas = random.uniform(98.000, 500.000) # 150.000 a 400.00 /mm³

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

            self.escolha()

        elif esc == 3:
            print("")
            print("COLESTEROL")
            print("")

            colesterolldl = random.randint(90,120) # 60 a 130 mg/dl colesterol ruim

            colesterolhdl = random.randint(30,70) # acima de 40 colesterol bom

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

            self.escolha()

        elif esc == 4:
            print("Ureia e Creatinina")
            print("")

            self.escolha()

        elif esc == 5:
            print("Obrigado !!")
            print("Lembre-se a importancai de cuidar da saúde ! ")

        else:
            print("OPÇÃO INVÁLIDA !! ")
            print("Tente Novamente ")

            self.escolha()
        

dd = Exames("","")
dd.escolha()