import hdfs
import os
from hdfs import InsecureClient


hdfs = InsecureClient('http://115.146.86.32:50070', user='qilongz')
for i in hdfs.list('/team40/user_search_data'):
    hdfs_path = '/team40/user_search_data/'+i
    local_path = '/vdc/team40/searched_data/' + i
    if os.path.isfile(local_path) == False:
        hdfs.download(hdfs_path, local_path, overwrite=True, n_threads=5, temp_dir='temp')
