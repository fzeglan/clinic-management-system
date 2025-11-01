from patients import add_patient, list_patients, edit_patients, exclusion_patients
from doctors import add_doctor, list_doctors, edit_doctors, exclusion_doctors
from consultations import add_consultation, exclusion_consultation, listing_consultation
from treatments import add_treatments, exclusion_treatments

def invalidacao():
    print('Opção inválida, escolha uma das opções acima.')


print("### SISTEMA CLÍNICO ###")
print("""
[1] Gerenciar Pacientes
[2] Gerenciar Médicos
[3] Gerenciar Consultas
[4] Gerenciar Tratamentos
""")

opcao = input("> ")

if opcao == '1':
    print("""
    [1] Adicionar Paciente
    [2] Listar Pacientes
    [3] Editar Paciente
    [4] Excluir Paciente
    """)

    sub = input("> ")

    if sub == "1":
        add_patient()
    elif sub == "2":
        list_patients()
    elif sub == "3":
        edit_patients()
    elif sub == "4":
        exclusion_patients()
    else:
        invalidacao()

elif opcao == '2':
    print("""
    [1] Adicionar Doutor(a)
    [2] Listar Doutores
    [3] Editar Doutores
    [4] Excluir Doutores
    """)

    sub = input("> ")

    if sub == '1':
        add_doctor()
    elif sub == '2':
        list_doctors()
    elif sub == '3':
        edit_doctors()
    elif sub == '4':
        exclusion_doctors()
    else:
        
        invalidacao()

elif opcao == '3':
    print("""
    [1] Adicionar Consulta
    [2] Listar Consultas
    [3] Excluir Consulta
    """)

    sub = input("> ")

    if sub == '1':
        add_consultation()
    elif sub == '2':
        listing_consultation()
    elif sub == '3':
        exclusion_consultation()
    else:
        invalidacao()

elif opcao == '4':
    print("""
    [1] Adicionar Tratamento
    [2] Excluir Tratamento
    """)

    sub = input("> ")

    if sub == '1':
        add_treatments()
    elif sub == '2':
        exclusion_treatments()
    else:
        invalidacao()

else:
    invalidacao()
