def score_guess(secret: str, guess: str, length) -> tuple[int, int]:
    bool = 0
    cow = 0
    # for index in range(length):
    #     if guess[index] == guess[index]:
    #         bool += 1
    if secret == guess:
        pass

print(score_guess("1215","1215",4))

def is_won(bulls: int, length: int) -> bool:
    pass



GameState = {   "secret": str,
        "length": int,
        "max_tries": int | None,
        "tries_used": int,
        "unique_digits": bool,
        "allow_leading_zero": bool,
        "history": list[tuple[str, int, int]],
        "seen": set[str]}


def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> GameState:
    pass


def apply_guess(state: GameState, guess: str) -> tuple[int, int] :
    pass


