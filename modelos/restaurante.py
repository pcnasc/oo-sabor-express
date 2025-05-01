"""Define a classe Restaurante e suas funcionalidades relacionadas a avaliações e estado."""

from modelos.avaliacao import Avaliacao

class Restaurante:
    """Classe que representa um restaurante e armazena suas informações e avaliações."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa um novo restaurante.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria culinária do restaurante.
        """
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação legível do restaurante."""
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes cadastrados."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Indica se o restaurante está ativo ou inativo com emoji."""
        return '✅' if self._ativo else '💀'

    def alternar_estado(self):
        """Alterna o estado de ativo/inativo do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Recebe e armazena uma nova avaliação do restaurante.

        Args:
            cliente (str): Nome do cliente.
            nota (float): Nota da avaliação (entre 0 e 5).
        """
        try:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            print(f'Avaliação recebida: {avaliacao}')
        except ValueError as e:
            print(f'Erro ao registrar avaliação: {e}')

    @property
    def media_avaliacoes(self):
        """
        Calcula a média das avaliações recebidas.

        Returns:
            str: Média formatada com estrelas ou 'Sem avaliações' se nenhuma nota tiver sido registrada.
        """
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        media = round(soma_das_notas / len(self._avaliacao), 1)
        return f'{media} ⭐'