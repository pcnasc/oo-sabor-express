"""Define a classe Avaliacao, que representa uma avaliação de restaurante."""

class Avaliacao:
    """Classe que representa a avaliação feita por um cliente a um restaurante."""

    def __init__(self, cliente, nota):
        """
        Inicializa uma nova avaliação.

        Args:
            cliente (str): Nome do cliente.
            nota (float): Nota atribuída (de 0 a 5).

        Raises:
            ValueError: Se a nota estiver fora do intervalo permitido (0 a 5).
        """
        if nota < 0 or nota > 5:
            raise ValueError('Nota deve ser entre 0 e 5')
        self._cliente = cliente
        self._nota = nota

    @property
    def cliente(self):
        """Retorna o nome do cliente que avaliou."""
        return self._cliente

    @property
    def nota(self):
        """Retorna a nota atribuída pelo cliente."""
        return self._nota

    def __str__(self):
        """Retorna a avaliação em formato legível."""
        return f'Avaliação de {self.cliente}: {self.nota} estrelas'