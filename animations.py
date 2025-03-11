from manim import *
import math
import numpy as np
# Set global background color
config.background_color = "#1E1E1E"  # Dark gray background

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
        tex = Tex("Binomial Expansion", color = BLUE).move_to(DOWN)
        # Transition to display the binomial expansion for sqrt(1-x^2)
        expansion = MathTex(r"\sqrt{1-x^2} = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \cdots", color=WHITE).scale(0.8).next_to(tex, DOWN)
        self.play(Write(tex), ReplacementTransform(integral_eq.copy(), expansion))
        self.play(ShowCreationThenFadeOut(SurroundingRectangle(expansion)))
        self.wait(1)