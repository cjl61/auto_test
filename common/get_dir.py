import os

work_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APP_DIR = os.path.join(work_dir,'app')
BASE_DIR = os.path.join(work_dir,'base')
COMMON_DIR =os.path.join(work_dir,'common')
CONFIG_DIR = os.path.join(work_dir,'config')
LOGS_DIR = os.path.join(work_dir,'logs')
REPORT_DIR = os.path.join(work_dir,'report')
SCREENSHORT_DIR = os.path.join(work_dir,'screenshort')
CASE_DIR = os.path.join(work_dir,'test_case')
if __name__ == '__main__':
    print(work_dir)
    print(APP_DIR)
    print(SCREENSHORT_DIR)
    print(CASE_DIR)
