import random
import model_builder
import generator


def main():
    # random.seed(42)  # optional: deterministic runs for testing
    path = input("Corpus filename (.txt): ").strip()
    tokens = []

    # TODO: Call read_corpus
    # tokens =

    # Call build_bigram_model
    words, followers = model_builder.build_bigram_model(tokens)

    print("\n=== Generated text ===")

    # TODO: Call generate_from_bigram and print the result
    # Optional: the call can be in a loop, asking the user if they want another one.
    pass


if __name__ == "__main__":
    main()
