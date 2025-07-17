import cohere
import os

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def predict_event_category(EventName,Location, description):
    prompt = f"""
You are an event classification AI. Given the title, venue, and description of an event, classify it into one of these categories:
- Workshop
- Seminar
- Conference
- Cultural
- Sports
- Tech Talk
- Networking
- Celebration

Title: {EventName}
Venue: {Location}
Description: {description}

Category:
"""

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=10,
            temperature=0.3,
            stop_sequences=["\n"]
        )
        category = response.generations[0].text.strip()
        return category

    except Exception as e:
        print(f"Error during category prediction: {e}")
        return "Uncategorized"
