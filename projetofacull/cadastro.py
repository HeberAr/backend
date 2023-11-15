class Cadastro:

    def __init__(self,nome,cpf,dataNasc,rg, email, numCell, sexo, cep, endereco, num, estado, cidade):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc
        self.rg = rg
        self.email = email
        self.numCell = numCell
        self.sexo = sexo
        self.cep = cep
        self.endereco = endereco
        self.num = num
        self.estado = estado
        self.cidade = cidade

    def login(self):
        print("_" * 30)
        print("OLÁ, SEJA BEM VINDO(A) !")
        print("_" * 30)
        print("")
        print("_" * 60)
        email1 = input("Digite seu email: ") 
        cpf1 = int(input("Digite seu cpf: "))
        if email1 != self.email or cpf1 != self.cpf:
            print("")
            print("Email ou CPF incorreto !")
            print("Tente novamente ")
            self.login()
        else:
            print("")
            print("Login efetuado com sucesso !")

        self.apresentacao()



    def cadastro(self):
        print("_" * 30)
        print("Vamos efetuar o cadastro ")
        print("_" * 30)
        print("")
        print("_" * 60)
        self.nome = input("Digite seu nome completo: ")
        self.cpf = int(input("Digite seu cpf: "))
        self.dataNasc = int(input("Digite sua data de nascimento: "))
        self.rg = int(input('Digite seu RG: '))
        self.email = input("Digite seu email: ")
        self.numCell = int(input("Digite seu número de telefone: "))
        #Localização
        self.estado = input("Digite a sigla do seu estado: ")
        self.cidade = input("Digite sua cidade: ")
        self.endereco = input("Digite seu endereço: ")
        self.num = int(input("Digite o número da sua casa: "))
        self.cep = int(input("Digite seu CEP: "))
        self.sexo = input("Seu sexo m/f ")
        if self.sexo == "m":
            self.sexo = "Masculino"
        else:
            self.sexo = "Feminino"

        self.login()
        
    def apresentacao(self):
        print("")
        print("_" * 30)
        print("CONFIME SEUS DADOS !!")
        print("_" * 30)
        print("")
        print("_" * 60)
        print(f"Cadastro do cliente : {self.nome}              data de nascimento {self.dataNasc}")
        print(f"{self.nome} portador do CPF : {self.cpf} e do RG : {self.rg} do sexo {self.sexo}")
        print(f"Contatos atravez do email {self.email} e o número de celular {self.numCell}")
        print(f"Possui o endereço {self.endereco}, N° {self.num}, Cidade {self.cidade}, {self.estado} ")
        print(f"CEP: {self.cep}")
        print("_" * 60)
        print("") 
        
pas = Cadastro("",0,0,0,"",0,0,"","","","","")
pas.cadastro()
