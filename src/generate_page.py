import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path)
    md_file = f.read()
    f.close()

    t = open(template_path)
    template_file = t.read()
    t.close()

    HTML = markdown_to_html_node(md_file).to_html()
    Title = extract_title(md_file)

    template_file_titled = template_file.replace("{{ Title }}", Title)
    template_file_final = template_file_titled.replace("{{ Content }}", HTML)

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    ff = open(dest_path, "w")
    ff.write(template_file_final)
    ff.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        source = os.path.join(dir_path_content, item)
        if os.path.isfile(source) and item.endswith(".md"):
            dest = os.path.join(dest_dir_path, item).replace(".md", ".html")
            generate_page(source, template_path, dest)
        if os.path.isdir(source):
            dest = os.path.join(dest_dir_path, item)
            generate_pages_recursive(source, template_path, dest)



