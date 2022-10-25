import os

IMAGE_PATH = 'image.png'
IMAGE_RESIZED = 'image-resized.png'
IMAGE_GRAY = 'image-gray.png'
IMAGE_THRESH = 'image-thresh.png'
IMAGE_DISPLAYED = 'image-displayed.png'

USERLIST = []
with open(os.path.join('usernames.txt')) as f:
    for line in f:
        username = line.strip()
        USERLIST.append(username)

SCORES = ['1-1-1', '2-1-1', '2-1-2', '2-1-3']
for i in range(0, 15):
    for j in range(0, 15):
        SCORES.append(f'{i}-{j}')

VALID_SCORES = ('2-0', '2-1', '1-2', '0-2', '1-0', '0-1')
VALID_SCORES_SPLIT = tuple(tuple(s.split('-')) for s in VALID_SCORES)
SCORE_REPLACE = [('Z', '2'), ('Q', '0'), ('_', '-'), ('L', '1'),
                 ('_', '-'), ('4', '-1'), ('-.', '-')]
