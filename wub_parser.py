def parse(doc: str):
    """actually a tokenizer

        takes a string and splits it into an array of tokens
    """

    # this code is very complicated
    # try not to be overwhelmed

    dirty_tokens = doc.replace('\n', ' ').split(' ')
    clean_tokens = filter(lambda token: len(token) > 0, dirty_tokens)

    tokens = []

    for token in clean_tokens:
        tokens.append(token)

    return tokens