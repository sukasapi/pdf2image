import os
from pdf2image import convert_from_path

def convert_pdfs_to_images(input_folder, output_folder):
   
    # Pastikan bahwa path ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # melisting semua file pdf dalam folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
             #poppler path //pastikan sudah install ya
            poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin"
            # Convert PDF ke images
            images = convert_from_path(pdf_path,poppler_path= poppler_path)

            # simpan semua image, jika dalam satu file ada >1 halaman beri numbering pada file
            for i, image in enumerate(images):
                image_filename = f"{os.path.splitext(filename)[0]}_page_{i + 1}.png"
                image.save(os.path.join(output_folder, image_filename), 'PNG')
                print(f"Converted {filename}  to {os.path.basename(image_filename)}")
if __name__ == "__main__":
    input_folder = input("masukkan folder dimana anda menyimpan file pdf: ")
    output_folder = input("masukkan folder untuk menyimpan hasil konversi: ")
    convert_pdfs_to_images(input_folder, output_folder)
