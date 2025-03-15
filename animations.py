from manim import *
import math
import numpy as np
# Set global background color
config.background_color = "#1E1E1E"  # Dark gray background

class PiIntroScene(Scene):
    def construct(self):
        ### PHASE 1: Show Pi and Digits in Circular Pattern ###
        
        # Create the central π symbol
        pi_symbol = MathTex(r"\pi").scale(2).set_color(BLUE)
        # Display the introduction text
        pi_intro_text = Tex(
                "The most fundamental mathematical constants,", 
                "we encounter early in our life."
             ).arrange(DOWN)
        pi_intro_text.to_edge(UL)
        
        # Animation: π grows larger
        self.play(Write(pi_symbol),
                  Write(pi_intro_text))
        self.play(pi_symbol.animate.scale(3), run_time=2)
        self.wait(1)

        # Define the first few digits of π
        pi_digits = "3.1415926535897932384626433832795028841971"

        # Create a circular arrangement of digits
        radius = 2  # Radius for circular placement
        digit_objects = VGroup()
        num_digits = len(pi_digits)  # Get number of digits
        
        for i in range(num_digits):  
            digit_tex = MathTex(pi_digits[i]).scale(0.65).set_color(WHITE)
            angle = i * (2 * np.pi / num_digits)  
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            digit_tex.move_to([x, y, 0])  # Place digits around the circle
            digit_objects.add(digit_tex)

        # Animate the digits appearing in a circular motion
        self.play(LaggedStartMap(FadeIn, digit_objects, lag_ratio=0.1), run_time=3)
        self.wait(1)

        ### PHASE 2: Transform Digits into Circle Shape ###
        
        # Transition the digits into forming a circle
        circle = Circle(radius=2, color=BLUE)
        self.play(Transform(digit_objects, circle), run_time=2)
        self.wait(1)

        # Fade out the π symbol
        self.play(FadeOut(pi_symbol), FadeOut(pi_intro_text))
        self.wait(1)

        ### PHASE 3: Show Circle and Diameter ###
        
        # Define diameter
        diameter = Line(circle.get_left(), circle.get_right(), color=YELLOW)

        # Define bottom line (equal to circumference)
        circumference_length = 2 * PI * circle.radius
        bottom_line = Line(circle.get_left(), circle.get_left() + RIGHT * circumference_length, color=BLUE)
        bottom_line.move_to(DOWN * 2.5)  # Move below the circle

        # Create labels
        pi_text = MathTex(r"\pi = \frac{C}{d} \approx 3.14").to_edge(LEFT)
        d_text = MathTex(r"d").next_to(diameter, DOWN)
        c_text = MathTex(r"C").next_to(circle, RIGHT)
        unfolded_text = MathTex(r"\text{Unfolding the circumference}").to_edge(UP)

        # Show the circle and diameter
        self.play(Create(circle), Create(diameter))
        self.play(Write(pi_text), Write(d_text))
        self.play(Write(c_text))

        ### PHASE 4: Unfold the Circle's Circumference ###
        
        # Transform the perimeter into a straight line
        self.play(Transform(circle.copy(), bottom_line), Write(unfolded_text), run_time=3)

        # Show three diameters fitting in
        for i in range(3):
            segment = Line(bottom_line.get_start() + i * diameter.get_length() * RIGHT,
                           bottom_line.get_start() + (i + 1) * diameter.get_length() * RIGHT,
                           color=YELLOW)
            brace = Brace(segment, DOWN, buff=0.5, color=RED)
            tex = MathTex(r"d").next_to(brace, DOWN)
            self.play(Create(segment), FadeIn(brace), Create(tex))

        # Show the tiny leftover part (~0.14 of the diameter)
        leftover = Line(segment.get_end(), bottom_line.get_end(), color=BLUE)
        leftover_brace = Brace(leftover, DOWN, color=RED)
        leftover_text = MathTex(r"\approx 0.14 d").next_to(leftover, UP)

        self.play(Create(leftover), Write(leftover_text), Create(leftover_brace))
        self.wait(2)

class PiInNature(Scene):
    def construct(self):
        tex = Tex("\"Found Everywhere in Nature\"").to_edge(UP)
        self.add(tex)
        self.wait(2)

class EngineerScene(Scene):
    def construct(self):
        # Load engineer and mathematician images (keeping your original positions)
        engineer = ImageMobject("engineer.png").to_edge(LEFT).scale(0.8) # Engineer at Upper Left
        
        # Titles above the images
        engineer_title = Tex("Engineers", color=BLUE).scale(2).to_edge(UP)
        
        # Create text labels for their respective pi usage
        engineer_pi_approx = MathTex(r"\pi \approx 3.14 \text{ or } \pi \approx 3", color=WHITE)
        engineer_pi_approx2 = Tex("\"To the naked eye, it would still look perfect\"").next_to(engineer_pi_approx, DOWN, buff=1).shift(DOWN)
        engineer_pi_approx.next_to(engineer, RIGHT, buff=1)  # Positioned to the right of the engineer

        # Add everything to the scene
        # self.add(engineer, engineer_title, engineer_pi_approx, engineer_pi_approx2)
        self.play(FadeIn(engineer),
                  Write(engineer_title),
                  FadeIn(engineer_pi_approx),
                  Write(engineer_pi_approx2))

