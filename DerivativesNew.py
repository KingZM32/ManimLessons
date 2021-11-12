from manim import *
 
DEFAULT_SECANT_LENGHT = 2

def get_secant_and_lines(
    cds : CoordinateSystem,
    graph : ParametricFunction, 
    x : float, 
    dx : float,
    length : float = DEFAULT_SECANT_LENGHT,
    xvar : str = None, 
    dxvar : str = None
    ) -> VGroup:
    """
    Description
    ---
    Get secant line and corresponding dots to a `graph`, alongside vertical lines to both ends of the secant

    Parameters
    ---
    `cds`: Coordinate System (Axes § NumberPlane)

    `graph`: Graph of the function 

    `x` : initial value to start the secant

    `dx`: value to end the secant, located at a relative distance to x

    `length`: parameter to measure the length of the secant line. Defaults to `DEFAULT_SECANT_LENGTH`

    `xvar`: label of x to follow along the `x` parameter (defaults to none)

    `dxvar`: label of dx to follow along the `dx` parameter (defaults to none)
    """
    # Defaults § Constants
    DEFAULT_COLOUR = BLUE

    result = VGroup()
    p1 = cds.input_to_graph_point(x, graph)
    p2 = cds.input_to_graph_point(x+dx, graph)

    # Dots to end points
    dot1 = Dot(p1)
    dot2 = Dot(p2)

    # Vertical lines and variable labels (´\alpha´, ´\beta´, etc.)
    vline1 = cds.get_vertical_line(p2)
    vline2 = cds.get_vertical_line(p2)
    xl1 = MathTex(f"{xvar}").next_to(vline1.get_start(), DOWN) if vline1.get_start()[1] == 0 else MathTex(f"{xvar}").next_to(vline1.get_end(), DOWN)
    xl2 = MathTex(f"{dxvar}").next_to(vline2.get_start(), DOWN) if vline2.get_start()[1] == 0 else MathTex(f"{dxvar}").next_to(vline2.get_end(), DOWN)

    # Default slope lenght and secant line to plot
    # TODO: Where's the bridge to get sort out the length of the secant lines?
    

    return result

class Derivatives(Scene):
    def constructor(self):
        # Intro definition, title and text 
        pt1 = Text("CDI I")
        pt2 = Text("Introdução ao estudo das derivadas",
        t2c = {
            "[25:]" : BLUE
        }).next_to(pt1, DOWN, buff = 0.2)

        self.play(
            Create(pt1),
            FadeIn(pt2, shift = UP ),
            run_time = 3
        )

        pt = VGroup(pt1, pt2)
        self.play(FadeOut(pt))
        # Code for 3 seconds pause, video description might take longer
        self.wait(3)

        # Title <--> Intro to derivatives
        tx1 = Title("O que é uma derivada?").to_edge(UP)
        tx2 = Tex(
            "Seja $f$ uma função real. Diz-se que $f'$ é a função derivada de $f$ \n"
            "sse, para cada $x$, $f'(x)$ mede a variação instanântea da função $f$"
            ).to_edge(UL, buff = 0.5)
        
        self.play(Write(tx1,tx2), run_time = 5, rate_func = linear)
        self.wait(3)

        limtxt = Text("Formalmente, temos:").next_to(tx2, DOWN, buff = 0.5)
        lim1 = MathTex("\\lim_{x \\to a}\\frac{f(x)-f(a)}{x-a}")
        lim2 = MathTex("lim_{x \\to h}\\frac{f(x+h)-f(x)}{h}")
        limgr = VGroup(lim1,lim2).arrange(buff = 1.0).next_to(limtxt, DOWN, buff = 0.2)

        box = SurroundingRectangle(lim2, corner_radius=0.2, buff=MED_SMALL_BUFF)

        self.play(
            Write(limtxt),
            Create(limgr)
        )
        self.wait(3)
        self.play(Create(box))
        self.wait(3)
        self.play(FadeOut(VGroup(limtxt,limgr, box)))
        self.wait(3)
        
        # tmv de uma função
        # Exemplo de uma função polinomial
        #TODO: func_def for linhas horizontais e verticais ao gráfico, com dois pontos a e b, à distância 0.5
        title = Title("Gráfico da função $f(x) = x^{3}$").to_edge(UL)

        ax = Axes(x_range = [-2,2, 0.5],
        y_range = [-8,8, 2],
        x_length = 7, 
        y_length = 5.5, 
        tips = False
        ).set_color(GREY).add_coordinates()
        y_label = ax.get_y_axis_label("y").scale(0.5)
        x_label = ax.get_x_axis_label("x").scale(0.5)

        func = ax.plot(
            lambda x : x**3, color = BLUE
        )

        tmv = MathTex("f(x)_{t.m.v[a,b]} =", "\\frac {f(b)-f(a)}{b-a}")
        slope = MathTex("m = \\frac{\\Delta y}{\\Delta x}")

        



