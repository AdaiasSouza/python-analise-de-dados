import sqlite3
"""
    1. Conectar ao banco de dados
    2. realizar uma consulta
    3. imprimir resultado
    4. Fechar conexao
"""

con = sqlite3.connect("db_exemplo.db")
cursor = con.cursor()
res = cursor.execute("""SELECT dsc_categoria FROM tb_categoria""")
print(res.fetchall())
""" sempre fechar a conexao"""
cursor.close()
con.close()
