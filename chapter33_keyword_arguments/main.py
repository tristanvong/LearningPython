def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")

hello("Hello", "Mr.", "Vong", "Tristan") # position matters expected outcome: "Hello Mr.Vong Tristan"
hello("Hello", title="Mr.", last_name="Vong", first_name="Tristan") # specify which variable needs to have which value
# position doesnt matter expected outcome: "Hello Mr.Tristan Vong"
#improves readability
# but a caveat: positional arguments need to be before the keyword arguments otherwise -> error