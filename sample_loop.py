
def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if line.lower().startswith(("exit", "quit")):
            print("done")
            break
        words = line.split()
        if len(words) != 3:
            print(f"Error: input has {len(words)} words", file=sys.stderr)
        else:
            print("Success: input has 3 words", file=sys.stdout)


if __name__ == "__main__":
    main()
