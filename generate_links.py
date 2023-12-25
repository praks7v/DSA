import os


def generate_file_links(root_dir, target_folder):
    file_links = []
    target_folder_path = os.path.join(root_dir, target_folder)

    for root, dirs, files in os.walk(target_folder_path):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), target_folder_path)
            file_link = f'- [{file}]({file_path.replace(os.path.sep, "%20")})'
            file_links.append(file_link)
    return file_links


if __name__ == "__main__":
    root_directory = "."  # Change this to the root directory of your project
    target_data_structure_folder = "Data Structure"
    links = generate_file_links(root_directory, target_data_structure_folder)

    with open("README.md", "w") as readme_file:
        readme_file.write("\n".join(links))
