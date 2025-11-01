from database import get_cursor

def add_patient():
    patient_name = input('Digite o Nome do paciente > ').title()
    date_birth = input('Digite a Data de Nascimento do Paciente > ')
    gender = input('Digite o gênero M/F > ').upper()
    number = input('Digite o numero de telefone > ')
    address = input('Digite o endereço > ')
    with get_cursor() as cursor:
        cursor.execute("""
            INSERT INTO patients (full_name, date_of_birth, gender, phone, address)
                VALUES
                (%s, %s, %s, %s, %s);
    """, (patient_name, date_birth, gender, number, address))
    print('Paciente adicionado com sucesso !')

def list_patients():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM patients WHERE active = TRUE;")
        for linha in cursor.fetchall():
            print(linha)

def exclusion_patients():
    id_exclusion = int(input('Digite o ID do paciente a ser excluido > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM patients WHERE id = %s AND active = TRUE;", (id_exclusion,))
        if cursor.fetchone() is None:
            print('Paciente não encontrado ou já inativo.')
            return
        cursor.execute("UPDATE patients SET active = FALSE WHERE id = %s;", (id_exclusion,))
    print('Paciente excluido !')

def edit_patients():
    id_edit = int(input('Digite o ID do paciente a ser editado > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM patients WHERE id = %s AND active = TRUE;", (id_edit,))
        if cursor.fetchone() is None:
            print('Paciente não encontrado ou inativo.')
            return
        new_full_name = input('Digite o novo nome a ser adicionado > ').title()
        cursor.execute("""
                        UPDATE patients 
                        SET full_name = %s 
                        WHERE id = %s;
                    """, (new_full_name, id_edit))
    print('Nome do paciente editado !')