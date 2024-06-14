# flake8: noqa
import fitz  # PyMuPDF
import sys
import argparse


def create_empty_pdf(filename):
    doc = fitz.open()  # Create a new empty PDF
    doc.new_page()  # Add a blank page
    doc.save(filename)
    doc.close()


def hide_message(input_pdf, output_pdf, hidden_message):
    try:
        # Open the input PDF
        doc = fitz.open(input_pdf)

        # Choose the page to insert the hidden message
        page = doc[0]

        # Define the text insertion properties at the top of the page
        rect = fitz.Rect(50, 0, 550, 50)  # Coordinates for text at the top
        text = hidden_message
        font_size = 0
        color = (1, 1, 1)  # White color for invisibility

        # Insert the hidden plaintext message
        page.insert_textbox(rect, text, fontsize=font_size, color=color)

        # Save the output PDF
        doc.save(output_pdf)
        print(f'Hidden plaintext message encoded in {output_pdf}')
    except Exception as e:
        print(f'An error occurred: {e}', file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Encode a hidden plaintext message in a PDF.'
    )
    parser.add_argument(
        '--noinput',
        action='store_true',
        help='Create an empty PDF instead of using an input PDF.'
    )

    args = parser.parse_args()

    if args.noinput:
        input_pdf = 'empty.pdf'
        create_empty_pdf(input_pdf)
    else:
        input_pdf = input("Enter the file path to the input PDF: ")

    output_pdf = input("Enter the file path for the output PDF: ")
    hidden_message = input("Enter the message to be encoded: ")

    hide_message(input_pdf, output_pdf, hidden_message)


if __name__ == '__main__':
    main()
