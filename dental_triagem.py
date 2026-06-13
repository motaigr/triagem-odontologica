#Sistema de triagem de pacientes de clinica odontologica

import datetime
import csv

def main():
    entrada_paciente()
    # 2. buscar_por_paciente(cpf)
    # 3. comparar_respostas(...)
    # 4. salvar_consulta(...)
    

def entrada_paciente():
    #solicitação de cpf para verificar se é novo ou se já teve outra consulta 
    cpf = input("Digite o CPF do paciente (somente os números):")

    paciente = busca_por_paciente(cpf)

    is_novo = paciente is None

    if paciente:
        print(f"Paciente encontrado: {paciente['nome']}")
    else:
        print(f"Paciente não encontrado, siga com o cadastro")
        paciente = {}
        paciente["nome"] = input("Digite o nome do paciente:")
        paciente["data_nascimento"] = input("Digite a data de nascimento (DD/MM/AAAA):")

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

    if not is_novo:
        comparacao = comparar_respostas(paciente["triagem"], triagem)
        for alerta in comparacao:
            print(f"Alerta: {alerta}")
    salvar_consulta(cpf, paciente["nome"], paciente["data_nascimento"], triagem, anamnese)
    

def busca_por_paciente(cpf):
    #responsavel por verificar se o paciente já tem cadastro, caso tenha, retornar os linha do cliente para iniciar a consulta.
    try:
        with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0] == cpf:
                    return {
                        "cpf": linha[0],
                        "nome": linha[1],
                        "data_nascimento": linha[2],
                        "data_consulta": linha[3],
                        "triagem": {
                            "dor": linha[4],
                            "inchaco": linha[5],
                            "trauma": linha[6],
                            "sensibilidade": linha[7],
                            "sangramento": linha[8]
                        },
                        "anamnese": {
                            "doenca": linha[9],
                            "medicamento": linha[10],
                            "alergia": linha[11],
                            "gestante": linha[12],
                            "motivo": linha[13]
                        }
                    }
    except FileNotFoundError:
        return None

def comparar_respostas(consulta_anterior, consulta_atual):
    #responsavel por comparar as respostas da triagem atual com a triagem anterior, caso haja alguma mudança significativa, o sistema deve alertar o profissional de saúde.
    alertas = []
    for chave in consulta_atual:
        if chave in consulta_anterior and consulta_atual[chave] != consulta_anterior[chave]:
            alertas.append(f"Alteração na resposta para {chave}: {consulta_anterior.get(chave, 'não')} -> {consulta_atual[chave]}")
    return alertas

def salvar_consulta(cpf, nome, data_nascimento, triagem, anamnese):
    #responsavel por salvar as informações da consulta atual em um arquivo CSV, incluindo a data e hora da consulta para histórico do paciente.
    with open("pacientes.csv", "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([cpf, nome, data_nascimento, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), triagem["dor"], triagem["inchaco"], triagem["trauma"], triagem["sensibilidade"], triagem["sangramento"], anamnese["doenca"], anamnese["medicamento"], anamnese["alergia"], anamnese["gestante"], anamnese["motivo"]])


if __name__ == "__main__":
    main()