class MathScene(Scene):
    def construct(self):
        # Load engineer and mathematician images (keeping your original positions)
        mathematician = ImageMobject("mathematician.png").to_edge(DR).shift(RIGHT)  # Mathematician at Down Right
        mathematician_title = Tex("\"Mathematicians\"").scale(1.8).to_edge(UP)
      
        math_pi_precise = VGroup(
            Tex(r"3.1415926535 8979323846 2643383279"),
            Tex(r"5028841971 6939937510 5820974944"),
            Tex(r"5923078164 0628620899 8628034825"),
            Tex(r"3421170679\ldots")
        ).scale(0.8)
        math_pi_precise.arrange(DOWN).move_to(2 * LEFT + DOWN) # Positioned to the left of the mathematician
        infinite = Tex("Infinite Precision", color = BLUE).next_to(math_pi_precise, UP, buff=0.5)
        
        # Add everything to the scene
        # self.add(engineer, engineer_title, engineer_pi_approx, engineer_pi_approx2)
        self.play(FadeIn(mathematician),
                  FadeIn(mathematician_title),
                  Write(infinite),
                  Write(math_pi_precise),
                )

class ThinkingMuBot(Scene):
    def construct(self):
        # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.2)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.2)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
        bot_happy = VGroup(bot_body.copy(), happy_mouth).to_edge(DL)
        bot_sad = VGroup(bot_body.copy(), sad_mouth).to_edge(DL)
        
        # Blinking effect using fade-in and fade-out
        def blink():
            return AnimationGroup(
                FadeOut(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                FadeIn(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                lag_ratio=0.2,
            )
        
                # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).next_to(bot_thinking, UR, buff=0.1)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7.5, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)
        mu_thinking = VGroup(dot1,dot2,dot3, thinking_cloud).next_to(bot_thinking, UR)
        mu_thinking.shift(RIGHT)

        tex1 = Tex("That's not how we compute PI").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Physical measurements always", "lead to an error!")
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play( FadeIn(mu_thinking))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait(2)


class PiUncanny(Scene):
    def construct(self):
        # Load 4 uncanny images (assuming file names are "phase1.png", "phase2.png", etc.)
        images = [
            ImageMobject("Phase_1.png").scale(0.8),
            ImageMobject("Phase_2.png").scale(0.8),
            ImageMobject("Phase_3.png").scale(0.95).move_to(DOWN),
            ImageMobject("Phase_4.png").scale(0.8),
        ]

        # Define Pi formulas for each phase
        formulas = [
            MathTex(r"\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}").scale(0.8),
            MathTex(r"\pi = 4 \int_{0}^{1} \sqrt{1 - x^2} dx").scale(0.8),
            MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103 + 26390n)}{(n!)^4 396^{4n}}").scale(0.8),
            MathTex(r"\frac{1}{\pi} = 12 \sum_{n=0}^{\infty} \frac{(-1)^n (6n)! (13591409 + 545140134n)}{(3n)! (n!)^3 640320^{3n + 3/2}}").scale(0.8),
        ]

        # Positioning: Center the images and formulas
        for img, formula in zip(images, formulas):
            img.move_to(DOWN)  # Place image at center
            formula.next_to(img, UP, buff=0.3)  # Formula appears above the image

            # Show image & formula, then wait
            self.play(FadeIn(img), Write(formula))
            self.wait(2)

            # Fade out before moving to the next one
            self.play(FadeOut(img), FadeOut(formula))

        # Keep scene visible at the end
        self.wait(3)


class PiComputation(Scene):
    def construct(self):
        # Step 1: Show the Chudnovsky Algorithm Formula
        title = Tex("The Chunovsky Formula", color=BLUE).move_to(UP)
        chudnovsky_formula = MathTex(
            r"\frac{1}{\pi} = 12 \sum_{n=0}^{\infty} \frac{(-1)^n (6n)! (13591409 + 545140134n)}"
            r"{(3n)! (n!)^3 640320^{3n + 3/2}}"
        ).scale(0.8)

        self.play(Write(title),Write(chudnovsky_formula))
        self.wait(2)
        self.play(FadeOut(chudnovsky_formula), FadeOut(title))
        
        image1 = ImageMobject("google.png").scale(1.6).move_to(2*UP)
       
        pi_digits_text = Tex("- 100 Trillion Digits")
        days_text = Tex("- 157 days of computation!")
        storage_text = Tex("- 82k TB storage")
        electricity_text = Tex("- 200,000 dollars!")
        text = VGroup(pi_digits_text, days_text,
                      storage_text, 
                      electricity_text).arrange(DOWN, buff = 0.3, aligned_edge = LEFT)
        text.next_to(image1, DOWN)
        text.shift(RIGHT)
        self.play(FadeIn(image1))
        self.wait()
        self.play(FadeIn(text[0]))

        # Step 3: Display π digits below the "100 Trillion Digits" text
        pi_digits = VGroup(
            Tex(r"3.1415926535 8979323846 2643383279 5028841971 6939937510"),
            Tex(r"5820974944 5923078164 0628620899 8628034825 3421170679"),
            Tex(r"8214808651 3282306647 0938446095 5058223172 5359408128"),
            Tex(r"4811174502 8410270193 8521105559 6446229489 5493038196"),
            Tex(r"2874406566 9234603486 1045432664 8213393607 2602491412"),
            Tex(r"7372458700 6606315588 1748815209 2096282925 4091715364\ldots")
        ).scale(0.65)
        pi_digits.arrange(DOWN, buff = 0.5, aligned_edge=LEFT)
        pi_digits.next_to(pi_digits_text, DOWN, buff=0.5)

        # Animate the display of π digits
        self.play(Write(pi_digits), run_time=5)
        self.wait(3)
        self.play(FadeOut(pi_digits))

        self.play(FadeIn(text[1:]))
        self.wait(2)

