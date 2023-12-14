from PIL import Image, ImageEnhance

#TODO 1: Buka gambar dengan pillow
Image = Image.open('../../../OneDrive/Documents/UNIVERSITY FILES/Sem 5/ch.jpeg')

#TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(Image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

#TODO 3: Simpan gambar hasil edit
save_path = r'C:\Users\VIVOBOOK\OneDrive\Documents\UNIVERSITY FILES\Sem 5\Prak. Prog. Fungsional ' \
            r'H\brightness_contrast_image.jpg'
brightened_image.save(save_path)

#TODO 4: Tampilkan
brightened_image.show()