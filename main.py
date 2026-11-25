"""The Funniest Office Joke, Judged Head to Head — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the printer prints money for the company, just not for me.
TEXT = "I asked HR if my printer could get a raise. They said it already prints money for the company — just not for me."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
