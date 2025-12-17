import os
import shutil

def spread_lang(src, prefix):
    for file in os.listdir("."):
        if (file.startswith(prefix) and file.endswith(".json") and file != src):
            shutil.copyfile(src, file)
            print(f"Updated {file} 🥳")

if __name__ == "__main__":
    spread_lang("en_us.json", "en_")
    spread_lang("tr_tr.json", "tr_")
