"""
@author: kprav33n (Praveen Kumar)

Ref : https://gist.github.com/kprav33n/ea2b5be9b63d9886df5b3ee3ed2eabbc 
"""
#!/usr/bin/env python3

import functools
import string
import sys

import grapheme  # pip install grapheme

from collections import defaultdict


"""
This dictionary maintains the rank of each character in Tamil.
Ranks range from 1 (easiest) to 15 (hardest).
"""
character_ranks: dict[str, int] = {
    "அ": 1,
    "ஆ": 1,
    "இ": 1,
    "ஈ": 1,
    "உ": 1,
    "ஊ": 1,
    "எ": 1,
    "ஏ": 1,
    "ஐ": 1,
    "ஒ": 1,
    "ஓ": 1,
    "ஔ": 1,
    "்": 2,
    "க": 3,
    "ங": 3,
    "ச": 3,
    "ஞ": 3,
    "ட": 3,
    "ண": 3,
    "த": 3,
    "ந": 3,
    "ப": 3,
    "ம": 3,
    "ய": 3,
    "ர": 3,
    "ல": 3,
    "வ": 3,
    "ழ": 3,
    "ள": 3,
    "ற": 3,
    "ன": 3,
    "ா": 4,
    "ி": 5,
    "ீ": 6,
    "ு": 7,
    "ூ": 8,
    "ெ": 9,
    "ே": 10,
    "ை": 11,
    "ொ": 12,
    "ோ": 13,
    "ௌ": 14,
    "ஶ": 15,
    "ஜ": 15,
    "ஷ": 15,
    "ஸ": 15,
    "ஹ": 15,
    "க்ஷ": 15,
}


"""
The list of labels for each rank.
"""
rank_labels = [
    "அ",
    "க்",
    "க",
    "கா",
    "கி",
    "கீ",
    "கு",
    "கூ",
    "கெ",
    "கே",
    "கை",
    "கொ",
    "கோ",
    "கௌ",
    "ஜ",
]


def character_rank(ch: str) -> int:
    """
    Returns the rank of the given Tamil character.
    """
    if len(ch) == 1:
        return character_ranks.get(ch[0], sys.maxsize)
    elif len(ch) == 2:
        r1, r2 = character_rank(ch[0]), character_rank(ch[1])
        if r2 == 2 and r1 != 15:
            return r2
        return max(r1, r2)
    else:
        return sys.maxsize


def word_rank(word: str) -> int:
    """
    Returns the rank of the given Tamil word.
    """
    return functools.reduce(
        lambda rank, ch: max(rank, character_rank(ch)), grapheme.graphemes(word), 0
    )


def print_distribution(sentence: str):
    """
    Prints the distribution of Tamil words based on their ranks.
    """
    distribution = defaultdict(set)
    punctuation = set(string.punctuation)
    for word in sentence.split():
        word = "".join(filter(lambda ch: ch not in punctuation, word.strip()))
        if word:
            distribution[word_rank(word)].add(word)
    for rank, label in enumerate(rank_labels):
        words = ", ".join(distribution[rank + 1])
        print(f"{label}:\t{words}")


if __name__ == "__main__":
    poem = """தமிழுக்கும் அமுதென்று பேர்! - அந்தத்
தமிழ் இன்பத் தமிழ் எங்கள் உயிருக்கு நேர்
தமிழுக்கு நிலவென்று பேர்! - இன்பத்
தமிழ் எங்கள் சமூகத்தின் விளைவுக்கு நீர்!

தமிழுக்கு மணமென்று பேர்! - இன்பத்
தமிழ் எங்கள் வாழ்வுக்கு நிருமித்த ஊர்
தமிழுக்கு மதுவென்று பேர்! - இன்பத்
தமிழ் எங்கள் உரிமைச்செம் பயிருக்கு வேர்!

தமிழ் எங்கள் இளமைக்குப் பால்! - இன்பத்
தமிழ் நல்ல புகழ்மிக்க புலவர்க்கு வேல்!
தமிழ் எங்கள் உயர்வுக்கு வான்! - இன்பத்
தமிழ் எங்கள் அசதிக்குச் சுடர்தந்த தேன்!

தமிழ் எங்கள் அறிவுக்குத் தோள்! - இன்பத்
தமிழ் எங்கள் கவிதைக்கு வயிரத்தின் வாள்!
தமிழ் எங்கள் பிறவிக்குத் தாய்! - இன்பத்
தமிழ் எங்கள் வலமிக்க உளமுற்ற தீ!"""
    print_distribution(poem)
