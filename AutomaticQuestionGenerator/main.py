import aqgFunction


# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    inputTextPath = "E:/EDU/Study/FinalProject/NLPio/in.txt"
    readFile = open(inputTextPath, 'r+')
    inputText = readFile.read()

    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)

    return 0


# Call Main Function
if __name__ == "__main__":
    main()


