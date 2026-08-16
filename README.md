🛠️ toolsan

A toolkit for those who want to write clean, powerful, and beautiful Python code.

toolsan is a versatile library designed for everyday developer tasks. It combines everything you need — from simple math operations to AI conversations and beautiful console output.

The library is easy to use yet flexible enough for serious projects. It was created with the belief that programming should bring joy.

---

📦 Installation

Install the library via pip:

pip install toolsan

Note: Requires Python 3.7 or higher.

---

🚀 Quick Start

import toolsan as ts

# Colored output
ts.superprint("Hello, world!", color=ts.green, style=ts.bold)

# Simple math
print(ts.armean(1, 2, 3, 4, 5))   # 3.0

# Date formatting
print(ts.date("Today: Day.Month.Year"))

# Password generation
print(ts.rand_password(16))

# Progress bar
for i in range(101):
    ts.progress_bar(i, 100, prefix="Loading:", suffix="Done")

---

📚 Core Features

🧮 Mathematics

· calc(prompt, tp) — evaluate expressions (supports sin, cos, sqrt, ln, log, factorial)
· armean(*numbers) — arithmetic mean
· median(*numbers) — median
· clamp(value, min_val, max_val) — clamp a value between bounds
· lerp(a, b, t) — linear interpolation
· distance(x1, y1, x2, y2) — Euclidean distance
· linspace(start, stop, num) — evenly spaced array
· arange(start, stop, step) — range with step
· dot(a, b) — dot product of vectors
· norm(a) — vector norm
· cosine_similarity(a, b) — cosine similarity
· quantile(data, q) — quantile calculation
· iqr(data) — interquartile range
· transpose(matrix) — matrix transpose
· matmul(A, B) — matrix multiplication

🖥️ Console & Output

· superprint(word, delay, side, color, bg_color, style) — animated printing with colors and alignment
· loadspin(seconds, speed, color) — animated spinner
· smart_input(prompt, typ, delay, color) — input with animated prompt
· bgcolor(color) — fill screen with color
· countdown(seconds, color, bgcolor, style) — countdown timer
· animate(list, seconds, speed, color) — frame animation
· marquee(text, delay, width, repeat, color, style, bg_color) — scrolling marquee
· progress_bar(iteration, total, prefix, suffix, length, fill, empty, color) — progress bar

🎨 Colors & Styles

Available colors:

· black, red, green, yellow, blue, purple, cyan, white
· b_black, b_red, b_green, ... — bright variants
· bg_black, bg_red, ... — background colors

Styles:

· bold, italic, underline, strike

🗄️ Data Storage (JSON Database)

import toolsan as ts

# Connect to database file
conn = ts.connect("data.json")

# Add data
ts.content(conn, "user", "Alice")

# Save changes
ts.save(conn, "data.json")

🧩 Decorators

· @head(obj) — wraps function output with a header
· @new_text(sep) — adds a separator line
· @benchmark — measures function execution time

🤖 Artificial Intelligence

import toolsan as ts

# Chat with AI (OpenRouter)
reply = ts.answer("Hi! How are you?")
print(reply)

🧠 Utilities

· random_obj(list) — random element from a list
· levenshtein(a, b) — Levenshtein distance
· sim(word1, word2, threshold) — similarity check
· flatten(*lists) — flatten multiple lists
· rand_password(length) — generate random password
· date(text) — insert current date/time into text
· numeral(number, lang) — number to words in any language
· incline(word, case) — word inflection (Russian language)
· statlib(lib) — PyPI download statistics

---

📖 Examples

Colored output with animation

ts.superprint("🔥 Hello!", delay=0.1, color=ts.red, style=ts.bold)

Animated spinner for 3 seconds

ts.loadspin(3, speed=10, color=ts.cyan)

Progress bar

for i in range(101):
    ts.progress_bar(i, 100, prefix="Processing:", suffix="Complete")
    time.sleep(0.05)

Scrolling marquee

ts.marquee("🚀 toolsan — your coding assistant!", delay=0.08, width=30, repeat=2)

---

🧪 Testing

To run tests:

pytest tests/

---

🤝 Contributing

Want to improve toolsan? Follow these steps:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to your fork (git push origin feature/amazing-feature)
5. Open a Pull Request

Contributions are always welcome!

---

📄 License

Distributed under the MIT License. See LICENSE for more information.

---

👨‍💻 Author

VLAD — gkkasatik7719@gmail.com

---

🌟 Acknowledgments

This library was created in the summer of 2026 with love for Python and a desire to make development more enjoyable. Thanks to everyone who uses and supports toolsan