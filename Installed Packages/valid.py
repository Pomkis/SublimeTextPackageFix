import json
import re
import os

if not os.path.exists('channel_v3_orig.json'):
	if os.path.exists('channel_v3.json'):
		os.rename('channel_v3.json', 'channel_v3_orig.json')

with open('channel_v3_orig.json', 'r', encoding='utf-8') as f:
	content = f.read()

cleaned_content = re.sub(r'https://web\.archive\.org/web/\d+/', '', content)

with open('channel_v3.json', 'w', encoding='utf-8') as f:
	f.write(cleaned_content)