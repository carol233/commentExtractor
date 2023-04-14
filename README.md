# commentExtractor
要使用Python解析C++并提取函数和注释，您可以使用libclang-python库，它为libclang提供了Python绑定。首先，确保安装了libclang和libclang-python：

# Ubuntu
sudo apt-get install libclang-dev python3-clang

# macOS (using Homebrew)
brew install llvm
pip install clang


接下来，创建一个名为extract_cpp_functions_comments.py的Python文件，然后输入以下代码：

(cpp.py)

请将/path/to/libclang.so替换为您的系统上libclang库文件的实际路径。对于macOS，这可能是/usr/local/opt/llvm/lib/libclang.dylib（如果您使用Homebrew安装了LLVM）。

将C++源文件的路径作为命令行参数运行脚本：

python extract_cpp_functions_comments.py path/to/your/cpp_file.cpp

这将输出提取的C++函数及其所在行号和注释。

