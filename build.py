import subprocess
subprocess.call(["docker", "build", "-t", "mytensorflow", "."])
subprocess.call(["docker", "run", "-it", "--rm", "mytensorflow"])