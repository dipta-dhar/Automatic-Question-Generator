import spacy


def nerTagger(nlp, tokenize):
    """
    Nerner tokenizer.

    Args:
        nlp: (todo): write your description
        tokenize: (int): write your description
    """
    doc = nlp(tokenize)

    finalList = []
    array = [[]]
    for word in doc:
        array[0] = 0
        for ner in doc.ents:
            if (ner.text == word.text):
                finalList.append((word.text, ner.label_))
                array[0] = 1
        if (array[0] == 0):
            finalList.append((word.text, 'O'))

    return finalList

