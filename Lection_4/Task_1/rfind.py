import argparse
import os

def findFile(fileName, path):
    try:
        for file in os.listdir(path):
            jointPath = os.path.join(path, file)
            if file.find(fileName) != -1:
                print(os.path.abspath(jointPath))
            elif os.path.isdir(jointPath):
                findFile(fileName, jointPath)
    except Exception as exc:
        print(exc)

parser = argparse.ArgumentParser(description="file finder", add_help=True)
parser.add_argument('--folder', default="C:\\", help="path of needed folder(default C:\\)")
parser.add_argument('--file', help="name of file searched for(required)", required=True)
findFile(parser.parse_args().file, parser.parse_args().folder)