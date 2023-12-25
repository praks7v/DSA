import os


def generate_file_links(root_dir, target_folder):
    file_links = []
    target_folder_path = os.path.join(root_dir, target_folder)

    for root, dirs, files in os.walk(target_folder_path):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), root_dir)
            file_link = f'- [{file}]({file_path.replace(os.path.sep, "%20")})'
            file_links.append(file_link)
    return file_links


if __name__ == "__main__":
    root_directory = "/PycharmProjects/DSA"  # Set the root directory of your project
    target_data_structure_folder = "Data Structure"
    data_structure_links = generate_file_links(
        root_directory, target_data_structure_folder
    )

    with open("/PycharmProjects/DSA/README.md", "w") as readme_file:
        readme_file.write("\n".join(data_structure_links))
