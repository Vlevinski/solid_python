# Simple decorator

def decorator_(func):
    def wrapper(text):
        return func(f"* {text} *")
    return wrapper


@decorator_
def show(text):
    """ Text with the decoration"""
    print(text)


if __name__ == "__main__":
    # Show the decorated text
    show("Hello")

#   * Hello *
