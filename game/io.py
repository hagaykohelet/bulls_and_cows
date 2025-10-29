


def prompt_guess() -> str:
    guess = input("please enter your guess number ")
    return guess


def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"your {guess} score: bulls = {bulls} cows = {cows}")


def print_status(state) -> None:
    print(f"your history: {state["history"]}")
    print(f"the current turn: {state["tries_used"]} / {state["max_tries"]}")



def print_result(state) -> None:
    # print(won)
    print(f"the num is: {state}")