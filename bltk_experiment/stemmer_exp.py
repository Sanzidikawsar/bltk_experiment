from bltk.langtools import UgraStemmer
from bltk.langtools import Tokenizer

if __name__ == '__main__':

    text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
           "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
           "যায় সেটাই আমার জন্যে অনেক।"

    stemmer = UgraStemmer()
    tokenizer = Tokenizer()
    tokenized_text = tokenizer.word_tokenizer(text)

    stem = stemmer.stem(tokenized_text)

    print(f"Before stemming: {tokenized_text}")
    print(f'After stemming: {stem}')