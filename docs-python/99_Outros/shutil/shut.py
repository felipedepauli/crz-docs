import os
import shutil

path = "languages/python/99_Outros/shutil/"

listagem = os.listdir(os.path.join(path, "./documents"))
print("ls:", listagem)

# Eu quero copiar o arquivo 07.txt
source      = os.path.join(path, "./documents/7.txt")
destination = os.path.join(path, "./documents/07.txt") 

# Vamos pegar as informações sobre as permissões desse arquivo
perms = os.stat(source).st_mode
print(perms)

dest = shutil.copy(source, destination)