class ThinkingMuBot2(Scene):
    def construct(self):
        # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.2)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.2)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
        bot_happy = VGroup(bot_body.copy(), happy_mouth).to_edge(DL)
        bot_sad = VGroup(bot_body.copy(), sad_mouth).to_edge(DL)
        
        # Blinking effect using fade-in and fade-out
        def blink():
            return AnimationGroup(
                FadeOut(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                FadeIn(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                lag_ratio=0.2,
            )
        
                # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).next_to(bot_thinking, UR, buff=0.1)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7.5, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)
        mu_thinking = VGroup(dot1,dot2,dot3, thinking_cloud).next_to(bot_thinking, UR)
        mu_thinking.shift(RIGHT)

        tex1 = Tex("Why ??").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Why PI get so ridiculously", "complicated?")
        tex0 = Tex("Precision").scale(0.8).move_to(thinking_cloud.get_center())
        tex3 = Tex("Why more and more digits?").scale(0.8).move_to(thinking_cloud.get_center())
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(mu_thinking))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait()
        self.play(Transform(tex1, tex0))
        self.wait()
        self.play(Transform(tex1,tex3))
        self.wait(2)

class PiTimelines(Scene):
    def construct(self):
        # Create a vertical timeline on the left (from (-6, 3, 0) to (-6, -3, 0))
        timeline = Line(np.array([-6, 3, 0]), np.array([-6, -3, 0]), color=WHITE)
        self.play(Create(timeline))
        
        # Create two dots to divide the timeline into 3 equal parts (at y=1 and y=-1)
        dot_top = Dot(np.array([-6, 1, 0]), color=BLUE)
        dot_bottom = Dot(np.array([-6, -1, 0]), color=BLUE)
        self.play(Create(dot_top), Create(dot_bottom))
        
        # Create three segments as separate Line objects
        top_segment = Line(np.array([-6, 3, 0]), np.array([-6, 1, 0]), color=WHITE)
        middle_segment = Line(np.array([-6, 1, 0]), np.array([-6, -1, 0]), color=WHITE)
        bottom_segment = Line(np.array([-6, -1, 0]), np.array([-6, -3, 0]), color=WHITE)
        self.play(Create(top_segment), Create(middle_segment), Create(bottom_segment))
        
        # Create labels for each era and position them to the right of each segment
        label_texts = [
            "The Geometric Era (250 BCE – 1630 CE)",
            "The Infinite Series Era (1600s – 1980s)",
            "The Modern Algorithm Era (1980 – Present)"
        ]
        segments = [top_segment, middle_segment, bottom_segment]
        labels = VGroup(*[
            Tex(text, font_size=24, color=WHITE).next_to(seg, RIGHT, buff=0.5)
            for text, seg in zip(label_texts, segments)
        ])
        self.play(Write(labels))
        self.wait(1)
        
        # Helper function to highlight one label while fading out others,
        # then restore the label to its original state and fade in the others.
        def highlight_label(index):
            current_label = labels[index]
            # Save its original state for later restoration
            original = current_label.copy()
            others = VGroup(*[labels[i] for i in range(3) if i != index],
                            timeline, dot_top, dot_bottom)
            self.play(
                current_label.animate.scale(2).move_to(ORIGIN),
                FadeOut(others),
                run_time=1.5
            )
            self.wait(2)
            self.play(
                Transform(current_label, original),
                FadeIn(others),
                run_time=1
            )
            self.wait(1)
        
        # Highlight each era sequentially
        highlight_label(0)
        highlight_label(1)
        highlight_label(2)


class Archimedes(Scene):
    def construct(self):
       image = ImageMobject("archimedes.png").scale(0.8).shift(2.5 * LEFT)
       title = Tex("Archimedes\n(250 BCE)").next_to(image, RIGHT, buff=1)
       self.play(FadeIn(image), Write(title))
   
class ArchimedesPi(Scene):
    def construct(self):
        # Create the full progression label "6 -> 12 -> 24 -> 48 -> 96"
        progression = MathTex("6", "\\rightarrow", "12", "\\rightarrow", "24", "\\rightarrow", "48", "\\rightarrow", "96", color=WHITE)
        progression.to_edge(UP)
        
        # Initially, only show "6" (the first token)
        initial_prog = VGroup(*progression[:1])
        self.play(Write(initial_prog))
        
        # Draw the circle (radius 2)
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        
        # Define the sequence of side counts
        sides_list = [6, 12, 24, 48, 96]
        
        # Create initial inscribed and circumscribed polygons for n = 6
        n = sides_list[0]
        inscribed = RegularPolygon(n, radius=2, color=WHITE)
        circumscribed = RegularPolygon(n, radius=2 / math.cos(math.pi / n), color=WHITE)
        self.play(Create(inscribed), Create(circumscribed))
        
        # Store previous polygons for transformation
        prev_inscribed = inscribed
        prev_circumscribed = circumscribed
        
        # Loop over the remaining side counts (for side counts: 12, 24, 48, 96)
        for i, n in enumerate(sides_list[1:]):  # i=0 -> 12, i=1 -> 24, i=2 -> 48, i=3 -> 96
            # Create new polygons for current n
            new_inscribed = RegularPolygon(n, radius=2, color=WHITE)
            new_circumscribed = RegularPolygon(n, radius=2 / math.cos(math.pi / n), color=WHITE)
            
            # Determine which tokens to reveal:
            # For i = 0, reveal tokens at indices 1 and 2 ("\\rightarrow" and "12")
            # For i = 1, reveal tokens at indices 3 and 4 ("\\rightarrow" and "24"), etc.
            tokens_to_write = VGroup(*progression[2*i+1:2*i+3])
            
            # Transform the previous polygons into the new ones and reveal the new progression tokens
            self.play(
                ReplacementTransform(prev_inscribed, new_inscribed),
                ReplacementTransform(prev_circumscribed, new_circumscribed),
                Write(tokens_to_write),
                run_time=1.5
            )
            
            # Update for the next iteration
            prev_inscribed = new_inscribed
            prev_circumscribed = new_circumscribed
        
        # After the loop, zoom in by scaling the circle and polygons by a factor of 2.
        group = VGroup(circle, prev_inscribed, prev_circumscribed)
        self.play(ApplyMethod(group.scale, 2.5), run_time=1)

        # Finally, display Archimedes' bounds for π at the bottom of the scene
        bounds = MathTex(r"\frac{223}{71} < \pi < \frac{22}{7}", color=WHITE).to_edge(DOWN)
        numeric_bounds = MathTex(r"3.1408 < \pi < 3.1429")
        self.play(Write(bounds),
                  Write(numeric_bounds))
        self.wait(2)

        self.play(FadeOut(progression),
        FadeOut(bounds),
        FadeOut(numeric_bounds))
        self.wait()


        tex = Tex(r"By 1630, this method could determine $\pi$ to $\textbf{39 decimal places}$").to_edge(UP)         
        pi_text = MathTex(
            r"\pi = 3.1415926535"
            r"8979323846"
            r"2643383279"
            r"5028841971"
        ) # Adjust scale if needed
        
        tex1 = Tex("Millions of sides!").to_edge(DOWN)
        # Surround it with a rectangle for emphasis
        rect = SurroundingRectangle(pi_text, color=YELLOW)
         
        self.play(Write(tex))
        # Display text and rectangle
        self.play(Write(pi_text), Create(rect))
        self.play(Write(tex1))
        self.wait(2)


class Era2(Scene):
    def construct(self):
        image = ImageMobject("calc2.png")
        image2 = ImageMobject("calculus.png").scale(0.5)
        self.add(image,image2)

class NewtonQuarterCircle(Scene):
    def construct(self):

        image = ImageMobject("newton.png").scale(0.6).to_edge(RIGHT)
        age = Tex("Newton(1630s)").scale(0.65).next_to(image, DOWN)
        self.play(FadeIn(image), 
                  Write(age))
        self.wait()
        # Create coordinate axes centered at the origin
        axes = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            x_length=3,
            y_length=3,
            axis_config={"color": WHITE},
            tips=False
        )
        
        # Draw the full unit circle (radius=1, centered at origin)
        circle = Circle(radius=1, color=WHITE)

        # Create the quarter circle (sector in the first quadrant: from 0 to PI/2)
        quarter = Sector(
            outer_radius=1,
            angle=PI/2,
            start_angle=0,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_width=0  # optional: removes the boundary stroke
        )
        group = VGroup(circle, axes, quarter).scale(1.5).move_to(2*LEFT + UP).scale(0.6)
        
        # Display the integral equation below the axes
        integral_eq = MathTex(r"\int_0^1 \sqrt{1-x^2}\,dx = \frac{\pi}{4}", color=WHITE).scale(0.6).next_to(group, DOWN)
        tex = Tex("Binomial Expansion", color = BLUE).scale(0.8).next_to(integral_eq, DOWN)
        tex2 = Tex("Area of Quarter Circle").scale(0.8).next_to(group,UP)
        # Transition to display the binomial expansion for sqrt(1-x^2)
        expansion = MathTex(r"\sqrt{1-x^2} = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \cdots", color=WHITE).scale(0.6).next_to(tex, DOWN)

        # self.add(group, integral_eq,tex,expansion, tex2)
        self.play(Write(tex2),
                  Create(group),
                  Write(integral_eq))
        self.wait()
        self.play(
                  Write(tex),
                  Write(expansion))
        self.wait()

