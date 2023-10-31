### CopyAsPath

ctrl+shift+c：复制选中文件地址，如无选中文件则复制当前文件夹地址。支持同时复制多个文件地址。

### BlackScreen

win+b：打开一张纯黑图片并在副屏全屏（限定honeyview）。

### RemoveCarriageReturn

shift+alt+c：复制pdf中的文字并去除换行符。

### VideoSymbolicLink

```shell
usage: VideoSymbolicLink.py [-h] [-a] [-m MINIMUM] [-o] [-s SEASON] [-b BEGIN] [-r REPETITION] [-e [EXCLUDE ...]] [-sub] src dst

Anime make symbolic link and rename

positional arguments:
  src                   the source folder.
  dst                   the destination folder(create a new folder if folder is not exist).

options:
  -h, --help            show this help message and exit
  -a, --all             enable the option to create symbolic link for all file (default: copy when file size less then 100k).
  -m MINIMUM, --minimum MINIMUM
                        copy when file size less this number(k) (default: 100). eg. [-m 200] --> copy when file size less then 200k
  -o, --original        enable the option to do not rename.
  -s SEASON, --season SEASON
                        the season number (default: 1). eg. [-s 1] --> S01
  -b BEGIN, --begin BEGIN
                        the begin number (default: 1). eg. [-b 1] --> E01, E02, E03...
  -r REPETITION, --repetition REPETITION
                        the repetition number (default: 1). eg. [-r 2] --> E01, E01, E02...
  -e [EXCLUDE ...], --exclude [EXCLUDE ...]
                        the suffix need to exclude. eg. [-e '7z' 'rar']
  -sub, --subtitle      enable the option to keep simplified Chinese subtitles and change the suffix. eg. delete 'tc.ass' and rename 'sc.ass' to 'zh.ass'.
```

为目标文件夹中的文件创建符号链接到目标文件夹并添加(SXXEXX - )前缀。

### MusicScrape

```shell
usage: MusicScrape.py [-h] [-s] src dst

Music scrape with metadata

positional arguments:
  src            the source folder.
  dst            the destination folder(create a new folder if folder is not exist).

options:
  -h, --help     show this help message and exit
  -s, --symlink  enable the option to use symbolic link.
```

根据音乐文件中的元数据为目标文件夹中的音乐文件创建Jellyfin风格的文件结构。
