import sys
from clang.cindex import Config, Index, CursorKind

def extract_functions_and_comments(cursor, file_name, level=0):
    if cursor.location.file is not None and cursor.location.file.name != file_name:
        return

    if cursor.kind == CursorKind.FUNCTION_DECL or cursor.kind == CursorKind.CXX_METHOD:
        print("Function: ", cursor.spelling)
        print("Line: ", cursor.location.line)

        comments = cursor.get_parsed_comment()
        if comments is not None and comments.kind == CursorKind.RAW_COMMENT:
            print("Comment: ", comments.brief_parsed_comment)
        else:
            print("Comment: None")
        print()

    for child in cursor.get_children():
        extract_functions_and_comments(child, file_name, level + 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_cpp_functions_comments.py <cpp_file>")
        sys.exit(1)

    cpp_file = sys.argv[1]

    Config.set_library_file("/path/to/libclang.so")  # 如果需要，设置libclang库文件的路径
    index = Index.create()
    translation_unit = index.parse(cpp_file, ["-I/usr/include", "-I/usr/local/include"])
    cursor = translation_unit.cursor

    extract_functions_and_comments(cursor, cpp_file)

if __name__ == "__main__":
    main()
