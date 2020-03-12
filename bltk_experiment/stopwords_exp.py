from bltk.langtools import remove_stopwords
from bltk.langtools import Tokenizer

if __name__ == '__main__':
        
    tokenizer = Tokenizer()

    text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
           "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
           "যায় সেটাই আমার জন্যে অনেক।"

    tokened_words = tokenizer.word_tokenizer(text)

    print(f"Len of words: {len(tokened_words)}")
    print(f"After soft elimination: {(remove_stopwords(tokened_words))}")
    print(f"Length after soft elimination: {len(remove_stopwords(tokened_words))}")
    print(f"After moderate elimination: {(remove_stopwords(tokened_words, level='moderate'))}")
    print(f"Length after moderate elimination: {len(remove_stopwords(tokened_words, level='moderate'))}")
    print(f"After hard elimination: {(remove_stopwords(tokened_words, level='hard'))}")
    print(f"Length after hard elimination: {len(remove_stopwords(tokened_words, level='hard'))}")