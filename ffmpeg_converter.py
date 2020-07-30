# coding=UTF-8
import pathlib
import re
import ffmpeg


def main(): 
    root_path = pathlib.Path('.')
    root_files = [x.name for x in root_path.iterdir() if x.is_file()]

    for dir in root_path.iterdir():
        if dir.is_file():
            continue

        input_file_list = pathlib.Path(dir / 'VIDEO_TS/').glob('VTS_01_*.VOB')

        for input_file in input_file_list:
            if input_file.name == 'VTS_01_0.VOB':
                continue
            file_num = input_file.name.replace('VTS_01_', '-').replace('.VOB', '  ')
            output_file_name = dir.name.replace('ビデオ　家族の記録　', '').replace('  ', file_num) + '.mp4'

            if output_file_name in root_files:
                print('pass')
                continue

            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file_name)

            ffmpeg.run(stream)


if __name__ == "__main__":
    main()
