import os

# ── Paths ────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAMES_FILE = os.path.join(BASE_DIR, "data", "invited_names.txt")
LETTER_FILE = os.path.join(BASE_DIR, "data", "starting_letter.txt")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

PLACEHOLDER = "[name]"

# ── Read template letter ──────────────────────────────
with open(LETTER_FILE) as f:
    template = f.read()

# ── Read guest names ──────────────────────────────────
with open(NAMES_FILE) as f:
    names = [line.strip() for line in f.readlines()]

# ── Generate a personalised letter for each name ──────
os.makedirs(OUTPUT_DIR, exist_ok=True)

for name in names:
    personalised = template.replace(PLACEHOLDER, name)
    out_path = os.path.join(OUTPUT_DIR, f"letter_for_{name}.txt")
    with open(out_path, "w") as f:
        f.write(personalised)
    print(f"✅ Created: letter_for_{name}.txt")

print(f"\n📁 All letters saved in: {OUTPUT_DIR}")
