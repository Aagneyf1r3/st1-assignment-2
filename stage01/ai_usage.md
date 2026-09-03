# AI Usage Log

## Part C — AI as Tutor

**Tool used:** Microsoft Copilot

**Prompt:**
Act as a Python tutor. I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

**AI response summary:**
- Explained the code correctly (list of dictionaries, book_appointment adds,
  display_appointments prints)
- Identified 3 limitations: only patient name is validated, duplicate
  bookings allowed with no warning, data lost when program ends (no persistence)
- Suggested: add validation for practitioner/time, add duplicate check,
  add an interactive menu/loop

**AI's questions to me:**
1. Why is it useful to store appointments in a list of dictionaries instead
   of separate variables?
2. What happens if you call book_appointment() with an empty practitioner name?

**My answers:**
1. A list of dictionaries lets multiple appointments be stored together, with
   each dictionary holding one appointment's data (patient, practitioner, time).
   This scales far better than separate variables per appointment.
2. Nothing would stop it — only patient_name is checked, so an empty
   practitioner name would be silently accepted and added to the list.

**What I accepted / rejected / modified:**
- All three of AI's limitations matched limitations I had already found
  independently in Part B (empty-field handling, duplicates, no persistence).
- AI did not surface any new limitation beyond what my own testing found.
- This suggests my Part B testing was already fairly thorough.

## Part D — AI Generates an Alternative

**Tool used:** Microsoft Copilot (new/fresh chat, no file context)

**Prompt:**
Write a simple, beginner-friendly Python function that stores a patient name,
practitioner name, and appointment time for a small clinic appointment booking
system. Do not use a database. Do not create a GUI. Keep it simple enough for
someone learning introductory programming.

**Note:** First attempt (with file context open) returned code nearly
identical to my own Part B version. Started a fresh chat with no file
context to get an independently generated version instead.

**AI-generated code saved as:** stage01/smartcare_ai_version.py

**Result of running it:** Ran successfully with no errors. Produced two
"Appointment booked successfully!" messages followed by a formatted list
of both appointments.

**Key differences noticed vs. my Part B version:**
- No validation at all — does not check for empty patient_name (my version
  raises a ValueError for this)
- Prints a confirmation message after each booking (mine is silent)
- Adds header/footer formatting to the appointment list output
- Includes docstrings for both functions (mine does not)

## Part F — Verify Behaviour (Testing Both Versions)

**Test 1 — Blank patient name:**
- My version (smartcare_v01.py): crashed with ValueError("Patient name cannot be empty")
- AI version (smartcare_ai_version.py): ran successfully, printed
  "Appointment booked successfully!" with no warning at all

**Test 2 — Exact duplicate booking:**
- My version: silently added the duplicate, no warning
- AI version: silently added the duplicate, no warning

**Test 3 — None, None, None:**
- My version: crashed with the same ValueError as Test 1
- AI version: ran successfully, silently accepted all three None values

**Conclusion:** My version fails hard (crashes) on invalid input but has at
least one safeguard (patient name check). AI's version never crashes but has
zero validation on any field — it will silently accept blank names, None
values, and duplicate bookings without any warning. Neither approach is
actually correct; a good solution would validate input AND fail gracefully
(e.g. print an error message and skip the booking, rather than crashing or
silently

## Other Resources Used

- W3Schools (w3schools.com) — used throughout to look up Python syntax and
  concepts (e.g. f-strings, dictionaries, exception handling).

## Note on Documentation Assistance

I used Copilot to help me organise and format this documentation
(ai_usage.md, comparison.md, and reflection.md) into clear Markdown, since
I was unfamiliar with Markdown syntax and file structure. The engineering
decisions, code, testing, and reasoning throughout are my own — Claude
helped me structure and phrase how I recorded them, not what I decided or
built.