class MachinsFormula(Scene):
    def construct(self):
        image = ImageMobject("machin.png").scale(2).to_edge(RIGHT)
        name = Tex("John Machin(1706)").next_to(image, DOWN).scale(0.8)
        tex = Tex("In 1706, John Machin introduced Machin's Formula").arrange(DOWN).move_to(UP*3)
        formula_title = Tex("Machin's Formula", color=BLUE).move_to(2* LEFT+UP)
        formula = MathTex(r"\frac{\pi}{4} = 4\tan^{-1} \frac{1}{5} - \tan^{-1} \frac{1}{239}").next_to(formula_title, DOWN)
        # self.add(image, name, tex, formula_title, formula)
        self.play(FadeIn(image),
                  Write(name),
                  Write(tex))
        self.wait()
        self.play(Write(formula_title),
                  Write(formula))
        self.wait(2)
        pi_digits = MathTex(
            r"\pi = 3.1415926535\, 8979323846\, 2643383279\, 5028841971\, 6939937510,",
            r"5820974944\, 5923078164\, 0628620899\, 8628034825\, 3421170679"
        ).scale(0.6)
        
        # Arrange the digits in two lines
        pi_digits.arrange(DOWN, center=True).to_edge(DL)
        title = Tex("100 Digits of \\(\\pi\\)!", color = BLUE).next_to(pi_digits, UP)
        
        # Create a rectangle around the π digits
        rect = SurroundingRectangle(pi_digits, color=YELLOW)
        
        # Show the title, digits, and rectangle
        self.play(Write(title))
        self.play(Write(pi_digits), run_time=3)
        self.play(Create(rect))  # Draw the rectangle around digits

        self.wait(3)

