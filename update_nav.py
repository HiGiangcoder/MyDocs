import os
import yaml

def get_markdown_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                relative_path = os.path.relpath(filepath, directory)
                files.append(relative_path.replace("\\", "/"))
    return sorted(files)

def update_mkdocs_yml(root_folder):
    config_file = "mkdocs.yml"
    with open(config_file, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    markdown_files = get_markdown_files(root_folder)
    config["nav"] = [{"Home": "index.md"}]  # Reset nav
    for md_file in markdown_files:
        title = os.path.basename(md_file).replace(".md", "").capitalize()
        config["nav"].append({title: md_file})

    with open(config_file, "w", encoding="utf-8") as file:
        yaml.dump(config, file, allow_unicode=True, default_flow_style=False)

    print("mkdocs.yml updated successfully!")

if __name__ == "__main__":
    update_mkdocs_yml("docs")
