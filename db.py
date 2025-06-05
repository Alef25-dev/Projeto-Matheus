import psycopg2

# Configurações do banco
db_config = {
    'dbname': 'projeto_matheus',
    'user': 'postgres',
    'password': 'alefmc95',
    'host': 'localhost',
    'port': '5432'
}

# Função para abrir conexão
def get_connection():
    return psycopg2.connect(**db_config)
