import pygame

from jogo import config as cfg
from jogo.telas import TelaInstrucoes, TelaMenu, TelaPergunta, TelaResultado


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((cfg.LARGURA, cfg.ALTURA))
        pygame.display.set_caption("Conjuntos em Jogo")
        self.clock = pygame.time.Clock()
        self.running = True
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.tela_atual = TelaMenu(self)
        self.sons = cfg.carregar_sons()

    def tocar(self, nome):
        som = self.sons.get(nome)
        if som is not None:
            som.play()

    def iniciar_jogo(self):
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.tela_atual = TelaPergunta(self)

    def mostrar_instrucoes(self):
        self.tela_atual = TelaInstrucoes(self)

    def tela_menu(self):
        self.tela_atual = TelaMenu(self)

    def mostrar_resultado(self):
        self.tela_atual = TelaResultado(self)

    def encerrar(self):
        self.running = False

    def rodar(self):
        while self.running:
            dt = self.clock.tick(cfg.FPS) / 1000.0
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.encerrar()
                else:
                    self.tela_atual.tratar_evento(evento)

            self.tela_atual.atualizar(dt)
            self.tela_atual.desenhar(self.tela)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.rodar()
