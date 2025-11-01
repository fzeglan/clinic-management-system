from database import get_cursor
from datetime import date


def add_consultation():
    patient_id = int(input('Digite o ID do paciente > '))
    doctor_id = int(input('Digite o ID do Doutor > '))
    consultation_date = date.today()
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM patients WHERE id = %s AND active = TRUE;",(patient_id,))
        if cursor.fetchone() is None:
            print('ID informado não pertence a nenhum paciente.')
            return
        cursor.execute("SELECT id FROM doctors WHERE id = %s AND active = TRUE;", (doctor_id,))
        if cursor.fetchone() is None:
            print('ID informado não pertence a nenhum Dr(a).')
            return
        service_type = input('Digite o Tipo de Serviço [SUS/PLANOSAUDE/PARTICULAR] >')
        obs = input('Campo para Observações > ')
        cursor.execute("""
        INSERT INTO consultations (patient_id, doctor_id, consultation_date, observations, service_type)
            VALUES
            (%s, %s, %s, %s, %s);
    """, (patient_id, doctor_id, consultation_date, obs, service_type))
    print('Consulta Adicionada com Sucesso !')

def listing_consultation():
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT * FROM consultations WHERE active = TRUE;
    """) 
        for line in cursor.fetchall():
            print(line)

def exclusion_consultation():
    consultation_id = int(input('Digite o ID da consulta > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM consultations WHERE id = %s AND active = TRUE;", (consultation_id,))
        if cursor.fetchone() is None:
            print('Consulta não encontrada ou já inativa.')
            return
        cursor.execute("""
            UPDATE consultations SET active = FALSE WHERE id = %s;
    """, (consultation_id,))
    print('Excluido com Sucesso !')