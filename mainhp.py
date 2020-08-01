# -*- coding: utf-8 -*-
"""
Simple word counter from a book.
"""
from collections import Counter
import pandas as pd


def read_file(path):
    with open(path, 'r') as f:
        full_text = f.read()
    return full_text


def clean_text(text):
    for i in range(226):
        text = text.replace("Page {} of 226".format(i), "")
    for character in "?!,.;…“”’:-—":
        text = text.replace(character, " ")    
    return text


def create_words_counter(text):
    words = text.split()
    low_words = [word.lower() for word in words]
    return Counter(low_words)


def prepare_dictionary_for_data_frame(item_list):
    items = list(item_list)
    words = []
    count = []
    for item in items:
        words.append(item[0])
        count.append(item[1])
    return words, count


if __name__ == "__main__":
    PATH = "hpv2_text.txt"
    hp_content = read_file(PATH)
    cleaned_hp_content = clean_text(hp_content)
    counter = create_words_counter(cleaned_hp_content)
    
    words, count = prepare_dictionary_for_data_frame(counter.items())
    data = pd.DataFrame({'words': words, 'counter': count})
    data = data.sort_values(by=['counter'], ascending=False)
    data['length'] = data['words'].apply(len)
    
    print(data[data['length']>3][:50])