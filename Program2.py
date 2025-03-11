Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temperature = float(input("Enter temperature in centigrade: "))
Enter temperature in centigrade: -5
>>> f temperature < 0:
...     message = "FREEZING"
... elif temperature <= 15:
...     message = "COLD"
... elif temperature <= 30:
...     message = "WARM"
... elif temperature <= 40:
...     message = "HOT"
... else:
...     message = "VERY HOT"
