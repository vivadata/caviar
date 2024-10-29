import click
import nbformat
import os
from caviar.cell import update_content


# SOURCE="."
# TARGET="../student-challenge-default"

@click.command()
@click.option('--source', default=None, help='Source directory')
@click.option('--target', default=None, help='Target directory')
@click.option('--starting-tag', default=STARTING_TAG, help='Starting tag')
@click.option('--ending-tag', default=ENDING_TAG, help='Ending tag')
def caviar(source, target, starting_tag, ending_tag):
    # Turning source and target into absolute paths to avoid issues
    if source == None : 
        from  caviar.params import SOURCE
        source = SOURCE
    if target == None :
        from  caviar.params import TARGET
        target = TARGET
    source = os.path.abspath(source)
    target = os.path.abspath(target)
    
    click.echo(f'🔥 Caviarding from {source} to {target}')
    click.echo(f'   Using starting tag {starting_tag} and ending tag {ending_tag}')
    click.echo(os.environ.get('SOURCE'))
    if not os.path.exists(target):
        click.echo(f' Source directory {os.path.abspath(target)} does not exist, if this was intented you need to create it')
    # Scanning the source directory for ".py" and ".ipynb" files
    for root, dirs, files in os.walk(source):
        for file in files:
            
            # For our purpose we want to caviar only file in a "01-Challenges/src/{file}" directory
            # This behavior could be changed to update to user needs
            if (not "01-Challenges" in root) and not ("src" in root):
                click.echo(("FILE: ",root,file))
                if file=="README.md":
                    #click.echo(f'👀 Found file {file} in {root}')
                    # Copying the file to the target directory
                    os.system(f'cp {os.path.join(root, file)} {target}')
                    with open(os.path.join(root, file)) as fp:
                        original_md = fp.read()
                    caviarded_md = update_content(original_md, starting_tag, ending_tag)
                    with open(os.path.join(root.replace(target,source), file), "w") as fp:
                        fp.write(caviarded_md)
                continue
            
            # Copy directory structure to target
            target_dir = root.replace(source, target)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            output_path = os.path.join(root.replace(source,target), file).replace("01-Challenges/src/","")
            
            if  file.endswith('.ipynb'):
                #click.echo(f'👀 Found file {file} in {root}')
                #click.echo(f' {search_files(os.path.join(root, file), ".ipynb", starting_tag, ending_tag)}')
                with open(os.path.join(root, file)) as fp:
                    original_nb = (nbformat.read(fp, as_version=4))
                
                caviarded_cells = []
                for cell in original_nb.cells:
                    if cell.cell_type == "code":
                        cell.source = update_content(cell.source,starting_tag="STRIP_START",ending_tag="STRIP_END")
                        caviarded_cells.append(cell)
                    else:
                        caviarded_cells.append(cell)
                
                # This raise an error about cell id missing,
                # output_nb = nbformat.v4.new_notebook(cells=caviarded_cells
                #                                      , metadata=original_nb.metadata
                #                                      , nbformat=original_nb.nbformat)
                output_nb = original_nb.copy()
                output_nb.cells = caviarded_cells
                print(nbformat.validate(output_nb))
                
                with open(output_path, "w") as fp:
                    nbformat.write(output_nb, fp)
                    
            elif file.endswith('.py'):
                #click.echo(f'👀 Found file {file} in {root}')
                with open(os.path.join(root, file)) as fp:
                    original_py = fp.read()
                caviarded_py = update_content(original_py, starting_tag, ending_tag)
                with open(output_path, "w") as fp:
                    fp.write(caviarded_py)
                    
            elif file.endswith('.md'):
                #click.echo(f'👀 Found file {file} in {root}')
                with open(os.path.join(root, file)) as fp:
                    original_md = fp.read()
                caviarded_md = update_content(original_md, "$"+starting_tag, "$"+ending_tag)
                with open(output_path, "w") as fp:
                    fp.write(caviarded_md)
                    
            # else:
            #     os.system(f'cp {os.path.join(root,file)} {output_path}')
            
                    
            
                    
            
            
def search_files(path, extension, starting_tag, ending_tag):
    with open(path) as f:
        for line in f:
            if starting_tag in line:
                return True
            
            
    
if __name__ == '__main__':
    caviar()
