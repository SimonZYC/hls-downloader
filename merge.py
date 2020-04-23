import sys,os,glob
import subprocess

if __name__ == '__main__':
    path = sys.argv[1]
    output_name = sys.argv[2]
    print(path)
    # Merge all .ts files
    files = glob.glob(path + '/**/*.ts', recursive = True)
    files.sort(key = lambda x: int(x.split('/')[-1].split('-')[1]))

    f = open('content.txt', 'w')
    for item in files:
        f.write("file '{}'\n".format(item))
    
    f.close()
    subprocess.call('ffmpeg -f concat -i content.txt -c copy {}'.format(output_name), shell=True)

    
    os.remove('content.txt')
    

