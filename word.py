import requests

# URL of 20,000 common English words sorted by frequency (from Google corpus)
url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

# Fetch the word list
response = requests.get(url)

if response.status_code == 200:
    all_words = response.text.splitlines()

    # Filter: only words with length >= 3 and alphabetic
    filtered_words = [word for word in all_words if word.isalpha() and len(word) >= 3]

    # Optional: limit to top 5000 if needed
    top_words = filtered_words[:5000]

    # Save to file
    with open("daily_conversation_words.txt", "w") as file:
        for word in top_words:
            file.write(word + "\n")

    print(f"✅ Saved {len(top_words)} words to 'daily_conversation_words.txt'")
else:
    print("❌ Failed to download the word list. Status code:", response.status_code)
