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
    while True:
        cpf = input("Digite o CPF do paciente (somente os números):")
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("CPF inválido. Digite somente os 11 números do CPF.")

    paciente = busca_por_paciente(cpf)

    is_novo = paciente is None

    if paciente:
        print(f"Paciente encontrado: {paciente['nome']}")
    else:
        print(f"Paciente não encontrado, siga com o cadastro")
        paciente = {}
        paciente["nome"] = input("Digite o nome do paciente:")
        paciente["data_nascimento"] = perguntar_data("Digite a data de nascimento:")

    triagem = {}
    triagem["dor"] = perguntar_sim_nao("Está sentindo dor no momento?")
    triagem["inchaco"] = perguntar_sim_nao("Há inchaço no rosto ou gengiva?")
    triagem["trauma"] = perguntar_sim_nao("Houve trauma recente?")
    triagem["sensibilidade"] = perguntar_sim_nao("Apresenta sensibilidade ao quente ou frio?")
    triagem["sangramento"] = perguntar_sim_nao("Existe sangramento gengival espontâneo ou constante?")

    anamnese = {}
    anamnese["doenca"] = perguntar_sim_nao("Possui doença crônica? ")
    anamnese["medicamento"] = perguntar_sim_nao("Faz uso contínuo de medicamento?")
    anamnese["alergia"] = perguntar_sim_nao("Possui alergia a medicamentos?")
    anamnese["gestante"] = perguntar_sim_nao("É gestante?")
    anamnese["motivo"] = input("Qual o motivo principal da sua consulta hoje?")

    if not is_novo:
        comparacao = comparar_respostas(paciente["triagem"], triagem)
        for alerta in comparacao:
            print(f"Alerta: {alerta}")
    salvar_consulta(cpf, paciente["nome"], paciente["data_nascimento"], triagem, anamnese)
    

def busca_por_paciente(cpf, caminho="pacientes.csv"):
    #responsavel por verificar se o paciente já tem cadastro, caso tenha, retornar os linha do cliente para iniciar a consulta.
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if len(linha) == 0 or linha[0] == "cpf":
                    continue
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

def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (sim/não): ").strip().lower()
        if resposta in ("sim", "não", "nao"):
            if resposta == "nao":
                resposta = "não"
            return resposta
        print("Resposta inválida. Digite apenas 'sim' ou 'não'.")

def perguntar_data(pergunta):
    while True:
        data = input(pergunta + " (DD/MM/AAAA): ").strip()
        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA com números.")

if __name__ == "__main__":
    main()