class ArctanSeries(Scene):
    def construct(self):
        # Step 1: Show the formula
        title = MathTex(r"\textbf{Series of } \arctan(x)").to_edge(UP)
        formula = MathTex(r"\arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \dots").scale(0.8)
        formula.to_edge(DOWN)
        
        # Step 2: Create the coordinate system
        axes = Axes(
            x_range=[-1.2, 1.2, 0.2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": WHITE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Step 3: Plot the actual arctan function
        arctan_graph = axes.plot(lambda x: np.arctan(x), color=BLUE, x_range=[-1, 1])
        arctan_label = MathTex(r"y = \arctan(x)").scale(0.7).next_to(arctan_graph, UP, buff=0.3)

        # Step 4: Show partial sums of the Maclaurin series
        terms = [
            lambda x: x,
            lambda x: x - x**3 / 3,
            lambda x: x - x**3 / 3 + x**5 / 5,
            lambda x: x - x**3 / 3 + x**5 / 5 - x**7 / 7
        ]
        colors = [YELLOW, GREEN, ORANGE, RED]
        graphs = VGroup()

        for i, term in enumerate(terms):
            approx_graph = axes.plot(term, color=colors[i], x_range=[-1, 1])
            graphs += approx_graph
            term_label = MathTex(rf"y = \sum_{{n=0}}^{{{2*i+1}}} \frac{{(-1)^n x^{{2n+1}}}}{{2n+1}}").scale(0.6).next_to(approx_graph, DOWN, buff=0.3)
        
        self.add(title, formula, axes, arctan_graph, graphs)

class Ramanujan(Scene):
    def construct(self):
       image = ImageMobject("ramanujan.png").scale(0.6).to_edge(RIGHT)
       tex = Tex("The Ramanujan's miraculous formula",color=BLUE).to_edge(UP)
       formula = MathTex(r"\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103 + 26390n)}{(n!)^4 396^{4n}}").scale(0.8).move_to(LEFT*1.5)
       tex2 = Tex("Each term adds 8 decimal places!",
                  "Older formula's(Machin) requires about 20 terms to aachieve the same",
                  color=BLUE)
       tex2.arrange(DOWN, aligned_edge=LEFT).scale(0.6).next_to(formula, DOWN, buff=1)
    #    self.add(image, tex, formula, tex2)

       self.play(FadeIn(image),
                 Write(tex),
                 FadeIn(formula))
       self.wait()
       self.play(Write(tex2))
       self.wait()

class Chudnovsky(Scene):
    def construct(self):
       image = ImageMobject("chudnovsky.png").scale(0.25).to_edge(LEFT).shift(0.5*RIGHT)
       
       tex = Tex("David and Gregory Chudnovsky",color=WHITE).scale(0.5).next_to(image, DOWN)
       formula = MathTex(r"\frac{1}{\pi} = 12 \sum_{n=0}^{\infty} \frac{(-1)^n (6n)! (13591409 + 545140134n)}{(3n)! (n!)^3 640320^{3n + 3/2}}").scale(0.7).next_to(image, RIGHT, buff=0.5)
       tex2 = Tex("Each term adds 15 decimal places!",
                  color=BLUE)
       tex2.scale(0.6).next_to(formula, DOWN, buff=1)
       tex3 = Tex("In 1989, Chudnovsky brothers modifed the series even further !", color=BLUE).scale(0.8).to_edge(UP)
       self.add(image, tex, formula, tex2)

       self.play(Write(tex3),
                 FadeIn(image),
                 Write(tex),
                 FadeIn(formula))
       self.wait()
       self.play(Write(tex2))
       self.wait()

class PiBreakthroughs(Scene):
    def construct(self):
        # Introduction Text
        intro_text = MathTex(
            r"\text{The modern era began around 1980 when mathematicians}", r"\text{utilized three major breakthroughs:}"
        ).scale(0.8).arrange(DOWN).to_edge(UP)

        self.play(Write(intro_text))
        self.wait(1)

        # First Breakthrough: FFT
        fft_text = MathTex(
            r"\textbf{1. FFT Mul Algorithm }"
        ).scale(0.5)

        # Second Breakthrough: High-performance algorithms
        algo_text = MathTex(
            r"\textbf{2. High-Performance Algorithms }"
        ).scale(0.5)

        # Third Breakthrough: Supercomputers
        supercomputer_text = MathTex(
            r"\textbf{3. Supercomputer Advancement }"
        ).scale(0.5)

        # Group the text and arrange it
        group = VGroup(fft_text, algo_text, supercomputer_text).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP)

        # Position the group below the introduction text
        group.next_to(intro_text, DOWN, buff=0.8)

        image1 = ImageMobject("fft.png").scale(0.75).to_edge(DOWN).shift(LEFT*2 + UP)
        image2 = ImageMobject("fft2.jpg").scale(1.2).next_to(image1, RIGHT, buff=1.5)

        #supercomputerimage
        image3 = ImageMobject("super1.png").scale(0.3)
        image4 = ImageMobject("super2.jpg").scale(0.1)
        image5 = ImageMobject("super3.jpg").scale(0.2)

        group2 = Group(image3, image4, image5).arrange(RIGHT, buff=0.5).to_edge(DOWN).shift(0.5*UP) 
        group2.scale(1.2)

        for tex in group:
         # Fade in the group properly
         self.play(FadeIn(tex))
         self.play(tex.animate.set_color(BLUE).scale(1.2))
         if(tex == fft_text):
             self.play(FadeIn(image1),
                       FadeIn(image2))
             self.wait(2)
             self.play(FadeOut(image1),
                   FadeOut(image2))
         self.wait(2)
        self.play(FadeIn(group2))
        self.wait(2)


class Blank(Scene):
    def construct(self):
        self.wait(2)

class FuturOfPI(Scene):
    def construct(self):
        title = Tex("The Future of ",  r"$\pi$", " computation").scale(1.2).shift(3*UP)
        self.play(Write(title))

                # Bot's body: μ symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil (glints)
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        
        # Group the eyes together for easier manipulation
        eyes = VGroup(
            left_eye_white, right_eye_white, 
            left_eye_pupil, right_eye_pupil,
            left_eye_glint, right_eye_glint
        )
        
        # Assemble the bot from the μ symbol and the eyes.
        # Scale the entire bot up by 1.5.
        bot_body = VGroup(mu, eyes).scale(1.2)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.2)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
        bot_happy = VGroup(bot_body.copy(), happy_mouth).to_edge(DL)
        bot_sad = VGroup(bot_body.copy(), sad_mouth).to_edge(DL)
        
                # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).next_to(bot_thinking, UR, buff=0.1)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7.5, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)
        mu_thinking = VGroup(dot1,dot2,dot3, thinking_cloud).next_to(bot_thinking, UR).shift(0.5*DOWN)

        tex1 = Tex("How far can we go ?").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Researchers have shifted focus", "to a new challange!")
        tex3 = Tex("Computing individual digits").scale(0.8).move_to(thinking_cloud.get_center())
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(mu_thinking))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait(2)

        self.play(
                  Transform(tex1, tex3))
        self.wait()
        self.play(FadeOut(tex1),
                  FadeOut(title))
        #why pi part?
        text1 = Tex("We don't actually need trillion digits!").scale(0.8).move_to(thinking_cloud.get_center())
        text2 = Tex("10 decimal digits are enough for", "scientific and engineering pusposes")
        text2.arrange(DOWN)
        text2.scale(0.8).move_to(thinking_cloud.get_center())

        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1, text2))
        self.wait()
        
        
