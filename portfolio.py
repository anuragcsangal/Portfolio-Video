from manim import *
import manimpango

class Portfolio(Scene):
    def construct(self):
        # Warning Text
        warning_text = Text("This video is created using Python", color="red", font_size=15).align_on_border(UP)
        self.add(warning_text)

        # Intro
        first_text = ["Everyone makes portfolio websites as Programmers", "If we can Program a Video", "Why not do it ??"]

        for text in range(0, len(first_text)):
            t = Text(first_text[text], font_size=25, font="Monospace")
            self.play(Write(t))
            self.wait(0.5)
            self.remove(t)
            self.remove(warning_text)

        second_text = ["Hello Everyone","I'm Anurag Angal","Studying Electronics and Computer Engineering", "@ P.E.S. Modern College of Engineering, Pune"]

        for text in range(len(second_text)):
            t = Text(second_text[text], font_size=25, font="Monospace")
            self.play(Write(t), run_time=1)
            self.wait(0.5)
            self.remove(t)

        # Core Skills
        core_skills = Text("My Core Skills are", font_size=30, font="Monospace")
        self.add(core_skills.to_edge(UP))
        text_inside_box = Text("Out of the box", font_size=13, font="Monospace")
        text_outside_box = Text("thinking", font_size=15, font="Monospace").shift(RIGHT*2)
        square = Square()
        self.play(Write(square), run_time = 0.5)
        self.play(Write(text_inside_box),run_time = 0.5)
        self.play(Write(text_outside_box), run_time = 0.5)
        self.play(square.animate.shift(LEFT*5))
        self.play(text_inside_box.animate.shift(LEFT*5))
        self.play(text_outside_box.animate.rotate((PI + PI/2)).shift(LEFT*5.25))

        second_core_skill_word = Text("Problem", font_size=15, font="Monospace")
        second_core_skill_word2 = Text( "Solving", font_size=15, font="Monospace").next_to(second_core_skill_word)
        self.play(Write(second_core_skill_word))
        self.play(Write(second_core_skill_word2))
        self.play(second_core_skill_word.animate.shift(RIGHT*5))
        self.play(second_core_skill_word2.animate.shift(DOWN*0.5).rotate(PI).shift(RIGHT*4))

        third_skill_word = Text("Adaptability", font="Monospace")
        self.play(Write(third_skill_word))
        self.play(third_skill_word.animate.scale(0.25))
        self.remove(square)
        self.remove(core_skills)
        self.remove(text_inside_box)
        self.remove(text_outside_box)
        self.remove(second_core_skill_word)
        self.remove(second_core_skill_word2)
        self.remove(third_skill_word)

        # Technical Skills
        technical_skills = Text("My Technical Skills are", font_size=30, font="Monospace")
        self.play(FadeIn(technical_skills.to_edge(UP)))
        js = Text("Javascript", font_size=20, font="Monospace").shift(UP)
        gt = Text("Git", font_size=20, font="Monospace")
        pcj = Text("Python, C++, Java", font_size=20, font="Monospace").shift(DOWN).shift(LEFT*1.5)
        basic = Text("(Basic)", font_size=20, font="Monospace").shift(DOWN).shift(RIGHT*1.5)
        self.play(Write(js))
        self.play(Write(gt))
        self.play(Write(pcj))
        self.play(Write(basic))
        self.wait(2)
        self.remove(js)
        self.remove(gt)
        self.remove(pcj)
        self.remove(basic)
        self.remove(technical_skills)

        technical_text1 = Text("I may not know the programming languages at tip of my toungue", font_size=25, font="Monospace")
        technical_text2 = Text("but whatever is required to solve a problem is what I execute", font_size=25, font="Monospace")
        self.play(Write(technical_text1))
        self.wait(0.5)
        self.remove(technical_text1)
        self.play(Write(technical_text2))
        self.wait(1)
        self.remove(technical_text2)

        # # End
        # last_text = Text("My passion for computers and programming give me energy to Work Hard and to find a solution", font_size=15, font="Monospace")
        # self.play(Write(last_text))
        # self.play(last_text.animate.to_edge(UP))
        # socials_text = Text("You can find me at", font_size=15, font="Monospace")
        # self.play(Write(socials_text))
        # self.play(socials_text.animate.shift(UP))
