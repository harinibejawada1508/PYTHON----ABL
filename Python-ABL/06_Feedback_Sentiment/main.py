positive_words = ["good", "great", "excellent", "helpful", "clear", "interesting", "love"]
negative_words = ["bad", "poor", "boring", "confusing", "difficult", "hate", "slow"]

feedback = input("Enter student feedback: ").lower()
score = 0

for word in positive_words:
    score += feedback.count(word)
for word in negative_words:
    score -= feedback.count(word)

print("Sentiment score:", score)
if score > 0:
    print("Overall sentiment: Positive")
elif score < 0:
    print("Overall sentiment: Negative")
else:
    print("Overall sentiment: Neutral")
