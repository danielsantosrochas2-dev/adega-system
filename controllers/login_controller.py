from repositories.usuario_repository import cadastro_usuario
from repositories.usuario_repository import validar_login
from repositories.usuario_repository import buscar_usuario

def validar_acesso(usuario, senha):
    usuario_encontrado = validar_login(usuario, senha)

    if usuario_encontrado is None:
        return "Acesso Negado"

    return "Acesso Liberado"

# Valida os dados informados pelo usuario para criar um cadastro

def dados_cadastro(usuario, nome, senha, perfil):

  if not usuario or not nome or not senha or not perfil:
    return "Erro, não deixe em branco"
  else: 
    cadastro_usuario(usuario, nome, senha, perfil)
    return "Cadastro realizado com sucesso"

# Tratamento de erro
  
def dados_login(usuario, senha):

   if not usuario or not senha:
      return "Preencha todos os campos"

   resultado = validar_login(usuario, senha)

   if resultado: 
    return "Login realizado com sucesso"

   return "Usuario ou senha inválidos"

# Validar sessão se ativa ou não

usuario_logado = None

def validar_sessao(usuario, senha):
  global usuario_logado

  usuario_encontrado = validar_login(usuario, senha)

  if usuario_encontrado is None:
    return "Acesso Negado"

  usuario_logado = usuario_encontrado
  return "Acesso Liberado"

# Permissão usuario Administrador x Comum

usuario_administrador = False

def permissao_usuario(id):
 global usuario_administrador

 usuario = buscar_usuario(id)

 if usuario is None:
  return "Usuario não encontrado"

 if usuario["perfil"] == "Administrador":
   usuario_administrador = True
   return "Acesso Liberado"

 usuario_administrador = False
 return "Acesso Negado"

# Logout

usuario_logado = None
def logout():
  global usuario_logado

  usuario_logado = None

  return "Logout realizado com sucesso"

