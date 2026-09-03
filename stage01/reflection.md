Before using AI, I built the initial SmartCare prototype myself by following
the Stage 1 instructions. I started with a simple version that printed two
hard-coded appointments, and then expanded it into a more flexible design
using lists, dictionaries, and functions. Writing the enhanced version helped
me understand how data structures make the program easier to extend, and my
own testing revealed several limitations, including blank fields, duplicate
bookings, and the fact that all data disappears when the program closes.

When I used AI as a tutor, it mostly confirmed the issues I had already
found. The AI explained my code clearly and identified the same three
limitations I discovered through testing: incomplete validation, silent
duplicates, and lack of persistence. This showed me that my manual testing
was thorough. The AI also suggested improvements like adding validation for
all fields and creating an interactive menu, which were reasonable but not
required for Stage 1. I also noticed the AI assumed validation wasn't
necessary, since its own generated version accepted blank names and
duplicate bookings without any warning. I accepted the validation
suggestion and implemented consistent required-field checks across patient,
practitioner, and time.

Comparing my version with the AI-generated version highlighted that the
AI's code was simpler but lacked any validation. Testing both versions
confirmed that mine fails loudly while the AI's fails silently. Even with
AI assistance, I still had to write the code, test behaviour, interpret
results, and decide which improvements were appropriate. The engineering
work remained my responsibility.