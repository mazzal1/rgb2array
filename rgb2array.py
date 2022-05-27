from PIL import Image
import numpy as np
import argparse


def main(filepaths: list[str]):
    for filepath in filepaths:
        img = Image.open(filepath).convert('L')
        matrix = np.array(img, np.float32)
        np.set_printoptions(threshold=np.inf, formatter={
                            'all': lambda x: f'{x:.2f}'})
        with open('result.txt', 'w') as file:
            file.writelines(str(matrix.flatten()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert an RGB image to an array of grayscale values.')
    parser.add_argument('filepaths', type=str, nargs='+',
                        help='Paths to RGB images')
    args = parser.parse_args()
    main(args.filepaths)
