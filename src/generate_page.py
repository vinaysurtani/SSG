from markdown_to_htmlnode import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_data = f.read()
    with open(template_path, 'r') as g:
        template_data= g.read()
    htmlnode = markdown_to_html_node(markdown_data)
    htmlstr = htmlnode.to_html()
    title = extract_title(markdown_data)
    template_data = template_data.replace("{{ Title }}",title)
    template_data = template_data.replace("{{ Content }}",htmlstr)
    template_data = template_data.replace('href="/',f'href="{basepath}')
    template_data = template_data.replace('src="/',f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as h:
        h.write(template_data)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    #print(os.listdir(dir_path_content))
    for file in os.listdir(dir_path_content):
        new_dir_path = os.path.join(dir_path_content,file)
        new_dest_dir_path = os.path.join(dest_dir_path,file)
        #print(new_dir_path)
        if os.path.isdir(new_dir_path):
            generate_pages_recursive(new_dir_path,template_path, new_dest_dir_path, basepath)
        elif os.path.isfile(new_dir_path) and new_dir_path.endswith('.md'):
            #print('md page reached, generate .html here')
            #print(new_dir_path)
            html_file = new_dest_dir_path.replace('.md', '.html')
            generate_page(new_dir_path, template_path, html_file, basepath)


# generate_pages_recursive('/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/content/', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/template.html', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/public/')