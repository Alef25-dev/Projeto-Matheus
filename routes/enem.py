from flask import Blueprint, jsonify, render_template, request
from db import get_connection

enem_bp = Blueprint('enem_bp', __name__)

@enem_bp.route('/enem/humanas/')
@enem_bp.route('/enem/humanas/<int:co_municipio>')
def humanas_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Ciências Humanas")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                AVG(humanas) AS media_humanas
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Ciências Humanas"
            )

        sg_uf_esc, no_municipio_esc, media_humanas = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Média em Ciências Humanas",
            metric_value=f"{float(media_humanas):.2f}",
            titulo="Ciências Humanas"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Ciências Humanas"
        )

@enem_bp.route('/enem/natureza/')
@enem_bp.route('/enem/natureza/<int:co_municipio>')
def natureza_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Ciências da Natureza")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                AVG(natureza) AS media_natureza
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Ciências da Natureza"
            )

        sg_uf_esc, no_municipio_esc, media_natureza = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Média em Ciências da Natureza",
            metric_value=f"{float(media_natureza):.2f}",
            titulo="Ciências da Natureza"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Ciências da Natureza"
        )

@enem_bp.route('/enem/linguagens/')
@enem_bp.route('/enem/linguagens/<int:co_municipio>')
def linguagens_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Linguagens")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                AVG(linguagens) AS media_linguagens
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Linguagens"
            )

        sg_uf_esc, no_municipio_esc, media_linguagens = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Média em Linguagens",
            metric_value=f"{float(media_linguagens):.2f}",
            titulo="Linguagens"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Linguagens"
        )

@enem_bp.route('/enem/matematica/')
@enem_bp.route('/enem/matematica/<int:co_municipio>')
def matematica_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Matemática")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                AVG(matematica) AS media_matematica
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Matemática"
            )

        sg_uf_esc, no_municipio_esc, media_matematica = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Média em Matemática",
            metric_value=f"{float(media_matematica):.2f}",
            titulo="Matemática"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Matemática"
        )

@enem_bp.route('/enem/fed_priv/')
@enem_bp.route('/enem/fed_priv/<int:co_municipio>')
def fed_priv_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Escolas Federais/Particulares")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(fed_priv) AS total_fed_priv
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Escolas Federais/Particulares"
            )

        sg_uf_esc, no_municipio_esc, total_fed_priv = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Escolas Federais/Particulares",
            metric_value=int(total_fed_priv),
            titulo="Escolas Federais/Particulares"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Escolas Federais/Particulares"
        )

@enem_bp.route('/enem/est_mun/')
@enem_bp.route('/enem/est_mun/<int:co_municipio>')
def est_mun_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Escolas Estaduais/Municipais")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(est_mun) AS total_est_mun
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Escolas Estaduais/Municipais"
            )

        sg_uf_esc, no_municipio_esc, total_est_mun = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Escolas Estaduais/Municipais",
            metric_value=int(total_est_mun),
            titulo="Escolas Estaduais/Municipais"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Escolas Estaduais/Municipais"
        )

@enem_bp.route('/enem/s_pc/')
@enem_bp.route('/enem/s_pc/<int:co_municipio>')
def s_pc_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Acesso a Computador")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(s_pc) AS total_s_pc
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Acesso a Computador"
            )

        sg_uf_esc, no_municipio_esc, total_s_pc = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos com Acesso a Computador",
            metric_value=int(total_s_pc),
            titulo="Acesso a Computador"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Acesso a Computador"
        )

@enem_bp.route('/enem/n_pc/')
@enem_bp.route('/enem/n_pc/<int:co_municipio>')
def n_pc_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Sem Acesso a Computador")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(n_pc) AS total_n_pc
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Sem Acesso a Computador"
            )

        sg_uf_esc, no_municipio_esc, total_n_pc = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos sem Acesso a Computador",
            metric_value=int(total_n_pc),
            titulo="Sem Acesso a Computador"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Sem Acesso a Computador"
        )

@enem_bp.route('/enem/s_cel/')
@enem_bp.route('/enem/s_cel/<int:co_municipio>')
def s_cel_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Acesso a Celular")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(s_cel) AS total_s_cel
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Acesso a Celular"
            )

        sg_uf_esc, no_municipio_esc, total_s_cel = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos com Acesso a Celular",
            metric_value=int(total_s_cel),
            titulo="Acesso a Celular"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Acesso a Celular"
        )

