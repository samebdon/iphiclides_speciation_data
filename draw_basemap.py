from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

## mamba install python=3.9 anaconda::basemap=1.4.0

def plot_all(ax):
	#basemap without arcgis projection='cass'
	#provide lower left and upper right longitude and latitude
	map = Basemap(llcrnrlon=-10,llcrnrlat=33,urcrnrlon=27,urcrnrlat=45.5,
	             resolution='i', area_thresh=500., epsg=5520, ax=ax)

	map.drawcoastlines()
	map.drawcountries()

	#list of latitudes to plot
	#labels = [left,right,top,bottom]
	parallels = np.arange(34,46,4)
	map.drawparallels(parallels, linewidth = 0, labels=[True,True,False,False], dashes=(None,None))

	#list of longitudes to plot
	#labels = [left,right,top,bottom]
	meridians = np.arange(-6,26,10)
	map.drawmeridians(meridians, linewidth = 0, labels=[False,False,True,True], dashes=(None,None))

	#http://server.arcgisonline.com/arcgis/rest/services
	map.arcgisimage(service='Elevation/World_Hillshade', xpixels = 3000, verbose= True)

	HZ_sample_names = ['1303','1306','1308','1322','1325','1330']
	HZ_sample_latitudes = [42.859, 42.983, 42.954, 43.040,42.986, 43.050]
	HZ_sample_longitudes = [2.702, 2.604, 2.491, 2.042, 2.025, 1.935]

	lons, lats = map(HZ_sample_longitudes, HZ_sample_latitudes)

	for i, n in enumerate(HZ_sample_names):

		if n in ['1322','1325','1330']:
			marker = '^'
		else:
			marker = 'o'
		map.scatter(lons[i], lats[i], marker=marker, color='#FFE500', edgecolor='black')

	IP_sample_names = ['IP_504','IP_502','IP_RVcoll12R048','IP_RVcoll14H960','IP_RVcoll14E561','IP_RVcoll14F754']
	IP_sample_name_latitudes =  [44.25, 43, 39, 45.25, 44, 39.75]
	IP_sample_name_longitudes = [5, 5, 11.5, -2, 20, 20]
	IP_sample_latitudes = [43.805, 43.805, 38.010, 44.626, 45, 38.475]
	IP_sample_longitudes = [3.666, 3.666, 14.74, 2.053, 22.163, 22.517]

	lons, lats = map(IP_sample_longitudes, IP_sample_latitudes)
	text_lons, text_lats = map(IP_sample_name_longitudes, IP_sample_name_latitudes)
	map.scatter(lons, lats, marker='o', color='#008080', edgecolor='black')

	for sample, lon, lat, text_lon, text_lat in zip(IP_sample_names, lons, lats, text_lons, text_lats):
		
		ax.annotate(sample, xy=(lon,lat), 
			xytext=(text_lon, text_lat),
			bbox=dict(facecolor='white'), 
			arrowprops=dict(arrowstyle="-"))

	IF_sample_names = ['IF_234','IF_165','IF_142','IF_236','IF_RVcoll14B411','IF_RVcoll17B439','IF_RVcoll12N508','IF_RVcoll11F366']
	IF_sample_name_latitudes =  [42, 40.5, 40.5, 43, 41, 38, 35.5, 35]
	IF_sample_name_longitudes = [3.75, 3.5, -1.5, -1.5, -10, -6, 6, -4]
	IF_sample_latitudes = [42.330, 41.810, 41.695, 42.330, 40.409, 37.316, 36.764, 34.994]
	IF_sample_longitudes = [2.054, 2.305, 2.356,2.054, -7.490, -3.458, 8.666, -4.832]

	lons, lats = map(IF_sample_longitudes, IF_sample_latitudes)
	text_lons, text_lats = map(IF_sample_name_longitudes, IF_sample_name_latitudes)
	map.scatter(lons, lats, marker='o', color='#800080', edgecolor='black')

	for sample, lon, lat, text_lon, text_lat in zip(IF_sample_names, lons, lats, text_lons, text_lats):
		ax.annotate(sample, xy=(lon,lat), 
			xytext=(text_lon, text_lat),
			bbox=dict(facecolor='white'), 
			arrowprops=dict(arrowstyle="-"))

	map.drawmapscale(-10, 45.5, 0, 0, 200)

def plot_hz(ax):
	#basemap without arcgis projection='cass'
	#provide lower left and upper right longitude and latitude
	map = Basemap(llcrnrlon=0.53,llcrnrlat=42.15,urcrnrlon=5,urcrnrlat=43.85,
	             resolution='i', area_thresh=500., epsg=5520, ax=ax)

	map.drawcoastlines()
	map.drawcountries()

	#list of latitudes to plot
	#labels = [left,right,top,bottom]
	parallels = np.arange(41,45,2)
	map.drawparallels(parallels, linewidth = 0, labels=[True,True,False,False], dashes=(None,None))

	#list of longitudes to plot
	#labels = [left,right,top,bottom]
	meridians = np.arange(-4,7,2)
	map.drawmeridians(meridians, linewidth = 0, labels=[False,False,True,True], dashes=(None,None))

	#http://server.arcgisonline.com/arcgis/rest/services
	map.arcgisimage(service='Elevation/World_Hillshade', xpixels = 3000, verbose= True)

	sample_names = ['1303','1306','1308','1322','1325','1330']
	sample_name_latitudes =  [43, 43.5, 43.5, 43.4, 42.6, 43.1]
	sample_name_longitudes = [3.5, 3, 2.4, 1.5, 2.1, 1]
	sample_latitudes = [42.859, 42.983, 42.954, 43.040,42.986, 43.050]
	sample_longitudes = [2.702, 2.604, 2.491, 2.042, 2.025, 1.935]
	sample_markers = []
	lons, lats = map(sample_longitudes, sample_latitudes)
	text_lons, text_lats = map(sample_name_longitudes, sample_name_latitudes)

	for i, n in enumerate(sample_names):

		if n in ['1322','1325','1330']:
			marker = '^'
		else:
			marker = 'o'

		map.scatter(lons[i], lats[i], marker=marker, color='#FFE500', edgecolor='black')

	for sample, lon, lat, text_lon, text_lat in zip(sample_names, lons, lats, text_lons, text_lats):
		ax.annotate(sample, xy=(lon,lat), 
			xytext=(text_lon, text_lat), 
			bbox=dict(facecolor='white'), 
			arrowprops=dict(arrowstyle="-"))

	map.drawmapscale(0.8, 43.6, 0, 0, 20)

fig, axs = plt.subplots(nrows=2, figsize=[10,10])
all_ax = axs[0]
hz_ax = axs[1]

all_ax.set_title('A', loc='left')
hz_ax.set_title('B', loc='left')

plot_all(all_ax)
plot_hz(hz_ax)

plt.tight_layout()

plt.savefig('basemap_comp.png', dpi=200)
plt.savefig('basemap_comp.pdf')
plt.close()
