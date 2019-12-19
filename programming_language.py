class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        """Show the attributes of the function """
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return a string"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """test which programming language is dynamic in typing"""
        return self.typing == "Dynamic"


def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus = ProgrammingLanguage("Ruby", "Dynamic", False, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    languages = [ruby, python, visual_basic]
    print(java)
    print(c_plus)
    print(python)
    print(visual_basic)
    print(ruby)
    print("The dynamically typed languages are:")
    for i in languages:
        if i.is_dynamic():
            print(i.language)


if __name__ == '__main__':
    main()