class BBPAlg(Scene):
    def construct(self):
        title = Tex("The BBP Algorithm").scale(1.2).move_to(3*UP)
        
        bbp_formula = MathTex(
                r"\pi = \sum_{k=0}^{\infty} \frac{1}{16^k} \left("
                r"\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}"
                r"\right)"
            ).scale(0.6).next_to(title, DOWN, buff=0.5)
        
        image1 = ImageMobject("bbp.jpg").scale(0.55).move_to(1.5*DOWN + 2.5*LEFT)
        title1 = Tex("Simon Plouffe").scale(0.6).next_to(image1, DOWN)
        image2 = ImageMobject("bbp2.jpg").scale(0.3).next_to(image1, RIGHT, buff=2)
        title2 = Tex(" David H. Bailey").scale(0.6).next_to(image2, DOWN)

        # self.add(title, image1, image2, bbp_formula, title1, title2)

        self.play(Write(title),
                  Write(bbp_formula))
        self.wait()
        self.play(FadeIn(image1),
                  Write(title1),
                  FadeIn(image2),
                  Write(title2)
                  )
        self.wait(2)


class TimelinePiEvolution(Scene):
    def construct(self):
        # Create a number line from 250 BCE (-250) to 2025
        timeline = NumberLine(
            x_range=[-250, 2025, 250],  # Marks every 250 years
            length=12,  # Length of number line
            include_numbers=True,
            color=WHITE
        )
        timeline.shift(DOWN * 1.5)

        # Title
        title = Tex("Time Progression: 250 BCE to Present").scale(1).to_edge(UP)

        # Add timeline and title
        self.play(Write(title))
        self.play(Create(timeline))
        self.wait(1)

        # Moving indicator for time
        dot = Dot(color=RED).move_to(timeline.n2p(-250))
        year_label = Integer(-250).next_to(dot, UP)

        self.play(FadeIn(dot, year_label))
        self.wait(1)

        # Pi digits at different historical points
        pi_values = [
            "3",                           # 250 BCE - Archimedes
            "3.14",                        # 1500s - Early modern approximations
            "3.14159",                     # 1700s - Newton's work
            "3.1415926535",                # 1800s - More precision
            "3.141592653589793",           # 1900s - Calculus-based improvements
            "3.14159265358979323846",      # 1950s - Early computers
            "3.1415926535897932384626433", # 2000s - Supercomputers
            "3.1415926535897932384626433832795028841971"  # 2020s - Trillions of digits
        ]

        # Label to show pi digits
        pi_label = MathTex(r"\pi = " + pi_values[0] + r"\ldots").scale(0.8).to_edge(LEFT)
        self.play(Write(pi_label))

        # Years corresponding to the above π values
        years = [-250, 1500, 1700, 1800, 1900, 1950, 2000, 2025]

        # Animate the timeline progression and π digits increasing
        for i in range(1, len(years)):
            self.play(
                dot.animate.move_to(timeline.n2p(years[i])),
                ChangeDecimalToValue(year_label, years[i]),
                Transform(pi_label, MathTex(r"\pi = " + pi_values[i] + r"\ldots").scale(0.8).to_edge(LEFT)),
                rate_func=smooth,
                run_time=2
            )
            self.wait(1)

        self.wait(2)

