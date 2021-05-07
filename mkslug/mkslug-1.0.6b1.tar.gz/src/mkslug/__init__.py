import re


def check_for_errors(sentence: str) -> tuple[bool, str]:
    """
    Check for errors on the sentence.

    Args:
        sentence: The sentence to check.

    Returns:
        error bool and error text message.
    """

    error = True
    error_text = None

    while error:

        if not sentence:
            error_text = "The sentence must be populated. Please try again."
            break

        pattern = "[^a-zA-Z0-9\s-]"
        found = re.findall(pattern, sentence)
        if found:
            regex_error_text = ""
            found_len = len(found)

            for i in range(found_len):
                regex_error_text += found[i]

            error_text = f"Found one or more special characters in the sentence ({regex_error_text}). Please try again without any special characters."
            break

        error = False

    return error, error_text


def generate(sentence: str) -> str:
    """
    Generate a slug from a sentence.

    Args:
        sentence: The sentence to check.

    Returns:
        generated slug value.
    """

    slug = sentence.strip()
    slug = slug.lower()
    slug = slug.replace(" ", "-")

    return slug
