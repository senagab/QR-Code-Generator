# QR Code Generator

This simple Python script utilizes the `qrcode` library to generate QR codes from given input data, which can be a URL, text, or any information you want to encode into a QR code.

## How it Works

The script follows a straightforward process:

1. **Define Data**: Set the `qrcode_data` variable to the desired URL, text, or any information you want to encode.

2. **Create QR Code Object**: Initialize a QR code object (`qr`) using the `qrcode.QRCode` class, specifying parameters such as version, error correction, box size, and border.

3. **Input Data**: Add the data to be encoded to the QR code using the `qr.add_data` method.

4. **Generate QR Code**: Use the `qr.make(fit=True)` method to generate the QR code.

5. **Render Image**: Render the QR code image with specified fill and background colors using `qr.make_image(fill_color="white", back_color="#252525")`.

6. **Export Image**: Save the generated QR code image to a file, in this case, "bascuare-invert.png".

## Configuration Parameters

| Parameter             | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `version`             | Size of the QR code (larger values accommodate more data).     |
| `error_correction`    | Level of error correction (use `qrcode.constants.ERROR_CORRECT_*`).|
| `box_size`            | Size of each box (pixel) in the QR code.                       |
| `border`              | Width of the border around the QR code.                        |

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required library:

    ```bash
    pip install qrcode[pil]
    ```

3. Run the script:

    ```bash
    python generate_qrcode.py
    ```

4. Find the generated QR code in the project directory as "filename.png".

## Example

You can customize the `qrcode_data` variable with your own data to generate QR codes for different purposes.

Feel free to explore and modify the script according to your needs. If you encounter any issues or have suggestions, please open an issue on the GitHub repository.

Happy coding!
