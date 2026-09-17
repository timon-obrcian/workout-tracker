import time

def start_timer(seconds=180):
    print("\n" + "=" * 35)
    print("          3-MINUTEN-TIMER")
    print("=" * 35)
    print("Starte deine Pause. 💪")

    for remaining in range(seconds, 0, -1):
        minutes = remaining // 60
        seconds_left = remaining % 60

        print(
            f"\r⏱️ Noch {minutes:02d}:{seconds_left:02d}",
            end="",
            flush=True
        )

        time.sleep(1)

    print("\r✅ Pause vorbei! Weiter geht's!       ")
