from src.pdf import PDF
from src.utils import (get_input_path,
                       get_data_path,
                       is_pdf)


def main():
    pdf = PDF()
    file_name = '15_Undangan Evaluasi PPNPN TA 2022_sign_sign.pdf'
    file_path = get_input_path(file_name)

    # Using find_letter_number
    letter_number = pdf.find_letter_number(file_path)

    # find_number
    if letter_number:
        print("Office Letter Number:", letter_number)
    else:
        print("Office Letter Number not found.")


if __name__ == '__main__':
    main()
