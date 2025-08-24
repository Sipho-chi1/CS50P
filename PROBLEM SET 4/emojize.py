import emoji
def emoji_text():
        emoji_txt=input('Input:').lower()
        print(emoji.emojize(emoji_txt, language='alias'))
emoji_text()