import os
import shutil


def copy_static():
    src_path = '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/static/'
    desti_path = '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/public/' # via WSL console
    val = os.path.exists(desti_path)
    if os.path.exists(desti_path):
        print(os.listdir(desti_path))
        shutil.rmtree(desti_path)
        print(f"Cleared {desti_path}")
    os.makedirs(desti_path, exist_ok=True)
    print(f"public folder created at {desti_path}")

    if os.path.exists(src_path):
        print(os.listdir(src_path))
        copy_recursive(src_path, desti_path)
        print(f"copy completed")
    #return val


def copy_recursive(src_path, desti_path):
    for file in os.listdir(src_path):
        #print(type(file))
        #print(os.path.isfile(os.path.join(src_path,file)))
        src_item = os.path.join(src_path,file)
        dest_item = os.path.join(desti_path,file)
        if os.path.isfile(src_item):
            shutil.copy(src_item,dest_item)
            print(f"{file} copied")
        elif os.path.isdir(src_item):
            #os.mkdir(os.path.join(desti_path,file))
            os.makedirs(dest_item, exist_ok=True)
            print(f"{file} folder created")
            copy_recursive(src_item, dest_item)
