def generate_gray_code(n: int) -> list:
    if n == 0:
        return [""]
    else:
        gray_code = generate_gray_code(n - 1)  # hamming distance
        return ["0" + c for c in gray_code] + ["1" + c for c in reversed(gray_code)]

n = int(input())
gray_codes = generate_gray_code(n)
for gc in gray_codes:
    print(gc)

