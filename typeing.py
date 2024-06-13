
class Wpm:
    def calculate_wpm(text, time_taken):
        words = text.split()
        num_words = len(words)
        minutes = time_taken / 60
        wpm = num_words / minutes if minutes > 0 else 0
        return round(wpm)