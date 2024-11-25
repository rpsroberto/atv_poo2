from abc import ABC, abstractmethod

# Classe base abstrata para Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

# Subclasse UsuarioComum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.esta_disponivel():
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"Livro '{livro.titulo}' emprestado com sucesso!")
        else:
            print("Empréstimo não pode ser realizado.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"Livro '{livro.titulo}' devolvido com sucesso!")
        else:
            print("O livro não está na lista de empréstimos.")

# Subclasse Administrador
class Administrador(Pessoa):
    def cadastrar_livro(self, biblioteca, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

# Classe base abstrata para ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def esta_disponivel(self):
        pass

# Subclasse Livro
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor)
        self.ano = ano

    def esta_disponivel(self):
        return self.disponivel

# Classe Biblioteca para Gerenciar o Sistema
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            if livro.esta_disponivel():
                print(f" - {livro.titulo} ({livro.ano}) por {livro.autor}")

    def listar_usuarios_com_emprestimos(self):
        print("Usuários com livros emprestados:")
        for usuario in self.usuarios:
            if usuario.livros_emprestados:
                print(f" - {usuario.nome} ({usuario.matricula}): {[livro.titulo for livro in usuario.livros_emprestados]}")

# Exemplo de Uso
if __name__ == "__main__":
    biblioteca = Biblioteca()
    admin = Administrador("João", 35, "ADM001")

    # Cadastro de livros
    admin.cadastrar_livro(biblioteca, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    admin.cadastrar_livro(biblioteca, "1984", "George Orwell", 1949)

    # Cadastro de usuário
    usuario = UsuarioComum("Maria", 23, "USR123")
    biblioteca.cadastrar_usuario(usuario)

    # Empréstimos e Devoluções
    biblioteca.listar_livros_disponiveis()
    usuario.emprestar_livro(biblioteca.livros[0])
    biblioteca.listar_livros_disponiveis()
    usuario.devolver_livro(biblioteca.livros[0])
    biblioteca.listar_livros_disponiveis()

    # Relatórios
    biblioteca.listar_usuarios_com_emprestimos()
