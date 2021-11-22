import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primeiro comentário da livroteca', 'Muito bom! Adorei o material...')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Segundo comentário', 'Exemplo de um segundo comentário')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Branca de Neve', 'Ficção', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/branca_de_neve_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Carlos Chagas', 'Biografias', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/chagas_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Chapeuzinho Vermelho', 'Ficção', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/chapeuzinho_vermelho_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Parlendas', 'Poesia', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/parlendas_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('A Cegonha e a Raposa', 'Ficção', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/a_cegonha_e_a_raposa_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Anna Nery', 'Biografias', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/anna_nery_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Bichos, Coisas e Lugares', 'Para Bebês', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/bichos_coisas_e_lugares_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Cantigas', 'Poesia', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/cantigas_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('O Rei e a Flauta', 'Ficção', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/o_rei_e_a_flauta_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('O Vento', 'Somente com imagens', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/o_vento_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Água', 'Informativos', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/agua_informativo_versao_digital.pdf')
            )

cur.execute("INSERT INTO books (title, category, url) VALUES (?, ?, ?)",
            ('Trava-Línguas', 'Poesia', 'http://alfabetizacao.mec.gov.br/images/conta-pra-mim/livros/versao_digital/trava_lingua_versao_digital.pdf')
            )


connection.commit()
connection.close()
