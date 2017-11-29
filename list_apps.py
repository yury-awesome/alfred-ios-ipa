import subprocess
import alfred

def list_apps(arg):
    apps = subprocess.check_output(
            "ios-deploy -B | sort",
            stderr=subprocess.STDOUT,
            shell=True)
    apps = apps.rstrip().split('\n')

    items = []
    for app in apps:
        if arg is '' or app.startswith(arg):
            items.append(alfred.Item({'arg': app}, app, ''))

    alfred.write(alfred.xml(items))

if __name__ == '__main__':
    list_apps(alfred.args()[0])
