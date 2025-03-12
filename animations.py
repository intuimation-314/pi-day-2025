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
             ).scale(0.7).set_color(WHITE).to_edge(UP)
        
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
        bot_body = VGroup(mu, eyes).scale(1.5)
        
        # Mouth expressions (arc for different moods)
        happy_mouth = Arc(radius=0.2, start_angle=-3*PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.5)
        sad_mouth = Arc(radius=0.2, start_angle=PI/4, angle=2*PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT).scale(1.5)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE).scale(1.5)
        
        # Assemble complete bot expressions using the scaled bot body
        bot_thinking = VGroup(bot_body, thinking_mouth).to_edge(DL)
        bot_happy = VGroup(bot_body.copy(), happy_mouth)
        bot_sad = VGroup(bot_body.copy(), sad_mouth)
        
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
        self.play(FadeIn(bot_thinking), 
                  Create(mu_thinking))
        self.play(blink(), run_time = 0.5)
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

class EngMath(Scene):
    def construct(self):
        # Load engineer and mathematician images (keeping your original positions)
        engineer = ImageMobject("engineer.png").scale(0.8).to_edge(UL)  # Engineer at Upper Left
        mathematician = ImageMobject("mathematician.png").scale(0.8).to_edge(DR)  # Mathematician at Down Right
        
        # Titles above the images
        engineer_title = Text("Engineers", font_size=36, color=WHITE).next_to(engineer, UP, buff=0.1)
        mathematician_title = Text("Mathematicians", font_size=36, color=WHITE).move_to(3*RIGHT)
        
        # Create text labels for their respective pi usage
        engineer_pi_approx = MathTex(r"\pi \approx 3.14 \text{ or } \pi \approx 3", color=WHITE)
        engineer_pi_approx.next_to(engineer, RIGHT, buff=0.5)  # Positioned to the right of the engineer
        
        math_pi_precise = MathTex(r"\pi = 3.1415926535 8979323846 2643383279 \dots", color=WHITE).scale(0.8)
        math_pi_precise.move_to(DOWN + 2 * LEFT) # Positioned to the left of the mathematician
        
        # Add everything to the scene
        self.add(engineer, mathematician, engineer_title, mathematician_title, engineer_pi_approx, math_pi_precise)

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
       image = ImageMobject("archimedes.png").scale(0.8)
       self.add(image)
   
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
        self.play(Write(bounds))
        self.wait(2)

class NewtonQuarterCircle(Scene):
    def construct(self):
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
        group = VGroup(circle, axes, quarter).scale(1.5).to_edge(UR)
        self.play(Create(group))
        
        # Display the integral equation below the axes
        integral_eq = MathTex(r"\int_0^1 \sqrt{1-x^2}\,dx = \frac{\pi}{4}", color=WHITE).scale(0.8)
        integral_eq.shift(UP)
        self.play(Write(integral_eq))
        self.wait(1)
        tex = Tex("Binomial Expansion", color = BLUE).move_to(          DOWN)
        # Transition to display the binomial expansion for sqrt(1-x^2)
        expansion = MathTex(r"\sqrt{1-x^2} = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \cdots", color=WHITE).scale(0.8).next_to(tex, DOWN)
        self.play(Write(tex), ReplacementTransform(integral_eq.copy(), expansion))
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(expansion)))
        self.wait(1)