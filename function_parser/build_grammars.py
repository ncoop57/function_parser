import function_parser

from git import Git, Repo
from pathlib import Path
from tree_sitter import Language

_GRAMMARs = {
    "go": ("https://github.com/tree-sitter/tree-sitter-go.git", "tree-sitter-go", "v0.13.3"),
    "java": ("https://github.com/tree-sitter/tree-sitter-java.git", "tree-sitter-java", "v0.13.0"),
    "python": ("https://github.com/tree-sitter/tree-sitter-python.git", "tree-sitter-python", "v0.14.0"),
}

# if __name__ == '__main__':
def main():
    languages = []
    for lang, (url, dir, tag) in _GRAMMARs.items():
        repo_dir = Path(function_parser.__path__[0])/dir
        if not repo_dir.exists():
            repo = Repo.clone_from(url, repo_dir)
        g = Git(str(repo_dir))
        g.checkout(tag)
        languages.append(str(repo_dir))
    
    Language.build_library(
        # Store the library in the directory
        str(Path(function_parser.__path__[0])/"tree-sitter-languages.so"),
        # Include one or more languages
        languages
    )
