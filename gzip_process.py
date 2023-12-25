import os
import gzip
import logging


def decompress(src, dst):
    logging.info("decompress {} to {}".format(src, dst))
    dst_dir = os.path.dirname(dst)
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    with gzip.open(src, 'rb') as f_cmp:
        with open(dst, 'wb') as f_dec:
            f_dec.write(f_cmp.read())

def compress(src, dst):
    logging.info("compress {} to {}".format(src, dst))
    dst_dir = os.path.dirname(dst)
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    with open(src, 'rb') as f_raw:
        with gzip.open(dst, 'wb') as f_cmp:
            f_cmp.write(f_raw.read())

def gzip_extract(src, dst):
    if not os.path.isdir(src):
        logging.info("{} not exists!".format(src))
        return

    walk_result = os.walk(src)
    for path, dir_list, file_list in walk_result:
        for file in file_list:
            f_name = os.path.normpath(os.path.join(path, file))
            new_name = f_name.replace(os.path.normpath(src) + os.sep, '')
            f_name_dst = os.path.normpath(os.path.join(dst, new_name))
            decompress(f_name, f_name_dst)

def gzip_encod(src, dst):
    if not os.path.isdir(src):
        logging.info("{} not exists!".format(src))
        return

    walk_result = os.walk(src)
    for path, dir_list, file_list in walk_result:
        for file in file_list:
            f_name = os.path.normpath(os.path.join(path, file))
            new_name = f_name.replace(os.path.normpath(src) + os.sep, '')
            f_name_dst = os.path.normpath(os.path.join(dst, new_name))
            compress(f_name, f_name_dst)


if __name__ == "__main__":
    gzip_extract("./temp/web", "./temp/extracted")
    gzip_encod("./temp/extracted", "./temp/new")