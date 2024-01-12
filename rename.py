import os

if __name__ == '__main__':

    dire = input("Input directory:")
    files = os.listdir(dire)
    count = 0
    for file in files:
        if file.endswith('.jpg'):
            count += 1
            old_file = os.path.join(dire, file)
            new_name = f'{count}.jpg'
            new_file = os.path.join(dire, new_name)
            os.rename(old_file, new_file)
