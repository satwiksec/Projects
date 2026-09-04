import string

alpha = list(
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation +
    " "
)

MAX_KEY = len(alpha) - 1


while True:

    print("\n" + "=" * 50)
    print("             🔐 SATWIK CIPHER 🔐")
    print("=" * 50)
    print("[E] Encrypt")
    print("[D] Decrypt")
    print("[Q] Quit")
    print("=" * 50)

    choice = input("Your choice: ").strip().lower()

    if choice == "q":
        print("\n Thank you for using Satwik Cipher!")
        break

    if choice not in ("e", "d"):
        print("\n❌ Invalid option!")
        continue

    # ------------------------ Key ----------------------

    while True:
        try:
            key = int(input(f"\nEnter key (0-{MAX_KEY}): "))

            if 0 <= key <= MAX_KEY:
                break

            print(f"❌ Key must be between 0 and {MAX_KEY}.")

        except ValueError:
            print("❌ Please enter a valid integer.")

    # ------------------------ Message ----------------------

    print("\nPaste your message below.")
    print("Type END on a new line when you're finished.\n")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    message = "\n".join(lines)

    # ------------------ Encryption Logic ----------------------

    shift = key if choice == "e" else -key

    result = ""

    for ch in message:

        # Preserve unsupported characters
        if ch not in alpha:
            result += ch
            continue

        index = alpha.index(ch)
        new_index = (index + shift) % len(alpha)
        result += alpha[new_index]

    # ---------------- Output -------------------

    print("\n" + "=" * 50)

    if choice == "e":
        print("🔒 ENCRYPTED MESSAGE")
    else:
        print("🔓 DECRYPTED MESSAGE")

    print("-" * 50)
    print(result)
    print("=" * 50)

    again = input("\nRun again? (Y/N): ").strip().lower()

    if again != "y":
        print("\n Goodbye!")
        break
