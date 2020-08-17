import time
from threading import Lock
from PyQt5.QtCore import QThread, pyqtSignal
import requests
import math
import globals as g
import os

lock = Lock()


def isAlive(threads):
    for thread in threads:
        if thread.isRunning():
            return True
    return False


class DownloadThread(QThread):
    text_and_progress_signal = pyqtSignal(str, float)

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
        self.text_and_progress_signal.emit('线程{} 成功启动！！'.format(self.id), math.floor(30.0 / g.download_thread_num))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Range': 'bytes={}-{}'.format(self.start_seek, self.end_seek)}
        start_time = time.time()
        self.text_and_progress_signal.emit('线程{} 正在解析所要下载的文件...'.format(self.id), 0.0)
        response = requests.get(self.url, headers=headers, timeout=20)
        data = response.content
        self.text_and_progress_signal.emit('线程{} 文件大小为{} 开始下载...'.format(self.id, len(data)), 0.0)
        g.is_start = True
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
                g.file_size_download += len_one_download
                g.speed_all[self.id] = self.file_size_download / (end_time - start_time)
                lock.release()
                if (count + 1) * self.one_time_size >= self.file_size_all:
                    break
                count += 1
        self.text_and_progress_signal.emit('线程{} 下载完毕！'.format(self.id), 0.0)


class MultiThreadDownload(QThread):
    text_and_progress_signal = pyqtSignal(str, float)
    download_finished = pyqtSignal()
    progress_bar_value = 30

    def __init__(self, dealTextAndProgressSignal):
        super(MultiThreadDownload, self).__init__()
        self.dealTextAndProgressSignal = dealTextAndProgressSignal

    def run(self):
        self.text_and_progress_signal.emit('计时开始......', 0.0)
        timer1 = time.time()
        self.text_and_progress_signal.emit('正在解析链接......', 0.0)
        if not os.path.exists(g.download_target_dir):
            os.mkdir(g.download_target_dir)
        file_path = g.download_target_dir + '/' + g.download_url.split('?')[0].split('/')[-1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        header_infos = requests.head(g.download_url, headers=headers, timeout=20).headers
        file_size = int(header_infos.get('Content-Length', 0))
        for i in range(g.download_thread_num):
            g.speed_all.append(0)
        if file_size == 0:
            self.text_and_progress_signal.emit('链接解析失败', 0.0)
            exit(0)
        self.text_and_progress_signal.emit('链接解析成功 文件大小为{}KB'.format(file_size / 1024), 0.0)
        size_for_thread = []
        for i in range(g.download_thread_num):
            size_for_thread.append(i * file_size // g.download_thread_num)
        size_for_thread.append(file_size - 1)
        for i in range(g.download_thread_num):
            t = DownloadThread(i, g.download_url, size_for_thread[i], size_for_thread[i + 1] - 1, file_path)
            t.text_and_progress_signal.connect(self.dealTextAndProgressSignal)
            t.start()
            g.THREADS.append(t)
        progress_pre_value = 0
        while isAlive(g.THREADS):  # 阻塞式
            time.sleep(0.1)
            if g.is_start:
                self.text_and_progress_signal.emit(
                    '下载速度为{:.2f}KB/s'.format((sum(g.speed_all) / 1024)), 0.0)
                self.progress_bar_value += math.ceil(g.file_size_download / file_size * 70) - progress_pre_value
                self.text_and_progress_signal.emit('', math.ceil(
                    g.file_size_download / file_size * 70) - progress_pre_value)
                progress_pre_value = self.progress_bar_value
        with open(file_path, 'wb') as final_file:
            for i in range(g.download_thread_num):
                with open(file_path + str(i) + '.tmp', 'rb+') as f:
                    final_file.write(f.read())
                os.remove(file_path + str(i) + '.tmp')
        timer2 = time.time()
        self.text_and_progress_signal.emit(
            '平均速度为{:.3f}Mb/s 共计用时{:.2f}s'.format(g.file_size_download / (timer2 - timer1) / 1024 / 1024,
                                                 timer2 - timer1),0.0)
        self.download_finished.emit()
