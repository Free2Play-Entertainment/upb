from subprocess import Popen
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('mode')
parser.add_argument('-plugin')
parser.add_argument('-output')
parser.add_argument('-versions')
args = parser.parse_args()


if(args.mode=="build"):
    plugin = args.plugin
    output = args.output
    versions = args.versions.split(",")

    for version in versions:
        p = Popen(['UE_{}\Engine\Build\BatchFiles\RunUAT.bat'.format(version), BuildPlugin, -Plugin=plugin, -Package=output, -rocket], stdout=PIPE, stderr=PIPE)
        output, errors = p.communicate()

elif(args.mode=="push"):
    print("push mode")



