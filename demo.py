# -*- coding: utf-8 -*-

from lipsum import generate_words, generate_sentences, generate_paragraphs


if __name__ == "__main__":
    print("Lorem Ipsum generator!")
    print("\n------------------------")
    print("Generating 100 words:")
    print(generate_words(100))

    print("\n------------------------")
    print("Generating 5 sentences:")
    print(generate_sentences(5))

    print("\n------------------------")
    print("Generating 3 paragraphs:")
    print(generate_paragraphs(3))

    print("")
