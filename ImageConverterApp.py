import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


root = tk.Tk()
root.wm_iconbitmap('E:\PythonProjects\ImageConvertApp\converter.ico')
root.title('Image Converter App')
root.minsize(width = 500, height = 300)
root.maxsize(width = 500, height = 300)


canvas1 = tk.Canvas(root, width = 500, height = 500, bg = '#ffe4b5', relief = 'raised')
canvas1.pack()


label1 = tk.Label(root, text = "Image Converter App", bg = '#ffe4b5')
label1.config(font = ('roboto', 20))
canvas1.create_window(250, 20, window = label1)


def getImage():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

    messagebox.showinfo("Information", "Image Is Imported")

browsImage = tk.Button(text = "Import Image", command = getImage, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(250, 60, window = browsImage)


#2 JPG


def ConvertJPG():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpg')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete JPG")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

JpgButton = tk.Button(text = "Convert to JPG", command = ConvertJPG, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(100, 100, window = JpgButton)


#3 JPEG


def ConvertJPEG():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpeg')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete JPEG")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

JpegButton = tk.Button(text = "Convert to JPEG", command = ConvertJPEG, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(250, 100, window = JpegButton)


#4 PNG

def ConvertPNG():
    global im1
    
    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.png')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete PNG")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")



PngButton = tk.Button(text = "Convert to PNG", command = ConvertPNG, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(420, 100, window = PngButton)


#4 TIF

def ConvertTIF():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.tif')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete TIF")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

TifButton = tk.Button(text = "Convert to TIF", command = ConvertTIF, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(100, 140, window = TifButton)


#5 TIFF


def ConvertTIFF():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.tiff')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete TIFF")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

TiffButton = tk.Button(text = "Convert to TIFF", command = ConvertTIFF, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(250, 140, window = TiffButton)

#6 GIF

def ConvertGIF():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.gif')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete GIF")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

GifButton = tk.Button(text = "Convert to GIF", command = ConvertGIF, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(420, 140, window = GifButton)



#7 BMP

def ConvertBMP():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.bmp')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete BMP")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

BmpButton = tk.Button(text = "Convert to BMP", command = ConvertBMP, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(100, 180, window = BmpButton)

#8 PDF
def ConvertPDF():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.pdf')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete PDF")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

PdfButton = tk.Button(text = "Convert to PDF", command = ConvertPDF, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(250, 180, window = PdfButton)


#9 EPS

def ConvertEPS():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.eps')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete EPS")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

EpsButton = tk.Button(text = "Convert to EPS", command = ConvertEPS, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(420, 180, window = EpsButton)



def ConvertWEBP():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.webp')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete Webp")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

WebpButton = tk.Button(text = "Convert to WEBP", command = ConvertWEBP, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(100, 220, window = WebpButton)


def ConvertICO():
    global im1

    try:
        print("Image Information")
        print("im1")

        export_file_path = filedialog.asksaveasfilename(defaultextension = '.ico')
        im1.save(export_file_path)

        messagebox.showinfo("Information", "Complete ICO")

    except NameError:
        messagebox.showwarning("Warning","Import Image First")

IcoButton = tk.Button(text = "Convert to ICO", command = ConvertICO, bg = '#C0C0C0', fg = 'black', font = ('helvetica', 12, 'bold'),
                       border = 2,
                       relief= "raised",
                       activebackground = 'green')

canvas1.create_window(250, 220, window = IcoButton)



root.mainloop()
