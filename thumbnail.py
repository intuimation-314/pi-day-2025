from manim import *

class PiThumbnail(Scene):
    def construct(self):
        # Load images for each phase and scale them
        phase1 = ImageMobject("phase1.png").scale(0.5)
        phase2 = ImageMobject("phase2.png").scale(0.5)
        phase4 = ImageMobject("phase4.png").scale(0.5)

        # Arrange images in a row with spacing using Group instead of VGroup
        image_group = Group(phase1, phase2, phase4).scale(1.2).arrange(RIGHT, buff=0.9).scale(1.05).shift(1.5*DOWN)

        # Formulas corresponding to each phase
        formula1 = MathTex(r"\pi = \frac{C}{d}").scale(1).next_to(phase1, UP)
        formula2 = MathTex(r"\frac{\pi}{4} = 4\tan^{-1} \frac{1}{5} - \tan^{-1} \frac{1}{239}").scale(0.8).next_to(phase2, UP).shift(LEFT)
        formula3 = MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103 + 26390n)}{(n!)^4 396^{4n}}").scale(0.65).next_to(phase4, UP).shift(LEFT)

        # Group formulas together for spacing alignment
        formula_group = Group(formula1, formula2, formula3)


        # Add everything to the scene
        self.add(image_group, formula_group)
