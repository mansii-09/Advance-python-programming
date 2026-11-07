import re


def is_valid_pin(text):
    """Return True only for a complete 6-digit Indian PIN starting from 1-9."""
    return re.match(r"^[1-9]\d{5}$", text) is not None


def find_mobile(text):
    """Return the first 10-digit Indian mobile number, optionally with +91."""
    pattern = r"(?<!\d)(?:\+91)?[6-9]\d{9}(?!\d)"
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None


def count_pins():
    """Read addresses.txt and print each distinct PIN with its frequency."""
    with open("addresses.txt", "r", encoding="utf-8") as file:
        addresses = file.read()

    # Word boundaries prevent PINs from being extracted from longer numbers.
    pins = re.findall(r"\b[1-9]\d{5}\b", addresses)

    pin_counts = {}
    for pin in pins:
        pin_counts[pin] = pin_counts.get(pin, 0) + 1

    print("PIN code counts:")
    for pin, count in pin_counts.items():
        print(pin, ":", count)


if __name__ == "__main__":
    print("PIN validation:")
    for pin in ["380015", "110001", "056001", "38001", "3800155", "38O015"]:
        print(pin, "->", is_valid_pin(pin))

    print("\\nMobile search:")
    for sentence in [
        "Call 9000012345 after 6 pm",
        "Reach me on +919000012345",
        "Flat 5000012345",
        "Ring 900001234",
    ]:
        print(sentence, "->", find_mobile(sentence))

    print()
    count_pins()
