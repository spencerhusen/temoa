import sys

def main():
    datafile = sys.argv[1]
    inputConfig = open("../temoa_model/config_sample_in", "r")
    readWriteFile(inputConfig, datafile)


def readWriteFile(configFile, sqliteFile):
    INPUT_FLAG = "--input=data"
    OUTPUT_FLAG = "--output=data"
    outputConfig = open("../temoa_model/config_sample", "w")
    for line in configFile:
        if INPUT_FLAG in line:
            outputConfig.write(INPUT_FLAG + "_files/" + sqliteFile + "\n")
        elif OUTPUT_FLAG in line:
            outputConfig.write(OUTPUT_FLAG + "_files/" + sqliteFile + "\n")
        else:
            outputConfig.write(line)
    outputConfig.close()


if __name__ == "__main__":
    main()

