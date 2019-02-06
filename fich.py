import re 
from collections import Counter

DETECT_FICH = re.compile(r'fich-[a-z\-]+?(?:(?=fich)|$|(?=\s))')

with open('Summary of Comments on Survey of the State of the Art in Natural_Language Generation_ Core tasks, applications_and evaluation[2].txt') as f:

    text = f.read()

    fichs = DETECT_FICH.findall(text)

    for ix, cnt in sorted(Counter(fichs).most_common(), key=lambda x: x[0]):

        print(f'[{ix}] -- {cnt}')