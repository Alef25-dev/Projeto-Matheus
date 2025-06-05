from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import io
from db import get_connection

# import do blueprint
from routes.internet import internet_bp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Registra o blueprint das rotas /internet
app.register_blueprint(internet_bp)

# --- Resto das rotas diretamente aqui, se quiser ---
@app.route('/')
def index():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM microdados_ed_basica_2024 LIMIT 1000")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', dados=rows)
    except Exception as e:
        return f"Erro ao conectar ao banco: {e}"

@app.route('/exportar')
def exportar_csv():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM microdados_ed_basica_2024")
        dados = cur.fetchall()
        colunas = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(colunas)
        writer.writerows(dados)
        output.seek(0)

        return Response(
            output,
            mimetype='text/csv',
            headers={"Content-Disposition": "attachment;filename=microdados_2024.csv"}
        )
    except Exception as e:
        return f"Erro ao exportar: {e}"

@app.route('/importar', methods=['GET', 'POST'])
def importar():
    if request.method == 'POST':
        file = request.files['file']
        if not file or file.filename == '':
            return "Nenhum arquivo selecionado."

        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        reader = csv.reader(stream)
        next(reader)  # Pular o cabeçalho

        conn = get_connection()
        cur = conn.cursor()
        for row in reader:
            cur.execute("""
                INSERT INTO microdados_ed_basica_2024 (
                    nu_ano_censo, no_regiao, co_regiao,
                    no_uf, sg_uf, co_uf,
                    no_municipio, co_municipio, in_acesso_internet_computador
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    # Se for GET, renderiza a página de importação
    return render_template('importar.html')

if __name__ == '__main__':
    app.run(debug=True)
