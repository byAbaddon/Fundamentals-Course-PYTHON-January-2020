text = input()
get_file_index = text.rfind('\\')
file_name, extension = text[get_file_index + 1:].split('.')
print(f'File name: {file_name}\nFile extension: {extension}')
