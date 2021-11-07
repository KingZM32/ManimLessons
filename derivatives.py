from manim import *
import numpy as np

# A insistir --> a derivada é uma taxa de variação infinitesimal de uma dada função f
# COMPREENDER O INFINITÉSIMO!!!


#PART01
#TODO: Texto da aula --> Apresentação do conceito formal
#TODO: Função polinomial em 0xy --> Taxa média de variação --> Noção intuitiva --> Noção formal
#TODO: Transform num gráfico 0tx --> Ponto a mover-se num referencial unidimensional
#TODO: Variação num instante --> paradoxo, não há duas medidas num instante --> então temos o "limite", quando a variação se torna mais pequena
#TODO: Variação infinitesimal --> Reta tangente ao gráfico da função --> Variação infinitesimal
#TODO: Acompanhar a derivada em cada ponto com o gráfico da derivada --> Replay da animação --> análise ruber-duck
#TODO: Apresentar a fórmula --> *FORMULA TEXT HERE* --> voltar a associar com a variação infinitesimal e tangente
#TODO: RECAP DOS CONCEITOS GERAIS
#TODO: FINISH UP PART 01
#PART02
#TODO: RECAP da aula anterior 
#TODO: Análise da monotonia recorrendo à derivada --> Reforçar a visualização dy/dx  --> Tabela --> Associar a tabela com o gráfico (Dot Mobject) --> replay
#TODO: Problema de otimização --> resolução acompanhada --> deduzir fórmulas em openboard --> passar à visualização
#TODO: RECAP DOS CONCEITOS GERAIS
#PART03: OPTIONAL
#TODO: DERIVAÇÃO DA REGRA DO POLINÓMIO
#TODO: FURTER RESEARCH --> VÍDEOS 3BLUE1BROWN SOBRE A CHAIN RULE E DERIVADAS

class Derivatives(Scene):
    def construct(self):

        def ll_pause(self):
            self.wait(10)

        def long_pause(self):
            self.wait(5)

        def pause(self):
            self.wait(3)

        def short_pause(self):
            self.wait(1.5)

        # Intro
        chapter = Text("Chapter #01").shift(UP)
        theme = Tex("Introdução às Derivadas")
        tGroup = VGroup(chapter,theme)
        
        self.play(
            Write(chapter),
            FadeIn(theme, shift=UP),
            run_time = 3            
        )
        
        self.wait(3)

        self.play(FadeOut(tGroup), run_time = 3)

        # Limite
        lim = MathTex("f'(x)=", "\\lim_{h \\rightarrow 0}", "\\frac{f(x+h)-f(x)}{h}")
        B1 = Brace(lim[1], DOWN)
        t1 = B1.get_text("$h$ tende para 0")
        BG = VGroup(B1,t1)


        self.play(Write(lim), run_time = 3)

        self.play(Write(BG))

        self.wait(3)

        self.play(Uncreate(BG))

        self.wait(10)

        # Taxa média de variação: Função de equação y = x^3
        ax = Axes(x_range = [-2,2, 0.5],
        y_range = [-8,8, 2],
        x_length = 7, 
        y_length = 5.5, 
        x_axis_config = {
            "include_numbers": True,
            "font_size": 24 
        },
        y_axis_config={
            "include_numbers": True,
            "font_size": 24
        },
        tips = False
        ).set_color(GREY).add_coordinates()
        
        title = Title(r"Gráfico da função $f(x) = x^{3}$", include_underline=False, font_size = 40).to_edge(UL)
        function = ax.plot(lambda x : x**3, color = WHITE)
        y_label = ax.get_y_axis_label("y")
        x_label = ax.get_x_axis_label("x")
        graph_settings = VGroup(ax, function, y_label, x_label).to_edge(DL)
        
        self.play(Transform(lim, title), run_time = 3)

        self.play(Create(graph_settings), run_time = 3)

        self.wait(3)

        average_rate_of_change = MathTex(r"f(x)_{t.m.v[a,b]} =", r"\frac {f(b) - f(a)}{b-a}")
        slope = MathTex(r"\frac{\Delta y}{\Delta x}")

        
        