@enem_bp.route('/enem/n_cel/')
@enem_bp.route('/enem/n_cel/<int:co_municipio>')
def n_cel_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Sem Acesso a Celular")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(n_cel) AS total_n_cel
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Sem Acesso a Celular"
            )

        sg_uf_esc, no_municipio_esc, total_n_cel = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos sem Acesso a Celular",
            metric_value=int(total_n_cel),
            titulo="Sem Acesso a Celular"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Sem Acesso a Celular"
        )

@enem_bp.route('/enem/s_int/')
@enem_bp.route('/enem/s_int/<int:co_municipio>')
def s_int_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Acesso à Internet")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(s_int) AS total_s_int
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Acesso à Internet"
            )

        sg_uf_esc, no_municipio_esc, total_s_int = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos com Acesso à Internet",
            metric_value=int(total_s_int),
            titulo="Acesso à Internet"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Acesso à Internet"
        )

@enem_bp.route('/enem/n_int/')
@enem_bp.route('/enem/n_int/<int:co_municipio>')
def n_int_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Sem Acesso à Internet")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(n_int) AS total_n_int
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Sem Acesso à Internet"
            )

        sg_uf_esc, no_municipio_esc, total_n_int = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos sem Acesso à Internet",
            metric_value=int(total_n_int),
            titulo="Sem Acesso à Internet"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Sem Acesso à Internet"
        )

@enem_bp.route('/enem/cor_bra_ama/')
@enem_bp.route('/enem/cor_bra_ama/<int:co_municipio>')
def cor_bra_ama_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Alunos Brancos/Amarelos")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(cor_bra_ama) AS total_cor_bra_ama
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Alunos Brancos/Amarelos"
            )

        sg_uf_esc, no_municipio_esc, total_cor_bra_ama = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos Brancos/Amarelos",
            metric_value=int(total_cor_bra_ama),
            titulo="Alunos Brancos/Amarelos"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Alunos Brancos/Amarelos"
        )

@enem_bp.route('/enem/cor_outros/')
@enem_bp.route('/enem/cor_outros/<int:co_municipio>')
def cor_outros_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Alunos de Outras Raças")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(cor_outros) AS total_cor_outros
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Alunos de Outras Raças"
            )

        sg_uf_esc, no_municipio_esc, total_cor_outros = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos de Outras Raças",
            metric_value=int(total_cor_outros),
            titulo="Alunos de Outras Raças"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Alunos de Outras Raças"
        )

@enem_bp.route('/enem/masculino/')
@enem_bp.route('/enem/masculino/<int:co_municipio>')
def masculino_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Alunos do Sexo Masculino")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(masculino) AS total_masculino
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Alunos do Sexo Masculino"
            )

        sg_uf_esc, no_municipio_esc, total_masculino = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos do Sexo Masculino",
            metric_value=int(total_masculino),
            titulo="Alunos do Sexo Masculino"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Alunos do Sexo Masculino"
        )

@enem_bp.route('/enem/feminino/')
@enem_bp.route('/enem/feminino/<int:co_municipio>')
def feminino_por_municipio(co_municipio=None):
    if co_municipio is None:
        return render_template('detalhes.html', titulo="Alunos do Sexo Feminino")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                sg_uf_esc,
                no_municipio_esc,
                SUM(feminino) AS total_feminino
            FROM dados_enem
            WHERE co_municipio_esc = %s
            GROUP BY sg_uf_esc, no_municipio_esc
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return render_template('detalhes.html',
                co_municipio=co_municipio,
                error="Município não encontrado ou sem registros.",
                titulo="Alunos do Sexo Feminino"
            )

        sg_uf_esc, no_municipio_esc, total_feminino = resultado
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            uf=sg_uf_esc,
            municipio=no_municipio_esc,
            metric_name="Total de Alunos do Sexo Feminino",
            metric_value=int(total_feminino),
            titulo="Alunos do Sexo Feminino"
        )
    except Exception as e:
        return render_template('detalhes.html',
            co_municipio=co_municipio,
            error=f"Erro ao consultar o banco de dados: {str(e)}",
            titulo="Alunos do Sexo Feminino"
        ) 