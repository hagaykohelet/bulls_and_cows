from game.secret import generate_secret
from game.io import print_result,print_status,prompt_guess,print_feedback
from game.logic import score_guess,apply_guess,init_state,is_won
from game.validate import is_valid_guess,is_new_guess

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    visible_nums,hide_nums = generate_secret(length)
    print(visible_nums)
    game_state = init_state(hide_nums,length,max_tries,unique_digits,allow_leading_zero)
    while not game_state["tries_used"] == game_state["max_tries"]:
        guess = prompt_guess()
        check = is_valid_guess(guess,length)
        if not check[0]:
            print(f"you need enter {game_state["length"]}")
            continue
        else:
            bool,cow = score_guess(visible_nums,guess,length)
            # print_status(game_state)
            if not is_won(bool,length):
                if not is_new_guess(guess,game_state["history"]):
                    continue
                else:
                    print_feedback(guess,bool,cow)
                    apply_guess(game_state,guess)
                    print_status(game_state)
            else:
                print("this the num")
                print_result(visible_nums)
                break

if __name__ == "__main__":
   play()