
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Python Programming Question Paper', 0, 1, 'C')
        self.cell(0, 10, 'Total Marks: 50', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# MCQs
mcqs = [
    {
        "question": "What is the output of print(2**3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 4"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["A) //", "B) /*", "C) #", "D) --"],
        "answer": "C"
    },
    {
        "question": "What does len([1,2,3]) return?",
        "options": ["A) 3", "B) 6", "C) 1", "D) Error"],
        "answer": "A"
    },
    {
        "question": "Which loop is used for iterating over a sequence?",
        "options": ["A) if", "B) for", "C) while", "D) switch"],
        "answer": "B"
    },
    {
        "question": "What is the keyword to define a function?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a Python data type?",
        "options": ["A) int", "B) str", "C) float", "D) char"],
        "answer": "D"
    },
    {
        "question": "How to access the first element of a list 'lst'?",
        "options": ["A) lst[0]", "B) lst[1]", "C) lst.first()", "D) lst.get(0)"],
        "answer": "A"
    },
    {
        "question": "What does 'OOP' stand for?",
        "options": ["A) Object Oriented Programming", "B) Open Object Protocol", "C) Online Operation Process", "D) Organized Object Pattern"],
        "answer": "A"
    },
    {
        "question": "Which method is used to add an element to a list?",
        "options": ["A) add()", "B) insert()", "C) append()", "D) push()"],
        "answer": "C"
    },
    {
        "question": "What is the output of bool('')?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Which statement is used for conditional execution?",
        "options": ["A) for", "B) if", "C) while", "D) def"],
        "answer": "B"
    },
    {
        "question": "How to open a file for reading?",
        "options": ["A) open('file.txt', 'w')", "B) open('file.txt', 'r')", "C) open('file.txt', 'a')", "D) open('file.txt', 'x')"],
        "answer": "B"
    },
    {
        "question": "What is the base class for all exceptions?",
        "options": ["A) Error", "B) Exception", "C) BaseError", "D) RuntimeError"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "B"
    },
    {
        "question": "How to create a class in Python?",
        "options": ["A) class MyClass:", "B) def MyClass():", "C) create MyClass:", "D) new MyClass:"],
        "answer": "A"
    },
    {
        "question": "What does 'self' refer to in a class method?",
        "options": ["A) The class itself", "B) The instance", "C) The method", "D) The module"],
        "answer": "B"
    },
    {
        "question": "Which function converts a string to lowercase?",
        "options": ["A) lower()", "B) casefold()", "C) lowercase()", "D) Both A and B"],
        "answer": "D"
    },
    {
        "question": "What is the output of print(type(5))?",
        "options": ["A) <class 'int'>", "B) <class 'str'>", "C) <class 'float'>", "D) <class 'bool'>"],
        "answer": "A"
    },
    {
        "question": "How to handle exceptions in Python?",
        "options": ["A) try-except", "B) if-else", "C) for-while", "D) def-return"],
        "answer": "A"
    }
]

# 5-mark questions
questions = [
    "Write a Python program to find the factorial of a number using a loop.",
    "Explain the difference between lists and tuples with examples.",
    "Define a class 'Student' with attributes name and age, and a method to display them.",
    "Write code to read a file 'data.txt' and print its contents.",
    "Demonstrate error handling for division by zero.",
    "Create a function that takes a list and returns the sum of its elements."
]

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Section 1: MCQs
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Section 1: Multiple Choice Questions (20 x 1 = 20 marks)', 0, 1)
pdf.ln(5)

for i, mcq in enumerate(mcqs, 1):
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Q{i}. {mcq["question"]}', 0, 1)
    pdf.set_font('Arial', '', 12)
    for option in mcq["options"]:
        pdf.cell(0, 8, option, 0, 1)
    pdf.ln(5)

# Section 2: Questions
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Section 2: Descriptive Questions (6 x 5 = 30 marks)', 0, 1)
pdf.ln(5)

for i, q in enumerate(questions, 1):
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Q{i+20}. {q}', 0, 1)
    pdf.ln(10)

# Answer Key
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Answer Key for MCQs', 0, 1)
pdf.ln(5)

for i, mcq in enumerate(mcqs, 1):
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 8, f'Q{i}: {mcq["answer"]}', 0, 1)

pdf.output('question_paper.pdf')
print("Question paper generated as 'question_paper.pdf'")
