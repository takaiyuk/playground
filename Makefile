.PHONY: gitignore

gitignore:
	curl -s -w'\n' https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore >> .gitignore \
	&& curl -s -w'\n' https://raw.githubusercontent.com/github/gitignore/main/Go.gitignore >> .gitignore \
	&& curl -s -w'\n' https://raw.githubusercontent.com/github/gitignore/main/Rust.gitignore >> .gitignore
