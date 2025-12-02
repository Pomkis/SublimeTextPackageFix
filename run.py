import shutil
import os

dest = os.path.expandvars(r"%AppData%\Sublime Text")

for root, dirs, files in os.walk('.'):
	if '.git' in root:
		continue
	
	for file in files:
		if file in ['run.py', '.gitattributes', 'README.md', 'valid.py', 'channel_v3_orig.json']:
			continue
			
		src = os.path.join(root, file)
		rel_path = os.path.relpath(root, '.')
		dst_dir = os.path.join(dest, rel_path)
		dst = os.path.join(dst_dir, file)
		
		os.makedirs(dst_dir, exist_ok=True)
		
		if file.endswith('.sublime-settings'):
			with open(src, 'r', encoding='utf-8') as f:
				text = f.read()
			user = os.environ['USERNAME']
			text = text.replace("USERPROFILE", user)
			with open(dst, 'w', encoding='utf-8') as f:
				f.write(text)
		else:
			shutil.copy2(src, dst)