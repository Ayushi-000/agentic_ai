def summarize_text(text):
    """Simple function to return a summarized version of the text."""
    if not text:
        return "No content to summarize."
    return " ".join(text.split()[:10]) + "..."
