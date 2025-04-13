import sys
query = sys.argv[1] if len(sys.argv) > 1 else "factual summarization"
url = f"https://aclanthology.org/search/?q={query.replace(' ', '+')}"
