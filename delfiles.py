import os

def remove_files_with_phrase(root_folder, phrase):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            try:
                if phrase.lower() in file.lower():
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Fichier supprimé : {file_path}")
            except PermissionError as e:
                print(f"Je ne peux pas supprimer le fichier '{file}' !")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier '{file}' : {e}")

if __name__ == "__main__":
    root_folder = "assets"
    phrase_to_find = input("Entrez la phrase à rechercher : ")

    if os.path.exists(root_folder) and os.path.isdir(root_folder):
        remove_files_with_phrase(root_folder, phrase_to_find)
    else:
        print(f"Le dossier '{root_folder}' n'existe pas ou n'est pas un répertoire valide.")

    print("Terminé !")