from dental_triagem import comparar_respostas

def test_comparar_respostas():
    # monta os dados de entrada
    anterior = {"dor": "não", "inchaco": "sim"}
    atual = {"dor": "sim", "inchaco": "sim"}
    
    # chama a função
    resultado = comparar_respostas(anterior, atual)
    
    # verifica o resultado
    assert len(resultado) == 1
    assert "dor" in resultado[0]

    # segundo cenário - sem divergências
    anterior2 = {"dor": "sim", "inchaco": "não"}
    atual2 = {"dor": "sim", "inchaco": "não"}

    resultado2 = comparar_respostas(anterior2, atual2)

    assert len(resultado2) == 0

def salvar_consulta(cpf, nome, data_nascimento, triagem, anamnese):
    #responsavel por salvar os dados da consulta em um arquivo csv
    with open("pacientes.csv", "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            cpf,
            nome,
            data_nascimento,
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            triagem["dor"],
            triagem["inchaco"],
            triagem["trauma"],
            triagem["sensibilidade"],
            triagem["sangramento"],
            anamnese["doenca"],
            anamnese["medicamento"],
            anamnese["alergia"],
            anamnese["gestante"],
            anamnese["motivo"]
        ])

    assert os.path.exists("pacientes.csv")