class WhyComputePi(Scene):
    def construct(self):
        # Title at the top
        title = MathTex(r"\text{Why Do We Compute } \pi \text{ to Trillions of Digits?}").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # First Reason: Testing Computers & Algorithms
        testing_text = MathTex(
            r"\textbf{1. Testing Computers and Algorithms}"
        ).scale(0.6)

        # Second Reason: The Unsolved Mysteries of π
        mystery_text = MathTex(
            r"\textbf{2. The Unsolved Mysteries of } \pi"
        ).scale(0.6)

        # Third Reason: The Competitive & Cultural Appeal
        competition_text = MathTex(
            r"\textbf{3. The Competitive and Cultural Appeal}"
        ).scale(0.6)

        # Arrange all text in a vertical list
        group = VGroup(testing_text, mystery_text, competition_text).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 0.5)

        # Position below the title
        group.next_to(title, DOWN, buff=0.8)

        for tex in group:
            self.play(FadeIn(tex))
            self.play(tex.animate.set_color(BLUE).scale(1.2))
        self.wait(2)

class PiFinale(Scene):
    def construct(self):
        # Glowing Pi Symbol
        pi_symbol = MathTex(r"\pi").scale(4).set_color(YELLOW)
        self.play(Write(pi_symbol))
        self.wait(1)

        # Expanding Digits of Pi
        pi_digits = MathTex(
            "3.1415926535 8979323846 2643383279 5028841971 6939937510",
            "5820974944 5923078164 0628620899 8628034825 3421170679...",
        ).scale(0.7)
        pi_digits.move_to(DOWN * 1.5)

        self.play(Write(pi_digits), run_time=2)
        self.wait(1)

        # Timeline & Historical Figures
        timeline = NumberLine(
            x_range=[-2000, 2025, 500], length=10,
            include_numbers=True, include_ticks=True
        ).move_to(UP * 2)

        self.play(Create(timeline))
        self.wait(1)

        # Historical Mathematicians (Faint Appearances)
        archimedes = Tex("Archimedes").scale(0.6).set_opacity(0.5).move_to(LEFT * 3 + UP * 1.5)
        ramanujan = Tex("Ramanujan").scale(0.6).set_opacity(0.5).move_to(RIGHT * 3 + UP * 1.5)
        chudnovsky = Tex("Chudnovsky").scale(0.6).set_opacity(0.5).move_to(UP * 3)

        self.play(FadeIn(archimedes, ramanujan, chudnovsky), run_time=2)
        self.wait(1)

        # Transform to Happy Pi Day Message
        happy_pi = Tex("Happy ", r"$\pi$", " Day!").scale(1.5).set_color(ORANGE).move_to(DOWN * 2)
        self.play(Transform(pi_symbol, happy_pi))
        self.wait(1)

        # Closing Message
        closing_message = Tex(
            "Thank you for watching!", 
            "Check out sources in the description."
        ).arrange(DOWN).scale(0.8).move_to(DOWN * 3)

        self.play(Write(closing_message))
        self.wait(2)

        # Fade Out
        self.play(FadeOut(pi_symbol, pi_digits, timeline, archimedes, ramanujan, chudnovsky, happy_pi, closing_message))

class PiSpiralScene(Scene):
    def construct(self):
        # Create the central π symbol
        pi_symbol = MathTex(r"\pi").scale(2).set_color(BLUE)
        self.play(Write(pi_symbol),
                  pi_symbol.animate.scale(3))
        self.wait(1)
        
        # Transform to Happy Pi Day Message
        happy_pi = Tex("Happy ", r"$\pi$", " Day!").scale(1.5).set_color(ORANGE).move_to(2*DOWN)

        # Define the first few digits of π
        pi_digits = "3.14159265358979323846264338327950288419716939937510"
        
        # Spiral Parameters
        num_digits = len(pi_digits)  # Number of digits to animate
        spiral_radius = 0.3  # Distance between digits in the spiral
        spiral_expansion = 0.3  # Factor to increase spacing as it spirals out
        angle_shift = 0.3  # Angle shift per digit to form a spiral
        
        digit_objects = VGroup()
        
        for i in range(num_digits):
            digit_tex = MathTex(pi_digits[i]).scale(0.6).set_color(WHITE)
            
            # Define Spiral Position
            angle = i * angle_shift
            radius = spiral_radius + i * spiral_expansion
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            digit_tex.move_to([x, y, 0])  # Place digits along spiral
            digit_objects.add(digit_tex)

        # Animate the digits appearing in a spiral motion
        self.play(LaggedStartMap(FadeIn, digit_objects, lag_ratio=0.05), run_time=3)
        self.wait(1)
        self.play(FadeIn(happy_pi))
        self.wait(1)
        

