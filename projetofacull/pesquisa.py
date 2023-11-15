class Pesquisa:
    
    def __init__(self):
        self.fumar = ""
        self.beber = ""
        self.exercicio = ""
        self.alimentacao = ""
        self.descanso = ""
        self.lazer = ""
        self.drogas = ""
        self.muitoTempoCelular = ""

    def fazer_pergunta(self, pergunta):
        resposta = input(pergunta + " ( s/n ): ").lower()
        return resposta

    def realizar_pesquisa(self):
        print("Vamos fazer uma rápida pesquisa!")
        print("")

        self.fumar = self.fazer_pergunta("Você fuma?")
        self.beber = self.fazer_pergunta("Você bebe?")
        self.drogas = self.fazer_pergunta("Você usa drogas?")
        self.muitoTempoCelular = self.fazer_pergunta("Costuma ficar muito tempo no celular?")

        self.exercicio = self.fazer_pergunta("Costuma praticar exercícios físicos regularmente?")
        self.alimentacao = self.fazer_pergunta("Costuma se alimentar de forma correta?")
        self.descanso = self.fazer_pergunta("Descansa o suficiente diariamente?")
        self.lazer = self.fazer_pergunta("Tem horários de lazer ao decorrer do mês?")


        maus_habitos = [self.fumar, self.beber, self.drogas, self.muitoTempoCelular]
        bons_habitos = [self.exercicio, self.alimentacao, self.descanso, self.lazer]


        maus_habitos_count = maus_habitos.count('s')
        bons_habitos_count = bons_habitos.count('s')
        saude1 = 0
        saude2 = 0
        print("")

        if maus_habitos_count == 0:
            saude1 = 100
        elif maus_habitos_count == 1:
            saude1 = 75
        elif maus_habitos_count == 2:
            saude1 = 50
        elif maus_habitos_count == 3:
            saude1 = 25
        elif maus_habitos_count == 4:
            saude1 = 0
        
        if bons_habitos_count == 4:
            saude2 = 100
        elif bons_habitos_count == 3:
            saude2 = 75
        elif bons_habitos_count == 2:
            saude2 = 50
        elif bons_habitos_count == 1:
            saude2 = 25
        elif bons_habitos_count == 0:
            saude2 = 0

        saudeTotal = saude1 + saude2

        if saudeTotal == 200:
            print("Parabéns !! Seu modo de vida está perfeito ")

        elif saudeTotal == 175:
            print("Parabéns !! Seu modo de vida está muito bom")

        elif saudeTotal == 150:
            print("Seu modo de vida está bom ")

        elif saudeTotal == 125:
            print("Seu modo de vida não está bom ")
        
        elif saudeTotal == 100:
            print("Seu modd de vida está ruim ")

        elif saudeTotal == 75:
            print("Seu modo de vida está muito ruim ")

        elif saudeTotal == 50:
            print('seu modo de vida está péssimo ')
        elif saudeTotal == 25:
            print("Mude agoar seu modo de vida está terrivel, procure com urgencia um especialista ! ")
        elif saudeTotal == 0:
            print("Vai morrer em 5 min !! ")
        

pesquisa = Pesquisa()

pesquisa.realizar_pesquisa()
