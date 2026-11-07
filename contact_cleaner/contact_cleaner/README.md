# Contact Cleaner Assignment

## Files
- `format_checker.py`: PIN validation, mobile search, and PIN frequency count.
- `addresses.txt`: 8 invented address lines used by `count_pins()`.
- `contact_cleaner.py`: imports the functions and cleans the contacts file.
- `contacts.txt`: 12 sample contacts, including invalid examples.
- `valid_contacts.txt` and `rejected_contacts.txt`: generated output files.

## Run
Open a terminal in this folder and run:

```bash
python format_checker.py
python contact_cleaner.py
```

`format_checker.py` uses `re.match()`, `re.search()`, and `re.findall()` as required.
The sample mobile numbers are dummy/test values, not contact details.
