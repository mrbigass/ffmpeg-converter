# coding=UTF-8
import pathlib
import ffmpeg

def main(): 
    root_path = pathlib.Path('.')

    for dir in root_path.iterdir():
        if dir.is_file():
            continue

        input_file_path = dir / 'VIDEO_TS/VTS_01_1.VOB'
        output_file_name = dir.name.replace('ビデオ　家族の記録　', '') + '.mp4'

        stream = ffmpeg.input(input_file_path)
        stream = ffmpeg.output(stream, output_file_name)

        ffmpeg.run(stream)
            

if __name__ == "__main__":
    main()
