import argparse
import glob
import os
import sys
import time

from pydub import AudioSegment

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-dir")
    parser.add_argument("source_dir", nargs="?", default=".")
                        
    args = parser.parse_args()
    source_files = glob.glob("*.m4b", root_dir=args.source_dir)
    if not source_files:
        print("No m4b files found in %s" % args.source_dir)

    for mp4b_file in source_files:
        start_time = time.time()
        print("Converting %s...(loading)..." % mp4b_file , end="")
        sys.stdout.flush()
        mp4wav_audio = AudioSegment.from_file(
            os.path.join(args.source_dir, mp4b_file), format="mp4")
        base_name, _ext = os.path.splitext(mp4b_file)
        new_file_name = base_name + ".mp3"
        print("(%.1fs)...(saving)..." % (time.time()- start_time), 
            end="")
        sys.stdout.flush()
        start_time = time.time()
        mp4wav_audio.export(os.path.join(args.target_dir, new_file_name),
            format="mp3")
        print("(%.1fs)...Done" % (time.time() - start_time))

if __name__ == "__main__":
    main()
