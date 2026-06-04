import os

os.system('git add -A')
os.system('git commit -m "stuff"')
os.system('git push')

os.environ["GX_GITHUB"] = "1"
os.system('mkdocs gh-deploy')
