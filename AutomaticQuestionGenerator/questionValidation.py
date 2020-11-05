# Question Validation


def hNvalidation(sentence):
    """
    Determine whether the given sentence is valid.

    Args:
        sentence: (todo): write your description
    """
    flag = 1

    Length = len(sentence)
    if (Length > 4):
        for i in range(Length):
            if (i+4 < Length):
                if (sentence[i]==' ' and sentence[i+1]=='h' and sentence[i+2]==' ' and sentence[i+3]=='N' and sentence[i+4]==' '):
                    flag = 0


    return flag

