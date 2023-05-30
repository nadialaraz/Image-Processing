import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 
import cv2
import numpy as np
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Image Convolution")
        
        self.frame2 = tk.Frame(self) 
        self.frame2.pack(side="left")
        
        self.frame1 = tk.Frame(self)
        self.frame1.pack(side="left") 
        self.frame1.config(bg="white")

        self.frame3 = tk.Frame(self) 
        self.frame3.pack(side="left")

        self.load_button = tk.Button(self.frame1, text="Start", command=self.load_image, width=20)
        self.sharpen_button = tk.Button(self.frame1, text="Sharpen", command=lambda: self.apply_filter("sharpen"), width=20)            
        self.blur_button = tk.Button(self.frame1, text="Blur", command=lambda: self.apply_filter("blur"), width=20)
        self.sobel_button = tk.Button(self.frame1, text="Sobel", command=lambda: self.apply_filter("sobel"), width=20)
        self.save_button = tk.Button(self.frame1, text="Save Image",command=self.save_image, width=20)

        self.load_button.pack(side="top", padx=10, pady=10, anchor="center") 
        self.sharpen_button.pack(side="top", padx=10, pady=10, anchor="center") 
        self.blur_button.pack(side="top", padx=10, pady=10, anchor="center")
        self.sobel_button.pack(side="top", padx=10, pady=10, anchor="center") 
        self.save_button.pack(side="top", padx=10, pady=10, anchor="center")

        self.canvas1 = tk.Canvas(self.frame2, width=400, height=400) 
        self.canvas1.pack(side="left")

        self.canvas3 = tk.Canvas(self.frame3, width=400, height=400) 
        self.canvas3.pack(side="right")

#         self.original_image = None 
#         self.processed_image = None

#     def load_image(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image Files","*.jpg;*.jpeg;*.png")]) 
#         if not file_path:
#             return
#         self.original_image = cv2.imread(file_path, 0) 
#         self.original_image1 = cv2.imread(file_path) 

#         aspect_ratio = float(self.original_image.shape[1]) / float(self.original_image.shape[0])

#         if self.original_image.shape[0] > self.original_image.shape[1]:
#             new_height = 400
#             new_width = int(new_height * aspect_ratio) 
#         else:
#             new_width = 400
#             new_height = int(new_width / aspect_ratio)

#         self.original_image = cv2.resize(self.original_image, (new_width, new_height))
#         self.display_image(self.original_image, self.canvas1)
#         self.display_image(self.original_image, self.canvas3)

#         aspect_ratio = float(self.original_image1.shape[1]) / float(self.original_image1.shape[0])

#         if self.original_image1.shape[0] > self.original_image1.shape[1]:
#            new_height = 400
#            new_width = int(new_height * aspect_ratio) 
#         else:
#            new_width = 400
#            new_height = int(new_width / aspect_ratio)

#         self.original_image1 = cv2.resize(self.original_image1, (new_width, new_height))

#     def save_image(self):
#         if self.processed_image is None:
#             messagebox.showerror("Error", "No image to save")
#             return 
#         file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
#         if not file_path:
#             return
#         cv2.imwrite(file_path, self.processed_image) 
#         messagebox.showinfo("Success", "Image saved successfully")


#     def apply_filter(self, filter_name): 
#         if self.original_image is None:
#             messagebox.showerror("Error", "No image loaded")
#             return
#         if filter_name == "sharpen":
#             self.processed_image = self.original_image.copy() 
#             sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]]) 
#             self.processed_image = cv2.filter2D(self.processed_image, -1, sharpen_kernel)
#         elif filter_name == "blur":
#             kernel = np.ones((15,15),np.float32)/225
#             self.processed_image = cv2.filter2D(self.original_image,-1,kernel)
#         elif filter_name == "sobel":
#             self.processed_image = cv2.cvtColor(self.original_image1, cv2.COLOR_BGR2GRAY)
#             self.processed_image = cv2.Sobel(self.processed_image, cv2.CV_64F,1, 0, ksize=3)
#             self.processed_image = cv2.convertScaleAbs(self.processed_image)

#         self.display_image(self.processed_image, self.canvas3)

#     def display_image(self, image, canvas):
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = Image.fromarray(image)
#         image = ImageTk.PhotoImage(image) 
#         canvas.delete("all") 
#         canvas.create_image(200, 200, image=image) 
#         canvas.image = image
        
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

        self.original_image = None 
        self.original_image1 = None 
        self.processed_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files","*.jpg;*.jpeg;*.png")]) 
        if not file_path:
            return
        self.original_image = cv2.imread(file_path) 
        

        aspect_ratio = float(self.original_image.shape[1]) / float(self.original_image.shape[0])

        if self.original_image.shape[0] > self.original_image.shape[1]:
            new_height = 400
            new_width = int(new_height * aspect_ratio) 
        else:
            new_width = 400
            new_height = int(new_width / aspect_ratio)

        self.original_image = cv2.resize(self.original_image, (new_width, new_height))
        self.original_image1 = cv2.resize(self.original_image, (new_width, new_height))
        self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        self.display_image(self.original_image, self.canvas3)
        self.display_image(self.original_image1, self.canvas1)

    def save_image(self):
        if self.processed_image is None:
            messagebox.showerror("Error", "No image to save")
            return 
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if not file_path:
            return
        cv2.imwrite(file_path, self.processed_image) 
        messagebox.showinfo("Success", "Image saved successfully")


    def apply_filter(self, filter_name): 
        if self.original_image is None:
            messagebox.showerror("Error", "No image loaded")
            return
        if filter_name == "sharpen":
            self.processed_image = self.original_image.copy() 
            sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]]) 
            self.processed_image = cv2.filter2D(self.processed_image, -1, sharpen_kernel)
        elif filter_name == "blur":
            kernel = np.ones((15,15),np.float32)/225
            self.processed_image = cv2.filter2D(self.original_image,-1,kernel)
        elif filter_name == "sobel":
            self.processed_image = cv2.cvtColor(self.original_image1, cv2.COLOR_BGR2GRAY)
            self.processed_image = cv2.Sobel(self.processed_image, cv2.CV_64F,1, 0, ksize=3)
            self.processed_image = cv2.convertScaleAbs(self.processed_image)

        self.display_image(self.processed_image, self.canvas3)

    def display_image(self, image, canvas):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image) 
        canvas.delete("all") 
        canvas.create_image(200, 200, image=image) 
        canvas.image = image
        
if __name__ == "__main__":
    app = App()
    app.mainloop()