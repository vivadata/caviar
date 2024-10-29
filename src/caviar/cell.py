import nbformat

    
def update_content(content:str
              ,starting_tag
              ,ending_tag) -> str:
    lines = content.split('\n')
    inside = False
    queue,output = [],[]
    # Return the content without the lines between the starting and ending tags
    for line in lines:
        if (starting_tag in line):
            inside = True
            queue.append(line)
        if (not inside):
            output.append(line)
        if (ending_tag in line):
            queue.append(line)
            inside = False
    if inside:
        raise ValueError("The ending tag was not found")
    return '\n'.join(output)
