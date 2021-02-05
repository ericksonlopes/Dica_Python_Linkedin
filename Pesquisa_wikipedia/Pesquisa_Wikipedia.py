# pip install wikipedia

import wikipedia

wikipedia.set_lang('pt')

info = wikipedia.summary('Ayrton Senna')

print(info)
