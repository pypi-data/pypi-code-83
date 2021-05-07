import mkslug


def main() -> None:

    print("Make a Slug from Sentence You Provide.")

    error = True

    while error:
        sentence = input("Please enter one sentence and press the return/enter key: ")
        error, error_text = mkslug.check_for_errors(sentence)
        if error:
            print(error_text)

    slug = mkslug.generate(sentence)
    print("The generated slug is:")
    print(f"{slug}")


if __name__ == "__main__":
    main()
