import os

def remove_files_from_rtf(root_folder, rtf_folder):
    mods_from_rtf = [mod for mod in os.listdir(os.path.join(rtf_folder, "assets")) if os.path.isdir(os.path.join(rtf_folder, "assets", mod))]
    print(f"Mods à supprimer : {mods_from_rtf}")
    
    for root, dirs, files in os.walk(root_folder):
        for dir in dirs:
            for root, dirs, files in os.walk(os.path.join(root_folder, dir)):
                for file in files:
                    try:
                        if file.lower() in ("ru_ru.json", "ru_ru.lang", "ruru.lang") and dir in mods_from_rtf:
                            file_path = os.path.join(root, file)
                            os.remove(file_path)
                            print(f"Fichier supprimé : {file_path}")
                    except PermissionError as e:
                        print(f"Je ne peux pas supprimer le fichier '{file}' !")
                    except Exception as e:
                        print(f"Erreur lors de la suppression du fichier '{file}' : {e}")

if __name__ == "__main__":
    root_folder = "assets"
    rtf_folder = "RTF_v.2.8.0_1.20.x"

    if os.path.exists(root_folder) and os.path.isdir(root_folder) and os.path.exists(rtf_folder) and os.path.isdir(rtf_folder):
        remove_files_from_rtf(root_folder, rtf_folder)
    else:
        print(f"Le dossier '{root_folder}' n'existe pas ou n'est pas un répertoire valide.")

    print("Terminé !")