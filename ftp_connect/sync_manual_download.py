import time
import os
import ftplib
import configparser


# Getting Files list
def list_ftp_files(hostaddr, username, password, src_file_path):
    with ftplib.FTP(hostaddr) as ftp:
        ftp.login(username, password)

        files = ftp.nlst(src_file_path)

        for file in files:
            print(file)

# Download synchronous
def download_files_using_ftp(hostaddr, username, password, src_file_path, dst_file_path=None):
    try:
        ftp = ftplib.FTP(hostaddr)
        ftp.login(user=username, passwd=password)

        files = ftp.nlst(src_file_path)

        for remote_filename in files:
            local_filename = os.path.join(os.getcwd(), remote_filename)
            print(f"local_filename: {local_filename} \tremote_file_names: {remote_filename}")
            with open(local_filename, "wb") as local_file:
                ftp.retrbinary(f"RETR {remote_filename}", local_file.write)
    
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    finally:
        ftp.quit()

if __name__ == "__main__":
    properties = configparser.ConfigParser()
    properties.read("./config.ini")

    config = properties["CONFIG"]

    hostaddr = config["hostaddr"]
    username = config["username"]
    password = config["password"]
    src_file_path = config["src_file_path"]
    dst_file_path = config["dst_file_path"]

    print(f"Host Address                : {hostaddr}")
    print(f"Host Username               : {username}")
    print(f"Host Password               : {password}")
    print(f"Source(Remote) file path    : {src_file_path}")
    print(f"Destination(Local) file path: {dst_file_path}")
    print(f"{'*' * 20}")
    srt_time = time.time()

    download_files_using_ftp(
        hostaddr,
        username,
        password,
        src_file_path,
    )
    
    print(f"Cost : {time.time() - srt_time : .3f} Sec")
