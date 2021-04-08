# instalar biblioteca
# pip install folium

import folium

# Para criar um mapa básico, basta passar suas coordenadas iniciais para o Folium:
map_sp = folium.Map(location=[-23.5489, -46.6388])

# para salvá-lo em um arquivo,
map_sp.save('sao_paulo.html')