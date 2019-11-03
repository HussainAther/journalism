https://pubs.usgs.gov/of/2002/0373/ 
README
The digital data and map of
this open-file report are available from thefollowing U.S. Geological
Survey URL: http://wrgis.wr.usgs.gov/open-file/of02-373/Data ContentsThe
digital dataset consists of one file (monterey\_100k.iso) containing
2,385 gravity stations. The file, monterey\_100k.iso, contains the
principal facts of the gravity stations, with one point coded per line.
The format of the data is described below. Each gravity station has a
station name, location (latitude and longitude, NAD27 projection),
elevation, and an observed gravity reading. The data are on the IGSN71
datum and the reference ellipsoid is the Geodetic Reference System 1967
(GRS67). The free-air gravity anomalies were calculated using standard
formulas (Telford and others, 1976). The Bouguer, curvature, and terrain
corrections were applied to the free-air anomaly at each station to
determine the complete Bouguer gravity anomalies at areduction density
of 2.67 g/cc. An isostatic correction was thenapplied to remove the
long-wavelength effect of deep crustal and/orupper mantle masses that
isostatically support regional topography.Offshore bottom-gravity
stations were reduced according to the descriptions in Naval
Postgraduate School theses (Brooks, 1973; Cronyn, 1973; Souto,
1973;Spikes, 1973; Woodson, 1973), after observed gravity values were
placed on the IGSN71 datum and data adjusted for the Geodetic Reference
System 1967. These stations are BROOKS01-BROOKS82, SPIKES02-SPIKES82,
SOUTO01-SOUTO055, W1-W8, and CRONYN01-CRONYN80. Stations with the name
"contour" lack observed gravity information because these locations were
digitized from simple Bouguer gravity contour-trackline intersections
(Chapman and others, 1990) and then reduced to complete Bouguer and
isostatic anomalies. 

EXPLANATION OF PRINCIPAL FACT FORMAT
ItemExplanation
STATION NAME (a8) ................An alphanumeric combination of up to 8 characters used for station identification
LAT(f3.0,f6.3)...................Latitude in degrees and minutes, to 0.01minute
LON (f4.0,f6.3)...................Longitude in degrees and minutes, to 0.01 minute
ELEV (f8.2).......................Elevation, to 0.1 ft
OG (f10.3).........................Observed gravity, to 0.01mGal
FAA (f9.3) .......................Free-air anomaly to 0.01 mGal
SBA(f8.3)........................Simple Bouguer anomaly to 0.01mGal
ITC(f7.3)........................Inner terrain correction for a density of 2.67 g/cc, to 0.01 mGal, followed by a letter denoting the extent of the correction. "Z" indicates computer terrain correction from the station out to 166.7 km with inner terrain correction out to Hayford D zone.
TC(f7.3).........................Total terrain correction from the station to 166.7 km for a density of 2.67 g/cc, to 0.01 mGal.
TC CODE(a1)......................Letter denoting the extent of the correction, according to the Hayford-Bowie template (e.g. 'D' means 590 meters).
CBA(f8.3)........................Complete Bouguer anomaly reduced for a density of 2.67 g/cc, to 0.01 mGal.
ISO(f8.3)........................Isostatic residual anomaly values assuming an Airy model for isostatic compensation of topographic loads. 

This model assumes a a crustal thickness of 25 km, a topographic load density
of 2.67 g/cc, and a density contrast across the base of the model crust
of 0.4 g/cc. Example of format for gravity file61990879 36 30.89 121
52.43 1115.0 979795.58 37.73 -0.29 2.29 9.27 D 8.52 -15.83STATION NAME:
51636676LAT: 36 degrees 30.89 minutes NorthLON: 121 degrees 52.43
minutes WestELEV: 1115.0 feetOG: 979795.58 mGalFAA: 37.73 mGalSBA: -0.29
mGalITC: 2.29 mGalTC: 9.27 mGalTC CODE: D (590 m)CBA: 8.52 mGalISO:
-15.14 mGalBrooks, R.A., 1973, A bottom gravity survey of the shallow
water regions of southern Monterey Bay and its geological
interpretation: Naval Postgraduate School Master's thesis, 90 p.Chapman,
R.H., Chase, G.W., and Youngs, L.G., 1990, Bouguer gravity and magnetic
anomaly map of the Central California continental margin: California
Continental Margin Geologic Map Series Central California Margin Map 5C,
scale 1:250,000.Cronyn, B.S., 1973, Underwater gravity survey of
northern Monterey Bay: Naval Postgraduate School Master's thesis, 53
p.Souto, A.P.D., 1973, A bottom gravity survey of Carmel Bay: Naval
Postgraduate School Master's thesis, 68 p.Spikes, C.H., 1973, A
gravimetric survey of the Santa Cruz-Ano Nuevo Point continental shelf
and adjacent coastline: Naval Postgraduate School Master's thesis, 114
p.Telford, W.M., Geldart, L.O., Sheriff, R.E., and Keyes, D.A., 1976,
AppliedGeophysics: New York, Cambridge University Press, 960 p.Woodson,
W.B., 1973, A bottom gravity survey of the continental shelf
betweenPoint Lobos and Point Sur, California: Naval Postgraduate School
Master's thesis, 110 p.
