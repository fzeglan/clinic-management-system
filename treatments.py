from database import get_cursor


def add_treatments():
    consultation_id = int(input('Digite o ID da consulta a ser vinculada > '))
    medications = input('Digite os medicamentos a serem utilizados > ')
    treatment_description = input('Digite como deve ser o tratamento > ')
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM consultations WHERE id = %s AND active = TRUE;", (consultation_id,))
        if cursor.fetchone() is None:
            print('ID informado não possui consulta ativa.')
            return
        cursor.execute("""
            INSERT INTO treatments (consultation_id, medications, treatment_description)
                VALUES
                    (%s, %s, %s);
    """, (consultation_id, medications, treatment_description))
    print('Tratamento adicionado a consulta !')

def exclusion_treatments():
    treatments_id = int(input('Digite o ID do Tratamento a ser excluido > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM treatments WHERE id = %s", (treatments_id,))
        if cursor.fetchone() is None:
            print('Tratamento não encontrado ou já inativo.')
            return
        cursor.execute("""
            DELETE FROM treatments WHERE id = %s;
    """, (treatments_id,))
    print('Tratamento excluido !')