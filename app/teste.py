import folium

lat = -1.4550
lon = -48.5022
mapa = folium.Map(location=[lat, lon], zoom_start=12)
folium.Marker([lat, lon], popup="Belém, Pará", tooltip="Clique para mais informações").add_to(mapa)
mapa.save("mapa.html")
