from format_checker import is_valid_pin, find_mobile


def clean_contacts():
    with open("contacts.txt", "r", encoding="utf-8") as source:
        lines = source.readlines()

    valid_lines = []
    rejected_lines = []

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split(",")]

        if len(fields) != 3:
            rejected_lines.append(
                f"{line} | Rejected: expected Name,Mobile,PIN (3 fields)"
            )
            continue

        name, mobile, pin = fields
        reasons = []

        # The complete mobile field must match; a number embedded in extra text
        # is not accepted as a valid contact mobile.
        if find_mobile(mobile) != mobile:
            reasons.append("Invalid mobile number")

        if not is_valid_pin(pin):
            reasons.append("Invalid PIN code")

        if reasons:
            rejected_lines.append(
                f"{name},{mobile},{pin} | Rejected: {', '.join(reasons)}"
            )
        else:
            valid_lines.append(f"{name},{mobile},{pin}")

    with open("valid_contacts.txt", "w", encoding="utf-8") as valid_file:
        valid_file.write("\\n".join(valid_lines))
        if valid_lines:
            valid_file.write("\\n")

    with open("rejected_contacts.txt", "w", encoding="utf-8") as rejected_file:
        rejected_file.write("\\n".join(rejected_lines))
        if rejected_lines:
            rejected_file.write("\\n")

    print("Contact cleaning completed.")
    print("Valid contacts:", len(valid_lines))
    print("Rejected contacts:", len(rejected_lines))


if __name__ == "__main__":
    clean_contacts()
