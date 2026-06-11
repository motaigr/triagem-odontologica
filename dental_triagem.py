#Sistema de triagem de pacientes de clinica odontologica

import datetime

def main():
    # 1. entrada_paciente()
    # 2. buscar_por_paciente(cpf)
    # 3. comparar_respostas(...)
    # 4. salvar_consulta(...)
    pass

def entrada_paciente():
    #solicitação de cpf para verificar se é novo ou se já teve outra consulta 
    cpf = input("Digite o CPF do paciente (somente os números):")

    paciente = busca_por_paciente(cpf)

    if paciente:
        print(f"Paciente encontrado: {paciente['nome']}")
    else:
        print(f"Paciente não encontrado, siga com o cadastro")
        nome = input("Digite o nome do paciente:")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA):")

    triagem = {}
    triagem["dor"] = input("Está sentindo dor no momento? (sim/não)")
    triagem["inchaco"] = input("Há inchaço no rosto ou gengiva? (sim/não)")
    triagem["trauma"] = input("Houve trauma recente? (sim/não)")
    triagem["sensibilidade"] = input("Apresenta sensibilidade ao quente ou frio? (sim/não)")
    triagem["sangramento"] = input("Existe sangramento gengival espontâneo ou constante? (sim/não)")

    anamnese = {}
    anamnese["doenca"] = input("Possui doença crônica? (sim/não)")
    anamnese["medicamento"] = input("Faz uso contínuo de medicamento? (sim/não)")
    anamnese["alergia"] = input("Possui alergia a medicamentos? (sim/não)")
    anamnese["gestante"] = input("É gestante? (sim/não)")
    anamnese["motivo"] = input("Qual o motivo principal da sua consulta hoje?")

    if paciente:
        comparacao = comparar_respostas

    else:
        salvar_consulta

def busca_por_paciente(cpf):
    pass

def comparar_respostas(consulta_anterior, consulta_atual):
    pass

def salvar_consulta(cpf, respostas):
    pass