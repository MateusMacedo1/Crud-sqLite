import sqlite3 as connector

conexao = connector.connect("fabrica543.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS devs (
               id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(60),
               area_atuacao VARCHAR(200),
               telefone VARCHAR(14)
)""")

# cursor.execute("""INSERT INTO devs (nome, area_atuacao, telefone) VALUES ('Joaozinho', 'Analista de dados', '6799999999')""")


nomeDev = input("Digite o nome do Desenvolvedor\n")
area = input("Digite a área de atuação do desenvolvedor\n")
tel = input("Digite o número do Desenvolvedor\n")

cursor.execute("""INSERT INTO devs (nome, area_atuacao, telefone) VALUES (?, ?, ?)""", (nomeDev, area, tel))
cursor.execute("""SELECT * FROM devs""")
dados = cursor.fetchall()

for desenvolvedores in dados:
    print(desenvolvedores)

conexao.commit()