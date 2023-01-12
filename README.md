Converts all m4b audio files in a directory to mp3 files with a short python program.

* install `ffmpeg` and `pydub` packages before running

==Usage==

Assuming you have a directory `dir_with_m4b_files` with files `Wedding 1.m4b` and `Wedding 2.m4b`, this command:

`mkdir mp3_files`
`python mp4b_to_mp3.py --target-dir mp3_files "dir_with_m4b_files"`

will generate  `Wedding 1.mp3` and `Wedding 2.mp3` in `mp3_files`
