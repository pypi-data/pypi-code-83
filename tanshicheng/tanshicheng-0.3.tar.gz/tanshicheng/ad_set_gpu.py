import subprocess
import os
import re
import sys
import socket
# 简单导入 set_gpu 的一种方式:
# with open(os.environ['HOME']+'/git/mycode/tanshicheng/ad_set_gpu.py', 'r', encoding='utf-8') as r:
#     exec(r.read())
# 原文中设置显卡的地方可以避免冲突:
# if not 'CUDA_VISIBLE_DEVICES' in os.environ:
#     os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


def set_gpu(showAllGpu=False):
    """
    指定最小显存占用GPU
    :param showAllGpu: bool; 是否显示所有gpu的状态
    :return:
    """
    gpu, ext_gpu_mem = -1, -1
    try:
        ext_mem = subprocess.getstatusoutput('free -m')[1].split('\n')[1].strip()
        ext_mem = int(re.split(r'\s+', ext_mem)[6])  # 不是free而是available
    except:
        ext_mem = -1
    try:
        ext_cpu = subprocess.getstatusoutput('top -bn 1 | head -n 10')[1]
        ext_cpu = re.findall(r'(?<=,)[ \d.]+?(?=id,)', ext_cpu)[0].strip()
    except:
        ext_cpu = ''
    try:
        cpu_num = int(subprocess.getstatusoutput('cat /proc/cpuinfo |grep "physical id"|sort|uniq|wc -l')[1])
        cpu_cores = int(subprocess.getstatusoutput('cat /proc/cpuinfo |grep "cpu cores"|uniq')[1].split('\n')[0].split(':')[1])
        core_pro = int(subprocess.getstatusoutput('cat /proc/cpuinfo |grep "processor"|wc -l')[1])
        core_pro = core_pro / cpu_num / cpu_cores
    except:
        cpu_num, cpu_cores, core_pro = 0, 0, 0
    (status, result) = subprocess.getstatusoutput('nvidia-smi')
    i_m = []
    power = 'W'
    if status == 0:
        if showAllGpu:
            print(result)
        r = re.findall(r'(?<=[|/])[\s\d]+?(?=MiB)', result)
        r = [int(r[i + 1]) - int(r[i]) for i in range(0, len(r), 2)]
        w = [i.replace(' ', '') for i in re.findall(r'(?<=\s)[\s\d]+?W\s+?/[\s\d]+?W(?=\s)', result)]
        i_m = [(i, j) for i, j in enumerate(r)]
        if i_m:
            i_m = sorted(i_m, key=lambda t: t[1])
            gpu = i_m[-1][0]
            ext_gpu_mem = i_m[-1][1]
        power = w[gpu]
    hostname = subprocess.getstatusoutput('hostname')[1]
    ip = socket.gethostbyname(hostname)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ...
    print('%s@%s, 设置显卡:%d(%s)-%d, 剩余CPU:%s%%(%d-%d-%d), 剩余内存:%.1fGB, 剩余显存:%.1fGB' %
          (hostname, ip, gpu, power, len(i_m) - 1, ext_cpu, cpu_num, cpu_cores, core_pro, ext_mem / 1024,
           ext_gpu_mem / 1024))
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu)
    return gpu


if __name__ == '__main__':
    gpu = set_gpu()
    if len(sys.argv) > 1:
        sys.exit(gpu+1)
