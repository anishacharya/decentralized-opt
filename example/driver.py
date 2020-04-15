import argparse
import os
import time

from dec_opt.data_reader import DataReader

curr_dir = os.path.dirname(__file__)


def _parse_args():
    parser = argparse.ArgumentParser(description='driver.py')
    parser.add_argument('--d', type=str, default='mnist',
                        help='Pass data-set')
    parser.add_argument('--r', type=str, default=os.path.join(curr_dir, './data/'),
                        help='Pass data root')
    args = parser.parse_args()
    return args


def run_experiment():
    raise NotImplementedError


if __name__ == '__main__':
    args = _parse_args()
    print(args)
    print("load data-set")
    data_set = args.d
    root = args.r

    t0 = time.time()
    data_reader = DataReader(root=root, data_set=data_set, download=True)
    print('Time taken to load Data {} sec'.format(time.time() - t0))

