# coding=UTF-8
import pathlib
import pdb

def main():
    # find sub-repositories in root repository
    base_path = pathlib.Path('Desktop')
    # sub_dirs = base_path.iterdir()
    sub_dirs = base_path.glob('**/familly_records')

    pdb.set_trace()

    for sub_dir in sub_dirs:
        # sub_dir = ビデオ　家族の記録　No.1  1994.9.15~

        for input_path in pathlib.Path(sub_dir).glob('**/VIDEO_TS/VTS_.*.VOB'):
            # 入力
            # stream = ffmpeg.input('input.VOB')
            stream = ffmpeg.input(input_path)

            # 出力
            output_file_name = 'output.mp4'
            stream = ffmpeg.output(stream, output_file_name)

            # 実行
            ffmpeg.run(stream)



            output_path = to_output_path(args.root_dir, input_path)
            noop_or_create_dir(output_path)
            convert(input_path, output_path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
