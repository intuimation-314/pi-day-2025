from manim import *
# Set global background color
config.background_color = "#1E1E1E"  # Dark gray background
class PiThumbnail(Scene):
    def construct(self):

        title = Tex(r"The Quest For $\pi$").set_color_by_gradient(BLUE, TEAL).to_edge(UP).scale(1.8)
        # Load images for each phase and scale them
        phase1 = ImageMobject("Phase_1.png").scale(0.5)
        phase2 = ImageMobject("Phase_2.png").scale(0.5)
        phase4 = ImageMobject("Phase_4.png").scale(0.5)

        # Arrange images in a row with spacing using Group instead of VGroup
        image_group = Group(phase1, phase2, phase4).scale(1.05).arrange(RIGHT, buff=0.5).scale(1.2).shift(1.5*DOWN)

        # Formulas corresponding to each phase
        formula1 = MathTex(r"\pi = \frac{C}{d}").scale(0.75).next_to(phase1, UP)
        formula2 = MathTex(r"\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}").scale(0.7).next_to(phase2, UP).shift(LEFT)
        formula3 = MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103 + 26390n)}{(n!)^4 396^{4n}}").scale(0.65).next_to(phase4, UP).shift(LEFT)

        # Group formulas together for spacing alignment
        formula_group = Group(formula1, formula2, formula3)

        arrow1 = Arrow().next_to(phase1, RIGHT, buff=0.1)
        arrow1.shift(LEFT)
        arrow2 = Arrow().next_to(phase2, RIGHT, buff=0.1)
        arrow2.shift(LEFT)
        # Add everything to the scene
        self.add(title, image_group, formula_group, arrow1, arrow2)
