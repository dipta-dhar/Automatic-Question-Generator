## Automatic Question Generator
Automatic Question Generator from Text


Prerequisites
-------------
```
- Python 3.5+
- NLTK 
- SpaCy
- NumPy
```

### Quickstart (main.py)

#### run user input:
```python
inputText = '''My best friend and I have been studying in the same 
               school since kindergarten.'''
```

#### run from user text file:
```python
inputText = filePATH

# Like:
# inputText = "E:/EDU/project/input.txt"
```


### Example

#### input:
```
My best friend and I have been studying in the same school since kindergarten. We have been classmates each year at 
school. We share a very close bond and have a special friendship that we cherish and treasure. My friend is my 
partner, sitting beside me in class. She is kindly and helpful, and if I have any difficulties in understanding any 
topic in my studies, or in completing my homework or school project, she helps me. She is brilliant in mathematics 
and the sciences, while I am good at English. So we both help each other in whatever way possible. She helps me 
without ever belittling me. I greatly appreciate the quality in her. She does not make me feel obliged.
```

#### output:
```
Q-01: Have you been classmates each year?
Q-02: Have you been at school?
Q-03: Who have been classmates each year at school?
Q-04: Who cherish and treasure?
Q-05: Who helps me?
Q-06: Who is good at English?
Q-07: Who helps me without ever belittling me?
Q-08: Who ever belittling me?
Q-09: Who greatly appreciate the quality in her?
Q-10: Whom she does not make feel obliged?
```
 
## SETTINGS OF MAIN FUNCTION:

### main.py
```python
    # Main Function
    def main():
        # Create AQG object
        aqg = aqgFunction.AutomaticQuestionGenerator()

        # Enter input Text File PATH
        inputTextPath = "PATH: (Like:- E:/in.txt)"
        readFile = open(inputTextPath, 'r+')
        inputText = readFile.read()

        questionList = aqg.aqgParse(inputText)
        aqg.display(questionList)

        return 0


    # Call Main Function
    if __name__ == "__main__":
        main()
 
```


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
=============================================================================================
