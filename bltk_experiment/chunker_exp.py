from bltk.langtools import Tokenizer
from bltk.langtools import Chunker


if __name__ == '__main__':

    grammar = r"""
      NP: {<DAB>?<JJ|JQ>*<N.>}      
      """
    text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
           "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
           "যায় সেটাই আমার জন্যে অনেক।"

    tokenizer = Tokenizer()
    sentences = tokenizer.sentence_tokenizer(text)
    tokened_text = [tokenizer.word_tokenizer(sentence) for sentence in sentences]

    noun_phrases = []
    for t in tokened_text:
        chunky = Chunker(grammar=grammar, tokened_text=t)
        chunk_tree = chunky.chunk()
        for i in chunk_tree.subtrees():
            if i.label() == "NP":
                print(i)
                noun_phrases.append(i)
