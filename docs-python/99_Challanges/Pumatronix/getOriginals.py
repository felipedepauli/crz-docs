import os
import argparse
import shutil

# Criar um programa capaz de pegar os nomes de todos os arquivos do diretório root
# e, com eles, copiar os arquivos com o mesmo nome de outro diretório para um terceiro diretório!

# /dir/with/reference/files
#       - image01.jpg
#       - image02.jpg
#       - image03.jpg
#       - image04.jpg
#       - image05.jpg
#       - image06.jpg

# /dir/with/original/files
#       - image00.jpg
#       - image02.jpg
#       - image04.jpg
#       - image06.jpg
#       - image08.jpg

# Resultado:
# /dest/dir
#       - image02.jpg
#       - image04.jpg
#       - image06.jpg

# python3 getOriginals.py /dir/with/reference/files /dir/with/original/files /dest/dir

def main(root, originals, dest):

    count = 0

    for dirpath, dirname, filename in os.walk(root):
        for name in filename:
            absPath = os.path.join(originals, name)
            if os.path.exists(absPath):
                shutil.copyfile(absPath, dest +"/"+ name)
                print(f'[Ok] {absPath}')
                count += 1
            else:
                print(f'[Error] File {absPath} does not exist.')
    print(f'{count} files have been found and copied.')

# Definition of variables that will receive the arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Original Images')
    parser.add_argument("root",     help="Root Directory to Look UP for Filenames")
    parser.add_argument("originals",help="Path to Originals")
    parser.add_argument("dest",     help="Path to Destination")
    args = parser.parse_args()

    main(args.root, args.originals, args.dest)

















