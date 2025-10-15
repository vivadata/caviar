import nbformat

    
def update_content(content:str
              ,starting_tag
              ,ending_tag) -> str:
    lines = content.split('\n')
    inside = False
    output = []
    # Return the content without the lines between the starting and ending tags
    for line in lines:
        if (starting_tag in line):
            inside = True
        if (not inside):
            output.append(line)
        if (ending_tag in line):
            inside = False
    # If we're still inside a tag block at the end (no matching END tag found),
    # return the content up to the start of the unclosed tag block
    return '\n'.join(output)
