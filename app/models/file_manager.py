import os
import shutil
import datetime

class FileManager:
    def list_files(self, folder_path, filter_text=None):
        if not folder_path or not os.path.exists(folder_path):
            return []
        
        try:
            files_data = []
            for f in os.listdir(folder_path):
                full_path = os.path.join(folder_path, f)
                if not os.path.isfile(full_path):
                    continue
                
                if filter_text and filter_text.lower() not in f.lower():
                    continue

                size = os.path.getsize(full_path)
                ts = os.path.getmtime(full_path)
                ext = os.path.splitext(f)[1].upper().replace('.', '') or "File"
                
                files_data.append({
                    'name': f,
                    'path': full_path,
                    'size': size,
                    'timestamp': ts,
                    'extension': ext
                })
            return files_data
        except Exception as e:
            raise e

    def rename_files(self, folder_path, old_text, new_text):
        count = 0
        if not folder_path or not old_text:
            return count

        for f in os.listdir(folder_path):
            if old_text in f:
                old_path = os.path.join(folder_path, f)
                new_name = f.replace(old_text, new_text)
                new_path = os.path.join(folder_path, new_name)
                try:
                    os.rename(old_path, new_path)
                    count += 1
                except Exception:
                    pass
        return count

    def copy_and_rename_files(self, folder_path, old_text, new_text):
        count = 0
        if not folder_path or not old_text:
            return count

        for f in os.listdir(folder_path):
            if old_text in f:
                old_path = os.path.join(folder_path, f)
                new_name = f.replace(old_text, new_text)
                new_path = os.path.join(folder_path, new_name)
                try:
                    shutil.copy(old_path, new_path)
                    count += 1
                except Exception:
                    pass
        return count

    def delete_files(self, folder_path, match_text):
        count = 0
        deleted_files = []
        if not folder_path or not match_text:
            return count, deleted_files

        to_delete = [f for f in os.listdir(folder_path) 
                     if match_text.lower() in f.lower() and 
                     os.path.isfile(os.path.join(folder_path, f))]
        
        for f in to_delete:
            try:
                os.remove(os.path.join(folder_path, f))
                deleted_files.append(f)
                count += 1
            except:
                pass
        return count, deleted_files

    def get_files_to_delete(self, folder_path, match_text):
        if not folder_path or not match_text:
            return []
        return [f for f in os.listdir(folder_path) 
                if match_text.lower() in f.lower() and 
                os.path.isfile(os.path.join(folder_path, f))]
