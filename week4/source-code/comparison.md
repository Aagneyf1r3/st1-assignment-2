# Comparison: Human Version vs AI Version

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes — simple variables/prints, then list+dict+functions | Yes — similar structure, plus docstrings |
| Runs successfully? | Yes, no errors on normal input | Yes, no errors on normal input |
| Uses only required features? | Yes — variables, lists, dictionaries, functions only | Yes — same, no database/GUI as instructed |
| Adds assumptions? | No extra assumptions | Assumes no validation is needed; adds confirmation messages and formatted headers not requested |
| Handles errors? | Partial — rejects blank/None patient name (crashes), but practitioner/time are unchecked | None — accepts blank names, None values, and duplicates with no warning at all |
| Could I explain it? | Yes | Yes |

## Summary

Both versions are structurally very similar — a list of dictionaries with a
booking function and a display function — because this is a fairly standard,
obvious solution for a beginner-level task. The real difference is in error
handling: my version has one safeguard (rejects blank/None patient names,
though this crashes the program rather than failing gracefully), while AI's
version has none at all and will silently accept any input, including blank
names and duplicate bookings. This was confirmed through direct testing
(see ai_usage.md, Part F) rather than assumed from reading the code.
