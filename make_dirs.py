

def main():
    import os, pathlib
    # thesis_folder = "\\OxThesis-master" # this will surely be modified using pathlib
    # # print(os.getcwd() + path)
    # # print(os.listdir('.' + path))
    # path = os.getcwd() + thesis_folder # 
    # folder = pathlib.Path("figures_chapter/")
    # print(type(path))
    # for p in pathlib.Path(path).iterdir():
    #     if p.is_dir():
    #         folder.mkdir(parents=True, exist_ok=True)

    path = os.getcwd()+"\\OxThesis-master\\"
    print(path)
    chapter_folders = []
    for root, dire, files in os.walk(path):
        for d in dire:
            if "chapter" in d:
                chapter_folders.append(d)
    
    os.chdir(path)
    for folder in chapter_folders:
        os.makedirs(os.path.join(folder, 'figures'))

    


if __name__ == '__main__':
    main()