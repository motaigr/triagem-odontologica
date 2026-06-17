from datetime import datetime
import os

from dental_triagem import comparar_respostas, salvar_consulta, busca_por_paciente

#python -m pytest test_dental_triagem.py -v

# Funções não testadas: entrada_paciente e main
# Motivo: essas funções dependem de input() do usuário,
# o que as torna não testáveis com pytest.
# A lógica principal está nas funções testadas acima.



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

def test_salvar_consulta():
    cpf = "12345678900"
    nome = "João da Silva"
    data_nascimento = "01/01/1990"
    triagem = {"dor": "sim", "inchaco": "não", "trauma": "não", "sensibilidade": "sim", "sangramento": "não"}
    anamnese = {"doenca": "não", "medicamento": "não", "alergia": "não", "gestante": "não", "motivo": "check-up"}

    salvar_consulta(cpf, nome, data_nascimento, triagem, anamnese)

    assert os.path.exists("pacientes.csv")

    # verifica se o CPF foi salvo corretamente
    with open("pacientes.csv", "r", encoding="utf-8") as f:
        conteudo = f.read()
        assert cpf in conteudo

def test_busca_por_paciente(tmp_path):
    arquivo = tmp_path / "pacientes.csv"
    arquivo.write_text("12345678900,João Silva,01/01/1990,12/06/2026 00:00:00,sim,não,não,sim,não,não,não,não,não,check-up\n", encoding="utf-8")
    
    resultado = busca_por_paciente("12345678900", caminho=str(arquivo))
    
    assert resultado is not None
    assert resultado["nome"] == "João Silva"