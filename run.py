import shutil
import os

dest = os.path.expandvars(r"%AppData%\Sublime Text")
user = os.environ['USERNAME']

for root, dirs, files in os.walk('.'):
	if '.git' in root:
		continue
		
	for file in files:
		if file in ['run.py', '.gitattributes']:
			continue
			
		src = os.path.join(root, file)
		dst = os.path.join(dest, root, file)
		
		os.makedirs(os.path.dirname(dst), exist_ok=True)
		
		if file.endswith('.sublime-settings'):
			with open(src, 'r') as f:
				text = f.read()
			text = text.replace("USERPROFILE", user)
			with open(dst, 'w') as f:
				f.write(text)
		else:
			shutil.copy2(src, dst)