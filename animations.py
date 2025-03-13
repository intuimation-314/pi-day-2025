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
                r"The most fundamental mathematical constants we encounter early in our life."
             ).scale(0.8).set_color(WHITE).to_edge(UP)
        
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

        tex1 = Tex("That's not how we compute PI").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Physical measurements always", "lead to an error!")
        tex3 = Tex("Engineers might use 3.14 or even 3").scale(0.8).move_to(thinking_cloud.get_center())
        tex4 = Tex("But Mathematicians ?", "They want infinite precision").scale(0.8).move_to(thinking_cloud.get_center())
        tex2.arrange(DOWN)
        tex4.arrange(DOWN).move_to(thinking_cloud.get_center())

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(bot_thinking), 
                  FadeIn(mu_thinking))
        self.play(blink(), run_time = 0.5)
        self.play(Write(tex1))
        self.play(blink(), run_time=0.5)
        self.play(Transform(tex1, tex2))
        self.wait(2)

        engineer = ImageMobject("image.png").scale(0.8).to_edge(DR)
        self.play(FadeIn(engineer),
                  Transform(tex1, tex3))
        self.play(blink(), run_time=0.5)
        self.wait()

        math = ImageMobject("mathematician.png").scale(0.8).to_edge(DR)
        math.shift(RIGHT)
        self.play(FadeOut(engineer),
                  FadeIn(math),
                  Transform(tex1, tex4))
        self.play(blink(), run_time=0.5)

class PiFormulas(Scene):
    def construct(self):
        # Load 4 uncanny images (assuming file names are "phase1.png", "phase2.png", etc.)
        images = [
            ImageMobject("phase1.png").scale(0.8),
            ImageMobject("phase2.png").scale(0.8),
            ImageMobject("phase3.png").scale(0.95).move_to(DOWN),
            ImageMobject("phase4.png").scale(0.8),
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
        
        image1 = ImageMobject("google.png").scale(2).to_edge(UP)
       
        pi_digits_text = Tex("- 100 Trillion Digits")
        days_text = Tex("- 157 days of computation!")
        storage_text = Tex("- 82k TB storage")
        electricity_text = Tex("- 200,000 dollars!")
        text = VGroup(pi_digits_text, days_text,
                      storage_text, 
                      electricity_text).arrange(DOWN, buff = 0.3, aligned_edge = LEFT)
        text.next_to(image1, DOWN)

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
            Tex(r"7372458700 6606315588 1748815209 2096282925 4091715364"),
            Tex(r"3678925903 6001133053 0548820466 5213841469 5194151160\ldots")
        ).scale(0.65)
        pi_digits.arrange(DOWN, buff = 0.5, center=False, aligned_edge=LEFT)
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

        tex1 = Tex("Why ??").scale(0.8).move_to(thinking_cloud.get_center())
        tex2 = Tex("Why PI get so ridiculously", "complicated?")
        tex3 = Tex("Why more and more digits?").scale(0.8).move_to(thinking_cloud.get_center())
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(bot_thinking), 
                  FadeIn(mu_thinking))
        self.play(blink(), run_time = 0.5)
        self.play(Write(tex1))
        self.play(blink(), run_time=0.5)
        self.play(Transform(tex1, tex2))
        self.wait(2)


class PiRatio(Scene):
    def construct(self):
        # Define circle and diameter
        circle = Circle(radius=2, color=BLUE)
        circle.move_to(UP)  # Move the circle up slightly
        diameter = Line(circle.get_left(), circle.get_right(), color=YELLOW)

        # Define bottom line (equal to circumference)
        circumference_length = 2 * PI * circle.radius
        bottom_line = Line(circle.get_left(), circle.get_left() + RIGHT * circumference_length, color=BLUE)
        bottom_line.move_to(DOWN * 2.5)  # Move below the circle

        # Create labels
        pi_text = MathTex(r"\pi = \frac{C}{d} \approx 3.14").to_edge(LEFT)
        d_text = MathTex(r"d").next_to(diameter, DOWN)
        c_text = MathTex(r"C").next_to(circle, RIGHT)
        unfolded_text = MathTex(r"\text{Unfolding the circumference}").next_to(bottom_line, UP)

        # Show the circle and diameter
        self.play(Create(circle), Create(diameter))
        self.play(Write(pi_text), Write(d_text))

        self.play(Write(c_text))
        
        # Unwrap the circle: Transform the perimeter into the bottom line
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
        leftover_brace = Brace(leftover, DOWN, color = RED)
        leftover_text = MathTex(r"\approx 0.14 d").next_to(leftover, UP)

        self.play(Create(leftover), Write(leftover_text), Create(leftover_brace))

        self.wait(2)

class EngineerScene(Scene):
    def construct(self):
        # Load engineer and mathematician images (keeping your original positions)
        engineer = ImageMobject("engineer2.png").to_edge(LEFT) # Engineer at Upper Left
        
        # Titles above the images
        engineer_title = Tex("Engineers", color=BLUE).scale(2).to_edge(UP)
        mathematician_title = Text("Mathematicians", font_size=36, color=WHITE).move_to(3*RIGHT)
        
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
        mathematician = ImageMobject("math.png").to_edge(DR).shift(RIGHT)  # Mathematician at Down Right
        mathematician_title = Tex("Mathematicians").scale(2).to_edge(UP)
        
        math_pi_precise = VGroup(
            Tex(r"3.1415926535 8979323846 2643383279"),
            Tex(r"5028841971 6939937510 5820974944 \ldots")
        ).scale(0.8)
        math_pi_precise.arrange(DOWN).move_to(2 * LEFT) # Positioned to the left of the mathematician
        
        # Add everything to the scene
        # self.add(engineer, engineer_title, engineer_pi_approx, engineer_pi_approx2)
        self.play(FadeIn(mathematician),
                  FadeIn(mathematician_title),
                  Write(math_pi_precise),
                )
        
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

        tex = Tex("1630").to_edge(UP)
        tex1 = Tex("Millions of sides")

        self.play(FadeOut(progression),
                  FadeOut(bounds),
                  FadeOut(numeric_bounds))
        self.wait()

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