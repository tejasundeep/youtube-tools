import random

def generae_seo_title(keyword):
    title_template = [
        f"How to {keyword} for beginners",
        f"Master {keyword} for beginners",
        f"Maximize {keyword} for beginners",
    ]

    title = random.choice(title_template).format(keyword = keyword)
    return print(title)

generae_seo_title(input("Keyword please: "))