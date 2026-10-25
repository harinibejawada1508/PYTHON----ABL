# Documentation: Student Feedback Sentiment Scoring

## 1. Problem Statement
Estimate whether a short feedback sentence is positive, negative, or neutral by counting words from simple positive and negative word lists.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
A feedback sentence.

## 4. Output
Positive word count, negative word count, score, and sentiment label.

## 5. Algorithm
1. Store small lists of positive and negative keywords.
2. Read feedback and convert it to lowercase.
3. Split the sentence into words and strip common punctuation from each word.
4. Count matches in each keyword list.
5. Calculate score = positive count - negative count.
6. Label positive, negative, or neutral according to the score.

## 6. Sample Execution / Example
```text
Input: The class is good and helpful
Output: positive words 2, negative words 0, score 2, Positive.
```

## 7. Python Concepts Used
strings, lists, split, lower, loops, generator expressions, sum, conditionals.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
