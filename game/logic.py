def score_guess(secret: str, guess: str, length) -> tuple[int, int]:
    bool = 0
    cow = 0
    for index in range(length):
        if secret[index] == guess[index]:
            bool += 1
        if secret[index] != guess[index]:
            if guess[index] in secret:
                cow += 1



    return bool,cow



def is_won(bulls: int, length: int) -> bool:
    return bulls == length




def init_state(secret: str, length: int, max_tries: int | None, unique_digits = False, allow_leading_zero=False,seen = ()):
    game_state = {"secret": secret,
                  "length": length,
                  "max_tries": max_tries,
                  "tries_used": 0,
                  "unique_digits":unique_digits,
                  "allow_leading_zero":allow_leading_zero,
                  "history":[],
                  "seen":set()
                  }
    return game_state

def apply_guess(state, guess: str):

    state["tries_used"] += 1
    state["history"].append(guess)
    return state





