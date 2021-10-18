import os
import argparse 
import sys

if __name__ == "__main__":
    # os.environ["CUDA_VISIBLE_DEVICES"]="1,2"
    os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
    argparser = argparse.ArgumentParser(description='train')
    argparser.add_argument('-trdata', type=str)
    args = argparser.parse_args()

    pwd = os.path.abspath(os.path.dirname(__file__))
    #两步检测的第一步
    # print("第一步")
    # os.system('%s/tools/train_step1.sh'%pwd)
    # 第二步
    print("第二步")
    os.system('%s/tools/train_step2.sh'%pwd)
    sys.stdout.write('Process end with exit code 0\n')
