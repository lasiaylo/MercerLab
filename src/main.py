import folderparser as p
import tkinter as tk
from tkinter import filedialog

def main():
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askdirectory()
    read = 'C:/Users/lasia/Documents/workspace/MercerLab/MercerLabCollection/resources'
    write = 'C:/Users/lasia/Desktop/Output'
    products = '5'
    parser = p.FolderParser(read, write, products)
    parser.parse()


if __name__ == "__main__":
    main()