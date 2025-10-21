Para execução, a API deve rodar do arquivo app.py

1 - localhost principal não funciona, o recomendado é ir diretamente para as rotas.
2 - Nem todas as páginas tem botão para voltar ou ser direcionado para um menu
3 - Nesta API existem as rotas que apenas executam o HTTP(por exemplo o método GET
que é o único que dá pra executar via navegador), mas também tem as páginas HTML que executam as funções PUT,POST e DELETE.

4 - ROTAS(HTTP):
#Receber ou inserir(sobrescrever) : /users(GET e POST)
#Receber por id : /users/(id do usuário) | Método(GET)
#Atualizar por id : /users/(id do usuário) | Método(PUT)
#Deletar funcionario : /users/(id do usuário) | Método(DELETE)

5 - ROTAS(HTML):
#Criar usuário : /createUser
#Listar usuários : /listUsers
#Editar usuários : editUser

* As rotas hmtl foram criadas para fácil acesso das informações da API, para criar, editar e excluir usuários, porém, todo o processo pode ser observado no /users
