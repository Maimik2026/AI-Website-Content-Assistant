
def review_website_content(text):
    """Review website text and suggest improvements."""

    if not text.strip():
        return "Please enter some website text to review."

    suggestions = []

    if len(text.split()) < 20:
        suggestions.append(
            "The text is short. Consider adding more useful details."
        )

    if not any(char in text for char in ".!?"):
        suggestions.append(
            "Add clear sentences with appropriate punctuation."
        )

    if not any(word in text.lower() for word in [
        "what", "how", "why", "how to"
    ]):
        suggestions.append(
            "Consider adding questions and answers (FAQ)."
        )

    if not suggestions:
        suggestions.append(
            "Review headings, clarity, factual accuracy and useful details."
        )

    return "\n".join("- " + item for item in suggestions)


if __name__ == "__main__":
    print("AI Website Content Assistant")
    print("Enter website text in English.")
    website_text = input("\nWebsite text: ")

    print("\nSuggestions:")
    print(review_website_content(website_text))
