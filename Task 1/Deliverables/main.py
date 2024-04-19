import sys
import getopt
import yaml
from yaml.loader import SafeLoader
from mailmerge import MailMerge

is_debug = False


def main(argv):
    config_file, output_dir = gather_params(argv)
    if is_debug:
        print("Config file is ", config_file)
        print("Output dir is ", output_dir)
    bands = get_bands(config_file)
    generate_documents(bands, output_dir)


def gather_params(argv):
    global is_debug
    opts, args = getopt.getopt(argv, "c:o:", ["config=", "output=", "debug"])
    for opt, arg in opts:
        if opt in ("-c", "--config"):
            config_file = arg
        elif opt in ("-o", "--output"):
            output_dir = arg
        elif opt == '--debug':
            is_debug = True
    return config_file, output_dir


def get_bands(config_file):
    with open(config_file) as f:
        data = yaml.load(f, Loader=SafeLoader)
        if is_debug:
            print("Configuration data loaded successfully!")
        return data["bands"]


def generate_documents(bands, output_dir):
    template = 'template.docx'
    try:
        for band in bands:
            if is_debug:
                print("Generating document for band ", band["name"])
                print(band)
            filename = output_dir + "\\" + band["name"] + ".docx"
            document = MailMerge(template)
            document.merge(
                BN=band["initials"],
                Band=band["name"],
                Members=band["members"],
                Genre=band["genre"],
                About=band["about"],
                Music1=band["musics"][0]["name"],
                Music2=band["musics"][1]["name"],
                Music3=band["musics"][2]["name"],
                Album1=band["musics"][0]["album"],
                Album2=band["musics"][1]["album"],
                Album3=band["musics"][2]["album"]
            )
            document.write(filename)
            if is_debug:
                log_message = "Document " + filename + " generated successfully!"
                print(log_message)
        print("Task completed successfully!")
    except FileNotFoundError:
        print("Error while creating file - output directory may not exist")
    except:
        print("Error while generating documents")


if __name__ == "__main__":
    main(sys.argv[1:])