class MuBotEndScene(Scene):
        def construct(self):
            # Bot's body: μ symbol as the body of the bot
            mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
            
            # Eyes: white ovals for the eyes
            left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
            right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
            left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
            right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
            
            # Add small circle in the middle of each pupil (glints)
            left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
            right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
            
            # Group the eyes together for easier manipulation
            eyes = VGroup(
                left_eye_white, right_eye_white, 
                left_eye_pupil, right_eye_pupil,
                left_eye_glint, right_eye_glint
            )
            
            # Assemble the bot from the μ symbol and the eyes.
            # Scale the entire bot up by 1.5.
            bot_body = VGroup(mu, eyes).scale(1.2)
            
            # Mouth expressions (arc for different moods)
            happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
            sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.2)
            thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.2)
            
            # Assemble complete bot expressions using the scaled bot body
            bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
            bot_happy = VGroup(bot_body.copy(), happy_mouth).to_edge(DL)
            bot_sad = VGroup(bot_body.copy(), sad_mouth).to_edge(DL)
            
            # Blinking effect using fade-in and fade-out
            def blink():
                return AnimationGroup(
                    FadeOut(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                    FadeIn(VGroup(left_eye_pupil, right_eye_pupil, left_eye_glint, right_eye_glint)),
                    lag_ratio=0.2,
                )
            
                    # Thought bubbles (dots leading to cloud)
            dot1 = Dot(radius=0.08, color=WHITE).next_to(bot_thinking, UR, buff=0.1)
            dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
            dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

            # Thinking cloud (Rounded Rectangle)
            thinking_cloud = RoundedRectangle(width=7.5, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
            thinking_cloud.next_to(dot3, UR)
            mu_thinking = VGroup(dot1,dot2,dot3, thinking_cloud).next_to(bot_thinking, UR)
            mu_thinking.shift(RIGHT)

            # Initial Thought Text: "More curious?"
            thought_text1 = Tex("More curious?").scale(0.9).move_to(thinking_cloud.get_center())

            # Final Thought Text: "Check out books and links!"
            thought_text2 = Tex("Check out books and links!").scale(0.8).move_to(thinking_cloud.get_center())

            # Group Thought Elements
            mu_thinking = VGroup(dot1, dot2, dot3, thinking_cloud, thought_text1)

            # Animate Mu Bot with Thought Cloud
            self.play(FadeIn(mu_thinking))
            self.wait(2)

            # Transform Text in Cloud
            self.play(Transform(thought_text1, thought_text2))
            self.wait(2)

class PiHistorySlopedTimeline(Scene):
    def construct(self):
        # Title
        title = Tex(r"The History of $\pi$ sapns over 4000 years").scale(1.2).to_edge(UP)
        self.play(Write(title))

        # Define the slope direction (diagonal timeline)
        start_point = LEFT * 4.5 + DOWN * 2  # Bottom-left
        end_point = RIGHT * 4.5 + UP * 2  # Top-right
        timeline = Line(start_point, end_point, color=WHITE)

        # Key Events: (Year, Mathematician, Contribution)
        events = [
            ("250 BCE", "Archimedes", r"\text{Polygon Approximation}"),
            ("1600s", "Isaac Newton", r"\text{Calculus-Based Computation}"),
            ("1706", "John Machin", r"\text{Machin's Formula}"),
            ("1910s", "Ramanujan", r"\text{Rapidly Converging Series}"),
            ("1980s", "Chudnovsky Bros", r"\text{Fastest } \pi \text{ Algorithm}"),
            ("2022", "Google", r"\text{100 Trillion Digits Computed}"),
        ]

        # Create event markers along the sloped timeline
        markers = []
        texts = []
        num_events = len(events)

        for i, (year, name, fact) in enumerate(events):
            # Positioning each event diagonally along the sloped line
            t = i / (num_events - 1)  # Normalized position along the slope
            x_pos = interpolate(start_point[0], end_point[0], t)
            y_pos = interpolate(start_point[1], end_point[1], t)
            event_pos = np.array([x_pos, y_pos, 0])

            marker = Dot(point=event_pos, color=RED)
            year_label = Tex(year).scale(0.6).next_to(marker, LEFT if i % 2 == 0 else RIGHT)
            fact_label = MathTex(fact).scale(0.5).next_to(marker, UP if i % 2 == 0 else DOWN, buff=0.3)

            markers.append(marker)
            texts.append(VGroup(year_label, fact_label))

        # Animate the events appearing sequentially
        for i in range(num_events):
            self.play(FadeIn(markers[i]), Write(texts[i]), run_time=1)
            self.wait(0.5)

        self.wait(3)