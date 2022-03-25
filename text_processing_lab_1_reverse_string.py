text = input()
while text != "end":
    reversed_text = reversed(text)
    print(f"{text} = {''.join(reversed_text)}")

    text = input()

