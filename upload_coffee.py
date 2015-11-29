import subprocess

def main():
    subprocess.call('git add coffeelog.json', shell=True)
    subprocess.call('git add coffeelog.js', shell=True)
    subprocess.call('git commit -m "Drank Cofee"', shell=True)
    subprocess.call('git push', shell=True)

if __name__ == '__main__':
    main()
