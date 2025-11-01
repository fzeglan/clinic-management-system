from database import get_cursor

def add_doctor():
    full_name_doctor = input('Digite o nome do Dr(a) > ').title()
    phone = input('Digite o telefone > ')
    with get_cursor() as cursor:
        cursor.execute("""
            INSERT INTO doctors (full_name, phone)
                VALUES
                    (%s, %s);
    """, (full_name_doctor, phone))
    print('Doutor(a) adicionado com sucesso !')

def list_doctors():
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT * FROM doctors WHERE active = TRUE;
    """)
        print('### Lista de Doutores ###')
        for line in cursor.fetchall():
            print(line)

def edit_doctors():
    id_edit = int(input('Digite o ID do Doutor(a) a ser editado > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM doctors WHERE id = %s AND active = TRUE;", (id_edit,))
        if cursor.fetchone() is None:
            print('Doutor(a) não encontrado ou inativo.')
            return
        new_full_name = input('Digite o novo nome > ').title()
        cursor.execute("""
            UPDATE doctors 
            SET full_name = %s 
            WHERE id = %s;
""", (new_full_name, id_edit))
    print('Nome do Doutor(a) editado com sucesso ! ')

def exclusion_doctors():
    id_exclusion = int(input('Digite o ID do doutor(a) a ser excluido > '))
    with get_cursor() as cursor:
        cursor.execute("SELECT id FROM doctors WHERE id = %s AND active = TRUE;", (id_exclusion,))
        if cursor.fetchone() is None:
            print('Dr(a) não encontrado ou já inativo.')
            return
        cursor.execute("""
            UPDATE doctors SET active = FALSE WHERE id = %s;
    """, (id_exclusion,))
    print('Doutor(a) desativado com sucesso !')