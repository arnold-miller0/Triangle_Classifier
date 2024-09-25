
def classify_triangle(sides):
    # slides is array of 3 numbers
    a, b, c = sorted(sides)
    if a + b <= c:
        return "NoTriangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    import sys
    for line in sys.stdin:
        
        words = line.strip().split()

        # exit when first work is Exit or Quit (lowercase)
        len_words = len(words)
        if len_words >= 1:
            input = words[0].lower()
            if input == "exit" or input == "quit":
                print(f"triangle classifier done")
                break

        # error when more-than 3 input words
        if len_words > 3:
            print(f"Error: More than Three words provided" 
                  , file=sys.stderr)
            continue

        non_count = 0
        num_sides = []
        for word in words:
            try:
                num_sides.append(float(word))
            except ValueError:
                non_count += 1

        num_count = len(num_sides)
        if num_count == 3:
            print(classify_triangle(num_sides))
            continue
        else:
            num_error = f"{'One side' if num_count == 2 else 'Two sides' if num_count == 1 else 'Three sides'} missing"
            print(f"Error: {num_error}{' with Non-numeric words' if non_count > 0 else ''}"
                  , file=sys.stderr)
       
if __name__ == "__main__":
    main()
