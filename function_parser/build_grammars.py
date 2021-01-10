"""
Usage:
    process_calls.py [options] INPUT_DIR DEFINITION_FILE OUTPUT_DIR

Options:
    -h --help
    --language LANGUAGE             Language
    --processes PROCESSES           # of processes to use [default: 16]
    --tree-sitter-build FILE        [default: /src/build/py-tree-sitter-languages.so]
"""
import function_parser

from docopt import docopt
from git import Git, Repo
from tree_sitter import Language

_GRAMMARs = {
    "go": ("https://github.com/tree-sitter/tree-sitter-go.git", "v0.13.3"),
    "java": ("https://github.com/tree-sitter/tree-sitter-java.git", "v0.13.0"),
    "python": ("https://github.com/tree-sitter/tree-sitter-python.git", "v0.14.0"),
}

if __name__ == '__main__':
    args = docopt(__doc__)

    for lang, (url, tag) in _GRAMMARs:
        repo = Repo.clone_from(url, repo_dir)
        g = Git(repo_dir)
        g.checkout('tag_name')
    # repo.commit("tag").checkout()
    # git clone https://github.com/tree-sitter/tree-sitter-python.git
    # cd tree-sitter-python && git checkout tags/v0.14.0 && cd ..

    # git clone https://github.com/tree-sitter/tree-sitter-go.git
    # cd tree-sitter-go && git checkout tags/v0.13.3 && cd ..

    # git clone https://github.com/tree-sitter/tree-sitter-java.git
    # cd tree-sitter-java && git checkout tags/v0.13.0 && cd ..
