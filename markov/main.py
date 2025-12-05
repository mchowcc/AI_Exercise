import random
import model_builder
import generator


def main():
    # random.seed(42)  # optional: deterministic runs for testing
    path = input("Corpus filename (.txt): ").strip()

    # Call read_corpus
    try:
        tokens = model_builder.read_corpus(path)
    except FileNotFoundError:
        print(f"Could not open '{path}'. Please provide a valid file path.")
        return

    # Call build_bigram_model
    words, followers = model_builder.build_bigram_model(tokens)

    print("\n=== Generated text ===")

    # Call generate_from_bigram and print the result
    answer = "y"
    while answer != "n":
        sample = generator.generate_from_bigram(words, followers)
        print(sample)
        answer = input("? ")


if __name__ == "__main__":
    main()
