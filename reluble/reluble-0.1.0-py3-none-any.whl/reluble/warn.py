from termcolor import colored


def warn(corruption, message: str = "") -> None:
    print(
        "{}: {}: {}".format(
            colored("CORRUPTION HYPOTHESIS FAILED", "red"),
            colored(corruption, "blue"),
            message,
        )
    )
    while True:
        response = input("Proceed anyway? (y/n/?) ").lower().strip()
        if response in ["y", "n", "?"]:
            break
        print(colored(f"{response} not in (y/n/?)", "red"))

    # TODO: an individual warning should only get triggered once, after which the hook should be
    # removed for speed.
    # TODO: if no response in some set period (say, five minutes), computation is
    # continued.
    if response == "y":
        return
    elif response == "n":
        quit()
    elif response == "?":
        raise NotImplementedError
    else:
        raise ValueError
