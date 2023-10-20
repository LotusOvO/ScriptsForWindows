### CopyAsPath

ctrl+shift+c：复制选中文件地址，如无选中文件则复制当前文件夹地址。支持同时复制多个文件地址。

### BlackScreen

win+b：打开一张纯黑图片并在副屏全屏（限定honeyview）。

### RemoveCarriageReturn

shift+alt+c：复制pdf中的文字并去除换行符。

### VideoSymbolicLink

```python
usage: VideoSymbolicLink.py [-h] [-a] [-o] [-s SEASON] [-b BEGIN] [-r REPETITION] src dst

Anime make symbolic link and rename

positional arguments:
  src                   the source folder.
  dst                   the destination folder(create a new folder if folder is not exist.

options:
  -h, --help            show this help message and exit
  -a, --all             enable the option to create symbolic link for all file (default: copy when file size less then 100k).
  -o, --original        enable the option to do not rename.
  -s SEASON, --season SEASON
                        the season number (default: 1). eg. --season 1 --> S01
  -b BEGIN, --begin BEGIN
                        the begin number (default: 1). eg. --begin 1 --> E01, E02, E03...
  -r REPETITION, --repetition REPETITION
                        the repetition number (default: 1). eg. --repetition 2 --> E01, E01, E02...

```

为目标文件夹中的文件创建符号链接到目标文件夹并添加(SXXEXX - )前缀。
