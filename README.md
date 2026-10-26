# Conjuntos em Jogo

Quiz educativo de **Matemática Discreta** para o Ensino Médio, feito em **Python + Pygame**. O jogo trabalha a definição de conjuntos, a pertinência entre elemento e conjunto, os subconjuntos, a união, a interseção e o complemento, sempre apoiado por diagramas de Venn e por explicações depois de cada resposta.

O projeto foi pensado para o Trabalho Aplicado – AV2 e pode ser executado localmente ou publicado no GitHub.

![Tela inicial](screenshots/01_menu.png)

## Sobre o jogo

São **12 perguntas de múltipla escolha**, com **30 segundos** para responder cada uma. O jogador escolhe entre quatro alternativas e, em seguida, recebe a correção com uma explicação curta do conceito. Ao final, o jogo mostra a pontuação, o aproveitamento, a melhor sequência de acertos, o tempo total e os temas que merecem revisão.

O visual foi construído com uma identidade própria: fundo escuro, cartões claros, cores de apoio e diagramas de Venn desenhados especificamente para cada questão.

| Quiz | Feedback |
| --- | --- |
| ![Pergunta com diagrama](screenshots/04_quiz_diagrama.png) | ![Explicação após a resposta](screenshots/05_modal_acerto.png) |

| Instruções | Resultado |
| --- | --- |
| ![Instruções](screenshots/02_instrucoes.png) | ![Resultado final](screenshots/07_resultado.png) |

## Conteúdo abordado

- Definição de conjunto e relação de pertinência (`∈` e `∉`)
- Subconjuntos (`⊂`), incluindo o conjunto vazio
- União (`∪`) e interseção (`∩`)
- Complemento (`Aᶜ`) em relação ao conjunto universo
- Conjuntos disjuntos
- Leitura de diagramas de Venn
- Princípio da inclusão-exclusão para contagem de elementos

## Como jogar

| Ação | Mouse | Teclado |
| --- | --- | --- |
| Escolher alternativa | clique na opção | `1` a `4` ou `A` a `D` |
| Avançar após a correção | botão **Continuar** | `Enter` ou `Espaço` |
| Voltar ao menu | botão de seta | `Esc` |
| Tela cheia | — | `F11` |

### Pontuação

- **+10 pontos** por resposta correta;
- **+1 ponto** por segundo restante no cronômetro;
- **+10 pontos** extras a cada três acertos consecutivos.

O recorde fica salvo no arquivo `recorde.json`, criado automaticamente na primeira partida. Esse arquivo não deve ser enviado ao GitHub (já está no `.gitignore`).

## Como executar

Requisitos: **Python 3.9 ou superior** e o pacote **pygame-ce** (compatível com `import pygame`).

```bash
# 1. entre na pasta do projeto
cd jogo_conjuntos

# 2. crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# 3. instale a dependência
pip install -r requirements.txt

# 4. execute
python main.py
```

Também é possível usar os atalhos:

```bash
./executar.sh        # Linux/macOS
executar.bat         # Windows
```

Se aparecer algum erro relacionado a áudio, o jogo continua funcionando normalmente, apenas sem os efeitos sonoros.

## Executando no OneCompiler

O projeto também tem uma versão em **arquivo único**, pensada para colar direto no editor online:

1. Abra [onecompiler.com/python](https://onecompiler.com/python);
2. apague o conteúdo do arquivo `main.py` do editor;
3. copie todo o conteúdo de [`onecompiler/main.py`](onecompiler/main.py) deste repositório e cole no editor;
4. clique em **Run**.

Essa versão não depende de imagens, fontes ou sons externos: os diagramas e os cartões são desenhados com as próprias funções do Pygame, e as fontes vêm do sistema. O conteúdo das questões é o mesmo da versão completa.

> A versão completa, com os assets em alta resolução, é a recomendada para apresentação e para o GitHub.

## Estrutura do projeto

```text
jogo_conjuntos/
├── main.py                  # inicialização, navegação e laço principal
├── jogo/
│   ├── config.py            # cores, medidas, fontes e caminhos
│   ├── perguntas.py         # banco de questões, alternativas e explicações
│   ├── telas.py             # menu, instruções, quiz e resultado
│   └── ui.py                # botões, cartões, textos e barras
├── assets/
│   ├── fonts/               # Poppins e DejaVu Sans
│   ├── images/              # logotipo, fundo e diagramas de Venn
│   └── sounds/              # efeitos sonoros sintetizados
├── ferramentas/
│   ├── gerar_assets.py      # recria as imagens a partir do código
│   └── gerar_sons.py        # recria os efeitos sonoros
├── onecompiler/
│   └── main.py              # versão em arquivo único para uso online
├── screenshots/             # capturas usadas neste README
├── requirements.txt
├── executar.sh
├── executar.bat
├── LICENSE
└── README.md
```

## Recriando os assets

As imagens e os sons do jogo são gerados por scripts próprios, o que facilita ajustar cores, textos e formatos sem depender de arquivos externos.

```bash
pip install -r requirements-dev.txt
python ferramentas/gerar_assets.py
python ferramentas/gerar_sons.py
```

## Equipe

| Integrante | Responsabilidade |
| --- | --- |
| _preencher_ | _preencher_ |
| _preencher_ | _preencher_ |
| _preencher_ | _preencher_ |
| _preencher_ | _preencher_ |
| _preencher_ | _preencher_ |

## Créditos

- **Poppins** — fonte criada por Indian Type Foundry, distribuída sob a SIL Open Font License.
- **DejaVu Sans** — fonte livre usada para os símbolos matemáticos (`∈`, `∪`, `∩`, `⊂`, `∅`).
- Efeitos sonoros sintetizados com a biblioteca padrão `wave`, sem samples de terceiros.

## Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).
