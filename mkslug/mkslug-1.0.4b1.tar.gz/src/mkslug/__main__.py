import mkslug


def main() -> None:

    print("Make a slug from sentence you provide.")

    error = True

    while error:
        sentence = input("Please enter one sentence: ")
        error, error_text = mkslug.check_for_errors(sentence)
        if error:
            print(error_text)

    slug = mkslug.generate(sentence)
    print("The generated slug is:")
    print(f"{slug}")


if __name__ == "__main__":
    main()
