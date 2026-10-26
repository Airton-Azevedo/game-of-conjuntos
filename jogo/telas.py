import pygame


def desenhar_texto(surface, text, pos, font, color, align="center"):
    if text is None:
        return None
    render = font.render(str(text), True, color)
    rect = render.get_rect()
    if align == "center":
        rect.center = pos
    elif align == "midleft":
        rect.midleft = pos
    elif align == "midright":
        rect.midright = pos
    elif align == "topleft":
        rect.topleft = pos
    elif align == "topcenter":
        rect.midtop = pos
    else:
        rect.center = pos
    surface.blit(render, rect)
    return rect


def quebrar_texto(texto, max_width, font):
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = f"{linha_atual} {palavra}".strip()
        if font.size(teste)[0] <= max_width:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas


class Botao:
    def __init__(self, x, y, largura, altura, texto, cor, callback=None, font=None, text_color=(255, 255, 255), radius=18):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.callback = callback
        self.font = font or pygame.font.SysFont("arial", 22, bold=True)
        self.text_color = text_color
        self.hover = False
        self.radius = radius

    def atualizar(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def clicar(self):
        if self.callback is not None:
            self.callback()

    def desenhar(self, surface):
        cor_atual = self.cor
        if self.hover:
            cor_atual = tuple(min(255, max(0, c + 28)) for c in self.cor)
        pygame.draw.rect(surface, cor_atual, self.rect, border_radius=self.radius)
        pygame.draw.rect(surface, (255, 255, 255, 80), self.rect, 2, border_radius=self.radius)
        desenhar_texto(surface, self.texto, self.rect.center, self.font, self.text_color, align="center")


class Cartao:
    def __init__(self, x, y, largura, altura, titulo, texto="", color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.titulo = titulo
        self.texto = texto
        self.color = color

    def desenhar(self, surface, font_titulo=None, font_texto=None):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=20)
        pygame.draw.rect(surface, (255, 255, 255, 60), self.rect, 2, border_radius=20)
        if font_titulo is not None:
            desenhar_texto(surface, self.titulo, (self.rect.centerx, self.rect.y + 26), font_titulo, (255, 255, 255), align="center")
        if self.texto and font_texto is not None:
            linhas = quebrar_texto(self.texto, self.rect.width - 28, font_texto)
            y = self.rect.y + 58
            for linha in linhas[:4]:
                desenhar_texto(surface, linha, (self.rect.centerx, y), font_texto, (240, 245, 255), align="center")
                y += font_texto.get_linesize() + 6


class BarraCronometro:
    def __init__(self, x, y, largura, altura=18):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor_bg = (35, 58, 78)
        self.cor_fill = (110, 236, 180)

    def atualizar(self, valor, valor_total):
        self.valor = valor
        self.valor_total = valor_total

    def desenhar(self, surface):
        pygame.draw.rect(surface, self.cor_bg, self.rect, border_radius=10)
        largura = max(0, (self.valor / self.valor_total) * self.rect.width) if self.valor_total else 0
        fill = pygame.Rect(self.rect.x, self.rect.y, largura, self.rect.height)
        pygame.draw.rect(surface, self.cor_fill, fill, border_radius=10)


class DiagramaVenn:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self, surface, a_texto="A", b_texto="B", cor_a=(72, 196, 142), cor_b=(79, 129, 255)):
        centro_a = (self.x + self.largura * 0.38, self.y + self.altura / 2)
        centro_b = (self.x + self.largura * 0.62, self.y + self.altura / 2)
        raio_x = self.largura * 0.28
        raio_y = self.altura * 0.42

        pygame.draw.ellipse(surface, (*cor_a, 110), (centro_a[0] - raio_x, centro_a[1] - raio_y, raio_x * 2, raio_y * 2))
        pygame.draw.ellipse(surface, (*cor_b, 110), (centro_b[0] - raio_x, centro_b[1] - raio_y, raio_x * 2, raio_y * 2))

        pygame.draw.ellipse(surface, cor_a, (centro_a[0] - raio_x, centro_a[1] - raio_y, raio_x * 2, raio_y * 2), 2)
        pygame.draw.ellipse(surface, cor_b, (centro_b[0] - raio_x, centro_b[1] - raio_y, raio_x * 2, raio_y * 2), 2)

        font = pygame.font.SysFont("arial", 28, bold=True)
        desenhar_texto(surface, a_texto, centro_a, font, (255, 255, 255), align="center")
        desenhar_texto(surface, b_texto, centro_b, font, (255, 255, 255), align="center")
