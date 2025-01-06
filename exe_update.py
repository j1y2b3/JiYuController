import subprocess
import os
import shutil

def copy_files(source_dir,target_dir):
    
    os.makedirs(target_dir,exist_ok=True)
    
    for file in os.listdir(source_dir):
        source_file=os.path.join(source_dir,file)
        target_file=os.path.join(target_dir,file)
        if os.path.isfile(source_file):
            shutil.copy(source_file,target_file)

def create_exe(pyname,exename,dirname,iconname):

    path=os.getcwd()

    try:
        shutil.rmtree(dirname)
    except:
        pass
    os.makedirs('temp\\build',exist_ok=True)

    subprocess.run(f'pyinstaller -D {path}\\{pyname}.py -n {exename} -i {path}\\{iconname} --distpath {path} --specpath {path}\\temp --workpath {path}\\temp\\build -w')
    
    shutil.rmtree('temp')
    os.rename(exename,dirname)

    copy_files('file',f'{dirname}\\file')

if __name__=='__main__':

    try:
        create_exe('main','JiyuController','programme','file\\jiyu.ico')
    except Exception as e:
        input('按下回车以结束')
        raise e
    else:
        input('按下回车以结束')
