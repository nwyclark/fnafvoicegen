import os
import re
from pydub import AudioSegment

LETTERS = {}
LET_PATH = "./lets"
OUT_PATH = "./out"

def letter_segment(letter: str) -> AudioSegment:
    if letter in LETTERS:
        return LETTERS[letter]
    
    LETTERS[letter] = AudioSegment.from_file(os.path.join(LET_PATH, f"{letter}.wav"), format="wav")
    return LETTERS[letter]


def combine(message: str) -> AudioSegment:
    letters = list(message)
    combined = AudioSegment(
        data=b'',
        sample_width=2,
        frame_rate=44_100,
        channels=2
    )
    for letter in letters:
        combined += letter_segment(letter)

    return combined

def export(sentence: str, file: AudioSegment):
    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)

    file.export(os.path.join(OUT_PATH, f'{sentence}.wav'))

def main():
    sentence = re.sub("[^A-z]", "", input("enter sentence: ")).upper()
    export(sentence, combine(sentence))

if __name__ == '__main__':
    main()
