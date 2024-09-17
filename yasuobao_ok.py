#成功可运行，需要在这个main中才可以
import pyzipper

def unzip_file_with_password(zip_path, extract_path, password):
    with pyzipper.AESZipFile(zip_path) as zf:
        try:
            zf.pwd = password.encode('utf-8')
            zf.extractall(path=extract_path)
            print(f'成功解压，密码是: {password}')
            return True
        except (RuntimeError, pyzipper.zipfile.BadZipFile):
            return False

def dictionary_attack_zip(zip_path, extract_path, dictionary_path):
    with open(dictionary_path, 'r') as f:
        for line in f:
            password = line.strip()
            print(f'尝试密码: {password}')
            if unzip_file_with_password(zip_path, extract_path, password):
                return password
    return None

if __name__ == "__main__":
    zip_path = 'test.zip'  # 加密 ZIP 文件的路径
    extract_path = 'E:/CodeFile/Python/pythonProject'  # 解压 ZIP 文件内容的路径
    dictionary_path = 'xato-net-10-million-passwords.txt'  # 密码字典库文件的路径

    found_password = dictionary_attack_zip(zip_path, extract_path, dictionary_path)
    if found_password:
        print(f'找到密码: {found_password}')
    else:
        print('在给定的密码字典库中未找到密码')
