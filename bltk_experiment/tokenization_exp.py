from bltk.langtools import Tokenizer

if __name__ == '__main__':

    # Sample text
    text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
           "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
           "যায় সেটাই আমার জন্যে অনেক।"

    # Creating an instance
    tokenizer = Tokenizer()

    # Tokenizing Sentences
    print("TOKENIZED SENTENCES")
    sentences = tokenizer.sentence_tokenizer(text)
    print(sentences)

    # Splitting the sentences
    print("SPLIT SENTENCES")
    sentence_list = tokenizer.sentence_splitter(sentences)
    for i in sentence_list:
        print(i)

    # Tokenizing words
    print('TOKENIZED WORDS')
    words = tokenizer.word_tokenizer(text)
    print(words)