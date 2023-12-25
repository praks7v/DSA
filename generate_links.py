import os


def generate_file_links(root_dir, target_folder):
    file_links = []
    target_folder_path = os.path.join(root_dir, target_folder)

    for root, dirs, files in os.walk(target_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_dir)
            url_friendly_path = relative_path.replace(" ", "%20")

            # Use the file name (without extension) as the link text
            link_text = os.path.splitext(file)[0].replace("_", " ").title()

            file_link = f"- [{link_text}]({url_friendly_path})"
            file_links.append(file_link)

    return file_links


if __name__ == "__main__":
    root_directory = "."  # Change this to the root directory of your project
    target_data_structure_folder = "Data Structure"
    links = generate_file_links(root_directory, target_data_structure_folder)

    with open("README.md", "w") as readme_file:
        readme_file.write("\n".join(links))
