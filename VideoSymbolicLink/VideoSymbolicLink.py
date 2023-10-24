import os
import shutil
import argparse
import re


def make_video_link(src_path, dst_path="./SymbolicLink", copy_small_file_flag=True, exclude_suffix=None,
                    small_file_size=100 * 1024):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    elif dst_path == "./SymbolicLink":
        shutil.rmtree(dst_path)
        os.mkdir(dst_path)
    files = os.listdir(src_path)
    for file in files:
        src = os.path.join(src_path, file)
        if os.path.isfile(src) and not file.endswith(exclude_suffix):
            dst = os.path.join(dst_path, file)
            if copy_small_file_flag and os.path.getsize(src) <= small_file_size:
                shutil.copy(src, dst)
            else:
                os.symlink(src, dst)


def renamer(src_path, season=1, begin=1, repetition=1):
    files = [file for file in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, file))]
    tmp = 1
    for i, file in enumerate(files):
        src = os.path.join(src_path, file)
        new_file = f'S{season:>02d}E{begin:>02d} - {file}'
        dst = os.path.join(src_path, new_file)
        tmp += 1
        if tmp > repetition:
            tmp = 1
            begin += 1
        os.rename(src, dst)


def subtitle_renamer(src_path):
    files = os.listdir(src_path)
    for file in files:
        if re.search(r'(?i)tc.ass|cht.ass', file):
            os.remove(os.path.join(src_path, file))
        elif re.search(r'(?i)jpsc.ass', file):
            os.rename(os.path.join(src_path, file), os.path.join(src_path, re.sub(r'(?i)jpsc.ass', 'zh.ass', file)))
        elif re.search(r'(?i)jpchs.ass', file):
            os.rename(os.path.join(src_path, file), os.path.join(src_path, re.sub(r'(?i)jpchs.ass', 'zh.ass', file)))
        elif re.search(r'(?i)chs.ass', file):
            os.rename(os.path.join(src_path, file), os.path.join(src_path, re.sub(r'(?i)chs.ass', 'zh.ass', file)))
        elif re.search(r'(?i)sc.ass', file):
            os.rename(os.path.join(src_path, file), os.path.join(src_path, re.sub(r'(?i)sc.ass', 'zh.ass', file)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Anime make symbolic link and rename"
    )
    parser.add_argument('src',
                        help="the source folder.")
    parser.add_argument('dst',
                        help="the destination folder(create a new folder if folder is not exist).")
    parser.add_argument('-a', '--all',
                        action="store_false",
                        help="enable the option to create symbolic link for all file (default: copy when file size "
                             "less then 100k).")
    parser.add_argument('-m', '--minimum',
                        default=100*1024,
                        type=int,
                        help="copy when file size less this number(k) (default: 100). eg. [-m 200] --> copy when file "
                             "size less then 200k")
    parser.add_argument('-o', '--original',
                        action="store_false",
                        help="enable the option to do not rename."
                        )
    parser.add_argument('-s', '--season',
                        default=1,
                        type=int,
                        help="the season number (default: 1). eg. [-s 1] --> S01")
    parser.add_argument('-b', '--begin',
                        default=1,
                        type=int,
                        help="the begin number (default: 1). eg. [-b 1] --> E01, E02, E03...")
    parser.add_argument('-r', '--repetition',
                        default=1,
                        type=int,
                        help="the repetition number (default: 1). eg. [-r 2] --> E01, E01, E02...")
    parser.add_argument('-e', '--exclude',
                        action="extend",
                        nargs="*",
                        type=str,
                        help="the suffix need to exclude. eg. [-e '7z' 'rar']")
    parser.add_argument('-sub', '--subtitle',
                        action="store_true",
                        help="enable the option to keep simplified Chinese subtitles and change the suffix. "
                             "eg. delete 'tc.ass' and rename 'sc.ass' to 'zh.ass'.")
    args = parser.parse_args()
    make_video_link(args.src, args.dst, args.all, tuple(args.exclude), args.minimum)
    if args.original:
        renamer(args.dst, args.season, args.begin, args.repetition)
    if args.subtitle:
        subtitle_renamer(args.dst)
    pass
