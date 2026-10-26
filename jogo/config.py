import pygame

LARGURA = 1280
ALTURA = 720
FPS = 60

COR_BG = (14, 22, 34)
COR_PAINEL = (21, 37, 56)
COR_PAINEL_2 = (29, 49, 72)
COR_PRIMARIA = (72, 196, 142)
COR_SECUNDARIA = (79, 129, 255)
COR_ALERTA = (255, 173, 66)
COR_ERRO = (232, 93, 93)
COR_TEXTO = (240, 245, 255)
COR_MUTED = (174, 188, 214)
COR_BORDA = (102, 132, 170)

SONS = {
    "clique": None,
    "acerto": None,
    "erro": None,
}


def carregar_sons():
    sons = {}
    if not pygame.mixer.get_init():
        return sons
    for nome, caminho in {
        "clique": "assets/clique.wav",
        "acerto": "assets/acerto.wav",
        "erro": "assets/erro.wav",
    }.items():
        try:
            sons[nome] = pygame.mixer.Sound(caminho)
        except Exception:
            sons[nome] = None
    return sons
