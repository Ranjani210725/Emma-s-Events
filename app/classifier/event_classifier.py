import cohere
import os

# You can set your API key as an environment variable or paste it directly here
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# Alternatively, hardcode (NOT RECOMMENDED for production):
# COHERE_API_KEY = "your-api-key"

co = cohere.Client(COHERE_API_KEY)

def classify_event(EventName,Location, description):
    prompt = f"""
Classify the following event into one of the categories: Technical, Cultural, Sports, Wellness, Academic.

Event Title: {EventName}
Venue: {Location}
Description: {description}

Category:"""

    try:
        response = co.generate(
            model="command-r",
            prompt=prompt,
            max_tokens=10,
            temperature=0.3,
        )
        result = response.generations[0].text.strip()
        return result

    except Exception as e:
        print("Error with Cohere classification:", e)
        return "Uncategorized"

