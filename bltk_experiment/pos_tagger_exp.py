from bltk.langtools.pos_tagger import PosTagger
from bltk.langtools.tokenizer import Tokenizer

if __name__ == '__main__':

    pos_tagger = PosTagger()
    tokenizer = Tokenizer()

    text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
           "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
           "যায় সেটাই আমার জন্যে অনেক।"

    token_text = tokenizer.sentence_tokenizer(text)
    print(token_text)

    pos_tags = []
    for text in token_text:
        tokened = tokenizer.word_tokenizer(text)
        tagged = pos_tagger.pos_tag(tokened)
        pos_tags.append(tagged)
    print(pos_tags)