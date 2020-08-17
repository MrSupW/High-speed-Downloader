import requests
import os
from threading import Thread, Lock
import time

THREADS = []
file_size_download = 0
speed_all = []
lock = Lock()
is_start = False
session = requests.session()


class DownloadThread(Thread):
    def __init__(self, id, url, start_seek, end_seek, file_path):
        super(DownloadThread, self).__init__()
        self.id = id
        self.url = url
        self.start_seek = start_seek
        self.end_seek = end_seek
        self.file_path = file_path
        self.one_time_size = 16 * 1024
        self.file_size_all = 0
        self.file_size_download = 0

    def run(self):
        global file_size_download, speed_all, is_start
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Range': 'bytes={}-{}'.format(self.start_seek, self.end_seek)}
        start_time = time.time()
        print('线程{} 正在解析所要下载的文件...'.format(self.id))
        response = session.get(self.url, headers=headers, timeout=20)
        data = response.content
        print('线程{} 文件大小为{} 开始下载...'.format(self.id, len(data)))
        is_start = True
        self.file_size_all = len(data)
        with open(self.file_path + str(self.id) + '.tmp', 'wb') as f:
            pass
        with open(self.file_path + str(self.id) + '.tmp', 'ab+') as f:
            count = 0
            while True > 0:
                f.write(data[count * self.one_time_size:(count + 1) * self.one_time_size])
                len_one_download = len(data[count * self.one_time_size:(count + 1) * self.one_time_size])
                self.file_size_download += len_one_download
                end_time = time.time()
                lock.acquire()
                file_size_download += len_one_download
                speed_all[self.id] = self.file_size_download / (end_time - start_time)
                lock.release()
                if (count + 1) * self.one_time_size >= self.file_size_all:
                    break
                count += 1
        print('线程{} 下载完毕！'.format(self.id))


def isAlive(threads):
    for thread in threads:
        if thread.isAlive():
            return True
    return False


def MultiThreadDownload(url, dir_path, thread_num):
    print('正在解析链接......')
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file_path = dir_path + '/' + url.split('/')[-1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    header_infos = session.head(url, headers=headers, timeout=20).headers
    file_size = int(header_infos.get('Content-Length', 0))
    for i in range(thread_num):
        speed_all.append(0)
    if file_size == 0:
        print('链接解析失败')
        exit(0)
    print('链接解析成功 文件大小为{}KB'.format(file_size / 1024))
    size_for_thread = []
    for i in range(thread_num):
        size_for_thread.append(i * file_size // thread_num)
    size_for_thread.append(file_size - 1)
    print('size_for_thread', size_for_thread)
    for i in range(thread_num):
        t = DownloadThread(i, url, size_for_thread[i], size_for_thread[i + 1] - 1, file_path)
        t.start()
        print('线程{} 成功启动！！'.format(i))
        THREADS.append(t)
    while isAlive(THREADS):  # 阻塞式
        time.sleep(0.5)
        if is_start:
            print(
                '当前下载进度为{:.2f}% 下载速度为{:.2f}KB/s'.format((file_size_download / file_size) * 100, sum(speed_all) / 1024))
    with open(file_path, 'wb') as final_file:
        for i in range(thread_num):
            with open(file_path + str(i) + '.tmp', 'rb+') as f:
                final_file.write(f.read())
            os.remove(file_path + str(i) + '.tmp')
    print('下载完成')


if __name__ == '__main__':
    timer1 = time.time()
    url = 'https://ftp.sjtu.edu.cn/ubuntu-cd/20.04.1/ubuntu-20.04.1-desktop-amd64.iso'
    thread_num = 12
    dir_path = '..'
    MultiThreadDownload(url, dir_path, thread_num)
    timer2 = time.time()
    print('平均速度为{:.3f}Mb/s'.format(file_size_download / (timer2 - timer1) / 1024 / 1024))