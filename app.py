"""Módulo principal para execução da aplicação de gerenciamento de restaurantes."""

from modelos.restaurante import Restaurante

# Criação de instâncias de restaurantes
restaurante_praca = Restaurante('Praça', 'GOURMET')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonês')

# Testes de avaliação (uma válida, duas inválidas)
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Ana', 8)
restaurante_praca.receber_avaliacao('Carlos', 2)

def main():
    """Função principal que lista todos os restaurantes cadastrados."""
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()