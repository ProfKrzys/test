class color:
    @staticmethod
    def bright_black(text):
        return f"\033[90m{text}\033[0m"  # ANSI escape sequence for bright black
    
    @staticmethod
    def green(text):
        return f"\033[92m{text}\033[0m"  # ANSI escape sequence for green
    
    @staticmethod
    def white(text):
        return f"\033[97m{text}\033[0m"  # ANSI escape sequence for white

    @staticmethod
    def red(text):
        return f"\033[91m{text}\033[0m"  # ANSI escape sequence for red

    @staticmethod
    def dark_yellow(text):
        return f"\033[33m{text}\033[0m"  # ANSI escape sequence for dark yellow
