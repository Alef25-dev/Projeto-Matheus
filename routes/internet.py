from flask import Blueprint, jsonify
from db import get_connection

internet_bp = Blueprint('internet_bp', __name__)

@internet_bp.route('/internet/<int:co_municipio>')
def internet_por_municipio(co_municipio):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                no_regiao,
                no_uf,
                no_municipio,
                SUM(in_acesso_internet_computador) AS total_internet
            FROM microdados_ed_basica_2024
            WHERE co_municipio = %s
            GROUP BY no_regiao, no_uf, no_municipio
        """, (co_municipio,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado is None:
            return jsonify({
                "error": "Município não encontrado ou sem registros.",
                "co_municipio": co_municipio
            }), 404

        no_regiao, no_uf, no_municipio, total_internet = resultado
        return jsonify({
            "co_municipio": co_municipio,
            "no_regiao": no_regiao,
            "no_uf": no_uf,
            "no_municipio": no_municipio,
            "total_in_acesso_internet_computador": int(total_internet)
        })
    except Exception as e:
        return jsonify({
            "error": "Erro ao consultar o banco de dados",
            "detalhes": str(e)
        }), 500
