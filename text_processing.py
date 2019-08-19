def wrap_code(content: str):
    code_quote = '`' * 3
    return wrap_text(content, code_quote)

def wrap_text(content, wrapper):
    return f"{wrapper} {content} {wrapper}"

def combine_multiline(lines: list):
    return "\n".join(lines)