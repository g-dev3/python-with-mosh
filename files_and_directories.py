from pathlib import Path

# Absolute path
#  c:\Program files\mic\
# /user/local/bin

# Relational path

# path = Path("email")
# print(path.exists())


# print(path.mkdir())

# print(path.rmdir())

path = Path()

# for file in path.glob('*.py'):
for file in path.glob('*'):
    print(file)