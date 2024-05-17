import argparse
import glob
import os
import sys
import time

from pydub import AudioSegment

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-dir", help="Defaults to the source directory")
    parser.add_argument("--skip-existing", action="store_true",
            help="Don't convert files if the target file already exists.")
    parser.add_argument("source_dir_or_file", nargs="?", default=".",
                        help="Directory with mp4b files, defaults to the current directory.")

    args = parser.parse_args()
    if os.path.isfile(args.source_dir_or_file):
        print(f"{args.source_dir_or_file} is a file, assuming it is an audio file")
        source_files = [args.source_dir_or_file]
        source_dir = os.path.dirname(args.source_dir_or_file)
    else:
        source_files = glob.glob("*.m4b", root_dir=args.source_dir_or_file)
        if not source_files:
            print("No m4b files found in %s" % args.source_dir_or_file)
        source_dir = args.source_dir

    target_dir = args.target_dir
    if target_dir is None:
        target_dir = source_dir

    for mp4b_file in source_files:
        base_name, _ext = os.path.splitext(mp4b_file)
        new_file_name = base_name + ".mp3"
        target_file = os.path.join(target_dir, new_file_name)
        print("Converting %s..." % mp4b_file , end="")
        if args.skip_existing and os.path.isfile(target_file):
            print("Already Done")
            continue
        start_time = time.time()
        print("(loading)...", end="")
        sys.stdout.flush()
        mp4wav_audio = AudioSegment.from_file(
            os.path.join(source_dir, mp4b_file), format="mp4")
        print("(%.1fs)...(saving)..." % (time.time()- start_time),
            end="")
        sys.stdout.flush()
        start_time = time.time()
        mp4wav_audio.export(target_file, format="mp3")
        print("(%.1fs)...Done" % (time.time() - start_time))

if __name__ == "__main__":
    main()
