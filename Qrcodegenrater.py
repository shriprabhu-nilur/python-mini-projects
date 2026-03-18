# Importing the qrcode library to generate QR codes
import qrcode as qr


# Defineing a function to generate QR code
def generate_qr():
    
    # Takeing  text input from the user
    text = input("Enter the text or link to generate QR Code: ")
    
    # Createing a QRCode object with custom settings
    qrcode = qr.QRCode(
        version=None,  # Automatically adjust size based on data length
        error_correction=qr.constants.ERROR_CORRECT_H,  # High error correction level wiht if some mistake still work
        box_size=8,  # Size of each small square in QR code
        border=4,  # Thickness of white border around QR code
    )

    # Adding the user input data into the QR code
    qrcode.add_data(text)

    # Generateing the QR code structure
    qrcode.make(fit=True)

    # Converting QR code into an image with black color and white background
    img = qrcode.make_image(fill_color="red", back_color="lightblue")

    # Defineing the file name to save the QR code image
    file_name = "my_qrcode.jpg"

    # Saveing the generated QR code image as a JPG file
    img.save(file_name)

    # Printing success message 
    print(f"QR Code generated successfully and saved as {file_name}")


# Calling the function
generate_qr()