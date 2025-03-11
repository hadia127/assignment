Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> marks = int(input("Enter student marks (1-100): "))
... if marks < 50:
...     grade = "F"
... elif marks <= 60:
...     grade = "E"
... elif marks <= 70:
...     grade = "D"
... elif marks <= 80:
...     grade = "C"
... elif marks <= 90:
...     grade = "B"
... else:
...     grade = "A"
