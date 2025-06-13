from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import io
from db import get_connection

# import do blueprint
from routes.internet import internet_bp
from routes.enem import enem_bp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Registra o blueprint das rotas /internet
app.register_blueprint(internet_bp)
# Registra o blueprint das rotas /enem
app.register_blueprint(enem_bp)

# --- Resto das rotas diretamente aqui, se quiser ---
@app.route('/')
def index():
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        # Get the search parameter
        municipio = request.args.get('municipio', '')
        
        if municipio:
            # If there's a search term, filter by municipality name
            cur.execute("""
                SELECT * FROM dados_enem 
                WHERE LOWER(no_municipio_esc) LIKE LOWER(%s)
                LIMIT 1000
            """, (f'%{municipio}%',))
        else:
            # If no search term, get all records
            cur.execute("SELECT * FROM dados_enem LIMIT 1000")
            
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
        cur.execute("SELECT * FROM dados_enem")
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
            headers={"Content-Disposition": "attachment;filename=dados_enem.csv"}
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
                INSERT INTO dados_enem (
    nu_ano, co_uf_esc, sg_uf_esc, co_municipio_esc, no_municipio_esc,
    humanas, natureza, linguagens, matematica,
    fed_priv, est_mun, s_pc, n_pc, s_cel, n_cel,
    s_int, n_int, cor_bra_ama, cor_outros, masculino, feminino
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
            """, row)
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    # Se for GET, renderiza a página de importação
    return render_template('importar.html')

if __name__ == '__main__':
    app.run(debug=True)
