from sys import argv

script, user_name = argv
prompt = '#' # Achievement Unlocked: Got Root?

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"Is your name really {user_name}?")
nameValidate = input(prompt)

print(f"""
You said {likes} about liking me (hope you were nice to the script...).
You live in {lives}.
You have a {computer} computer. Awesome.
And you said {nameValidate} to {user_name} being your real name
""")
