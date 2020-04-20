import subprocess

def dump(url):
    try:
         return subprocess.Popen(['pg_dump', url], stdout = subprocess.PIPE)
     except 0SError as err:
         print(f"Error: {err}")
         sys.exit(1)
