# Projekt 1 Skapa modell för att förutspå väder.
Försök till att, genom AI, förutspå väder baserat på SMHI:s data för en grid i Borlängeområdet. Koordinater är: 60.489, 15.296 och gäller bara en grid i närheten av Borlänge.
Data hämtad från SMHI: [Griddade nederbörd- och temperaturdata - PTHBV](https://www.smhi.se/data/ladda-ner-data/griddade-nederbord-och-temperaturdata-pthbv)

## Data
Tanken är att förutspå kommande temperatur och nederbörd via lagrad data från detta område.
Data som ska användas är taget från 3 kolumner från grid nämnd ovan: 
- N, E (WGS 84);60.489, 15.296;60.489, 15.296 (är rad nr1 i datasetet innehållande utvalda koordinater)  
Denna rad kommer inte att finnas med in csv filen som modellen ska byggas ifrån. Man hittar det  i originalfilen som ligger under /data: SMHI_pthbv_p_t_2022_2023_daily_4326.csv
### Kolumner vars data används
- (namnlös kolumn innehållande datumstämpel)
- nederbörd [mm] (Nederbörd i mm / h /dag)
- temperatur [°C] (Temperatur i Celcius / h /dag)  

Under skrivande stund innehåller datasetet 681 rader av väderinformation.
Perioden på datainsamlingen är från och med 2022-01-01 till och med {dagens datum - 1}, innehållande information om temp och nederbörd under dygnet.
Senaste väderinsamling är alltid från dagen innan (dvs igår) då data ej har lagrats ännu i databasen hos SMHI.  
Datasetets kolumner innehåller enbart numeriska värden av typen float. Mängd av nederbörd växlar från 0 till olika positiva värden. Däremot skiftar temperaturen mellan negativa och positiva tal. Det ser inte ut att finnas några extrema värden i detta dataset. 
## Utmaning   
Eftersom datat innehåller enbart temperatur och nederbörd blir det svårt att förutsäga väder i sin helhet. Därav behövs det mer data över molntyper och eventuellt molnens rörelsemönster under datainsamlingsperioderna. Om det är molnigt, vilket väder bär molnen på? Typen av nederbörd är en faktor, är det regn eller snö? Hur rör sig molnen, kommer de att påverka det lokala vädret?  
Behöver årstider finnas med i beräkningen och måste då även historisk data över dessa behandlas med tanke på klimatförändringarna?  
Utmaningen i detta är nog den bristande mängden data och avsaknad av alla olika variabler som innefattar väder, tillika med tanke på att perioden sträcker sig från 2022-01-01 till dags dato. Det är en väldigt kort period för att få en någorlunda realistisk gissning på ett väldigt komplext system som väder.
## Tillvägagångssätt  
Med det historiska datat kan modellen tränas som ett regressionsproblem och eftersom data redan finns kommer det att vara supervised learning, i syfte att hitta kommande värden som passar med framtida väderobservationer. 
Till en början ska jag använda datasetet ovan för att träna modellen och om det skulle krävas mer data blir det i nästa steg.
  


