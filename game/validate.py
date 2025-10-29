def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    if len(guess) > length:
        return False,guess
    return True,guess





def is_new_guess(guess: str, history: set[str]) -> bool:
    if guess in history:
        return False
    return True

