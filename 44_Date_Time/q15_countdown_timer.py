# Question: Create a countdown timer — ask the user for a future date,
# compute how many days remain until that date, and show a friendly message.

# Example output:
# === Countdown Timer ===
# Enter the future event date:
# Year: 2025
# Month: 1
# Day: 1
# 
# Event: 2025-01-01 (Wednesday, January 01, 2025)
# Today: 2024-01-15
# 
# ⏳ Countdown: 351 days remaining!
# That's about 50 weeks and 1 days.
# 
# Or: 11 months and 17 days.

import datetime

print("=" * 35)
print("      Countdown Timer")
print("=" * 35)
print("Enter the future event date:\n")

try:
    year = int(input("Year: "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))

    event_date = datetime.date(year, month, day)
    today = datetime.date.today()

    if event_date < today:
        days_past = (today - event_date).days
        print(f"\nThat date has already passed ({days_past} days ago)!")
    elif event_date == today:
        print("\nThat's TODAY! Happy event day!")
    else:
        days_remaining = (event_date - today).days

        print(f"\nEvent: {event_date} ({event_date.strftime('%A, %B %d, %Y')})")
        print(f"Today: {today}")
        print(f"\n⏳ Countdown: {days_remaining} days remaining!")
        print(f"That's about {days_remaining // 7} weeks and {days_remaining % 7} days.")

        # Approximate months
        months_remaining = days_remaining // 30
        leftover_days = days_remaining % 30
        print(f"Or approximately: {months_remaining} months and {leftover_days} days.")

        # Progress as percentage of year
        print(f"\nHours remaining: {days_remaining * 24:,}")
        print(f"Minutes remaining: {days_remaining * 24 * 60:,}")

except ValueError as e:
    print(f"Invalid date: {e}")
