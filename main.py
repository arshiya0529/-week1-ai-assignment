# ============================================================
#  Smart Student Assistant
#  Name  : Shaik Arshiya Tabasum
#  Roll  : 24JR1A0529
#  Week 1 Assignment — AIML Internship
# ============================================================

import json
import datetime
import random
import os

# ── Load tips and quotes from JSON ──────────────────────────
def load_json(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ── Save output to output.txt ────────────────────────────────
def save_output(text):
    with open("output.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[{timestamp}]\n{text}\n{'-'*40}\n")

# ── Feature 1: Study Tips ────────────────────────────────────
def generate_study_tips(data):
    tips = data.get("study_tips", [
        "Break your study sessions into 25-minute Pomodoro intervals.",
        "Teach what you've learned to someone else — it reinforces memory.",
        "Use active recall: close your notes and try to remember key points.",
        "Review your notes within 24 hours to boost long-term retention.",
        "Stay hydrated and take short breaks to keep your brain fresh.",
    ])
    print("\n📚 Here are your Study Tips:")
    print("=" * 45)
    selected = random.sample(tips, min(3, len(tips)))
    for i, tip in enumerate(selected, 1):
        print(f"  {i}. {tip}")
    print("=" * 45)
    save_output("STUDY TIPS:\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(selected)))

# ── Feature 2: Motivation Quote ──────────────────────────────
def generate_motivation_quote(data):
    quotes = data.get("quotes", [
        "\"The secret of getting ahead is getting started.\" — Mark Twain",
        "\"Success is the sum of small efforts, repeated day in and day out.\" — Robert Collier",
        "\"Don't watch the clock; do what it does. Keep going.\" — Sam Levenson",
        "\"Believe you can and you're halfway there.\" — Theodore Roosevelt",
        "\"The expert in anything was once a beginner.\" — Helen Hayes",
    ])
    quote = random.choice(quotes)
    print("\n✨ Your Motivation Quote:")
    print("=" * 45)
    print(f"  {quote}")
    print("=" * 45)
    save_output(f"MOTIVATION QUOTE:\n{quote}")

# ── Feature 3: Current Date & Time ──────────────────────────
def display_datetime():
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %d %B %Y")
    time_str = now.strftime("%I:%M:%S %p")
    print("\n🕐 Current Date & Time:")
    print("=" * 45)
    print(f"  📅 Date : {date_str}")
    print(f"  ⏰ Time : {time_str}")
    print("=" * 45)
    save_output(f"DATE & TIME:\nDate: {date_str}\nTime: {time_str}")

# ── Main Program ─────────────────────────────────────────────
def main():
    data = load_json("tips.json")

    print("=" * 50)
    print("       🎓 Smart Student Assistant 🎓")
    print("    AIML Internship — Week 1 Assignment")
    print("=" * 50)

    name = input("  Enter your name: ").strip()
    if not name:
        name = "Student"

    print(f"\n  👋 Hello, {name}! Welcome to your Smart Assistant.")
    print("  I'm here to help you study and stay motivated!\n")
    save_output(f"SESSION STARTED for: {name}")

    while True:
        print("\n📋 Main Menu:")
        print("  1️⃣  Generate Study Tips")
        print("  2️⃣  Generate Motivation Quote")
        print("  3️⃣  Display Current Date & Time")
        print("  4️⃣  Exit")
        print("-" * 30)

        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            generate_study_tips(data)
        elif choice == "2":
            generate_motivation_quote(data)
        elif choice == "3":
            display_datetime()
        elif choice == "4":
            print(f"\n  👋 Goodbye, {name}! Keep learning and growing! 🚀")
            save_output("SESSION ENDED")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
