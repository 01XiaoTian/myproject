#也许需要安装pip install pycryptodome
#解决了编码格式报错问题

import PyPDF2

def read_passwords(password_file, encoding='latin1'):
    with open(password_file, 'rb') as file:
        passwords = file.readlines()
    return [password.decode(encoding).strip() for password in passwords]

def decrypt_pdf(pdf_file, password_file):
    # 读取密码列表
    passwords = read_passwords(password_file)
    # 打开加密的PDF文件
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # 确保PDF文件是加密的
        if not reader.is_encrypted:
            print("The PDF file is not encrypted.")
            return
        # 尝试每个密码
        for password in passwords:
            try:
                reader.decrypt(password)
                # 尝试读取第一页，如果成功则表示解密成功
                reader.pages[0]
                print(f"Password found: {password}")
                return
            except Exception as e:
                print(f"Tried password: {password} - Failed ({str(e)})")
    print("No valid password found in the dictionary.")

if __name__ == "__main__":
    pdf_file = "TestPdf113579.pdf"  # PDF文件路径
    password_file = "six_digit_numbers.txt"  # 密码字典文件路径
    decrypt_pdf(pdf_file, password_file)
#解决了编码格式报错问题