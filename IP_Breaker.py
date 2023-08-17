import sys

def replace_commas_with_line_breaks(input_text):
    modified_text = input_text.replace(',', '\n')
    return modified_text

def remove_leading_spaces(input_text):
    lines = input_text.split('\n')
    cleaned_lines = [line.lstrip() for line in lines]
    return '\n'.join(cleaned_lines)

def add_line_break_after_ip(input_text):
    lines = input_text.split('\n')
    modified_lines = []
    for line in lines:
        if ":" in line:
            parts = line.split(":")
            if len(parts) > 1 and any(part.strip() and part.strip()[0].isdigit() for part in parts[1:]):
                modified_lines.append(parts[0].strip() + ":\n" + "\n".join(parts[1:]).strip())
            else:
                modified_lines.append(line)
        else:
            modified_lines.append(line)
    return "\n".join(modified_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 process_text.py <input_file>")
        sys.exit(1)

    input_file_name = sys.argv[1]
    
    with open(input_file_name, "r") as file:
        input_text = file.read()

    modified_text = replace_commas_with_line_breaks(input_text)
    cleaned_text = remove_leading_spaces(modified_text)
    final_text = add_line_break_after_ip(cleaned_text)
    
    print(final_text)
