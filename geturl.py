import os
import pyperclip

pre_url = 'Learning/Python/'

# Lấy tất cả các tệp trong thư mục hiện tại và thay thế dấu cách bằng dấu _
files = [pre_url + f.replace(" ", "_") for f in os.listdir() if os.path.isfile(f)]

# Ghép các tên tệp thành một chuỗi, mỗi tên tệp cách nhau một dòng
file_names = "\n".join(files)

# Sao chép danh sách tên tệp vào clipboard
pyperclip.copy(file_names)

print("Đã sao chép tên các tệp vào clipboard:")
print(file_names)