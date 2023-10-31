import argparse
import re
import mutagen
import os
import shutil


def regularity(s):
    s = re.sub(r"\\|/|\|", r"&", s)
    s = re.sub(r":", "：", s)
    s = re.sub(r"\?", "？", s)
    s = re.sub(r"\*", "`·`", s)
    s = re.sub(r"\"", "'", s)
    s = re.sub(r"<", "[", s)
    s = re.sub(r">", "]", s)
    return s


def music_scrape(src_path, dst_path, using_symlink=False):
    for root, dirs, files in os.walk(src_path):
        file_dir = ""
        if not re.search(r"(?i)BD|Scan", root):
            for file in files:
                file_path = os.path.join(root, file)
                audio = mutagen.File(file_path)
                if audio:
                    file_dir = os.path.join(dst_path, regularity(audio['ARTIST'][0]), f'({audio["DATE"][0]}){regularity(audio["ALBUM"][0])}')
                    if "DISCTOTAL" in audio and audio["DISCTOTAL"][0] != "1":
                        file_dir = os.path.join(file_dir, f"Disc {regularity(audio['DISCNUMBER'][0])}")
                    if not os.path.exists(file_dir):
                        os.makedirs(file_dir)
                    file_dir = os.path.join(file_dir,
                                            f"{int(audio['TRACKNUMBER'][0]):>02d} - {regularity(audio['TITLE'][0])}{os.path.splitext(file)[-1]}")
                    if using_symlink:
                        # 符号链接
                        os.symlink(file_path, file_dir)
                    else:
                        # 复制
                        shutil.copy(file_path, file_dir)
                else:
                    if using_symlink:
                        # 符号链接
                        os.symlink(file_path, os.path.join(os.path.split(file_dir)[0], os.path.split(file_path)[1]))
                    else:
                        # 复制
                        shutil.copy(file_path, os.path.join(os.path.split(file_dir)[0], os.path.split(file_path)[1]))
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Music scrape with metadata"
    )
    parser.add_argument('src',
                        help="the source folder.")
    parser.add_argument('dst',
                        help="the destination folder(create a new folder if folder is not exist).")
    parser.add_argument('-s', '--symlink',
                        action="store_true",
                        help="enable the option to use symbolic link.")
    args = parser.parse_args()
    music_scrape(args.src, args.dst, args.symlink)
