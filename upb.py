import argparse, os

def build(args):
    versions = args.versions.split(",")
    plugin = ' -Plugin="{}"'.format(args.plugin)
    package = ' -Package="{}"'.format(args.output)
    for version in versions:
        path = os.path.join(os.environ['UEINSTALL'], 'UE_{}\Engine\Build\BatchFiles\RunUAT.bat'.format(version))
        buildplugin = " BuildPlugin"
        os.system(path + buildplugin + plugin + package)

def push(args):
    print("push mode")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

buildparser = subparsers.add_parser("build")
buildparser.add_argument('-plugin')
buildparser.add_argument('-output')
buildparser.add_argument('-versions')
buildparser.set_defaults(func=build)

pushparser = subparsers.add_parser("push")
pushparser.set_defaults(func=push)

args = parser.parse_args()
try:
    args.func(args)
except AttributeError:
    parser.error("too few arguments")