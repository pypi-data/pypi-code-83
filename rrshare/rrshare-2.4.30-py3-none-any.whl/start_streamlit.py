#TODO
import os
import subprocess

#print(os.system("ps -a | grep streamlit"))
#print(subprocess.run("ps -a |grep streamlit"))

def bash_command(cmd):
  subprocess.Popen(['/bin/bash', '-c', cmd])


def st_run_py():
  # If your shell script has shebang, 
  # you can omit shell=True argument.

  #subprocess.run(["~/rrshare/rrshare/start_streamlit.sh",  "arguments"], shell=True)
  subprocess.run(["~/rrshare/rrshare/start_streamlit.sh",  "arguments"],shell=True)

if __name__ == "__main__":
    bash_command('ls')

  








