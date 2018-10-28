import nltk


def nerTagger(tokenize):
    tagged_sentences = nltk.pos_tag(tokenize)
    ne_chunked_sents = nltk.ne_chunk(tagged_sentences)

    named_entities = []
    for tagged_tree in ne_chunked_sents:
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
            entity_type = tagged_tree.label()
            named_entities.append((entity_name, entity_type))
    return named_entities