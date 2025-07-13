import os
import subprocess

# Lặp qua tất cả các tệp .ipynb trong thư mục hiện tại
for file in os.listdir("."):
    if file.endswith(".ipynb"):
        print(f"Converting {file}...")
        subprocess.run(["jupyter", "nbconvert", "--to", "markdown", file])
print("Hoàn tất chuyển đổi!")
