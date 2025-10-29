import random
def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool =True,
rng: random.Random | None = None) -> str:
    nums = [0,1,2,3,4,5,6,7,8,9]
    if length > 10:
        raise "you need enter less than 10"
    guess_visible = []
    guess_hide = []
    counter = 0
    if allow_leading_zero:
        while counter < length:
            hide_num = random.randint(0,len(nums)-1)
            if str(nums[hide_num]) in guess_hide:
                continue
            else:
                guess_visible.append("-")
                guess_hide.append(str(nums[hide_num]))
                counter += 1

    if not allow_leading_zero:
        first_num = random.randint(1, len(nums) - 1)
        guess_hide.append(str(nums[first_num]))
        guess_visible.append("-")
        while counter < length - 1:
            hide_num = random.randint(0, len(nums) - 1)
            if nums[hide_num] in guess_hide:
                continue
            else:
                guess_visible.append("-")
                guess_hide.append(str(nums[hide_num]))
                counter += 1


    return guess_hide,guess_visible
