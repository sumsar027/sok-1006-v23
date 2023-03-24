#!/usr/bin/env python
# coding: utf-8

# In[5]:


# importerer ulike pakker
import json
import pandas as pd
import requests
from pyjstat import pyjstat
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from matplotlib.patches import Polygon
import sympy as sp


# In[77]:


# henter inn datasett for total andel konsum
postUrl = "https://data.ssb.no/api/v0/no/table/10638"

apiQuery = {
  "query": [
    {
      "code": "KonsumInnd",
      "selection": {
        "filter": "item",
        "values": [
          "UTLK",
          "NOHT",
          "NONF"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Priser"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "2020"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

def apiToDataframe(postUrl, query):

    # postUrl som spørringen skal postes mot
    # Spørringen og endepunktet til API-et kan hentes fra Statistikkbanken.

    res = requests.post(postUrl, json=query)
    # legger resultat i ds. DS har i tillegg en del metadata
    ds = pyjstat.Dataset.read(res.text)
    # skriver resultatet til to dataframes
    # først dataframe med tekst
    df = ds.write('dataframe')
    # deretter dataframe med koder
    df_id = ds.write('dataframe', naming='id')
    # returnerer også ds i tilfelle en trenger metadata
    return df, df_id, ds

df, df_id, ds = apiToDataframe(postUrl, apiQuery)


# In[78]:


# lager plot for total andel konsum
fig1 = px.pie(df, values='value', names='konsumentgruppe')


# In[79]:


# henter inn datasett for resiemåter 
postUrl = "https://data.ssb.no/api/v0/no/table/10638"

apiQuery ={
  "query": [
    {
      "code": "Reiseliv",
      "selection": {
        "filter": "item",
        "values": [
          "01.03",
          "01.04",
          "01.05",
          "01.06"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Priser"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "2020"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

def apiToDataframe(postUrl, query):

    # postUrl som spørringen skal postes mot
    # Spørringen og endepunktet til API-et kan hentes fra Statistikkbanken.

    res1 = requests.post(postUrl, json=query)
    # legger resultat i ds. DS har i tillegg en del metadata
    ds1 = pyjstat.Dataset.read(res1.text)
    # skriver resultatet til to dataframes
    # først dataframe med tekst
    df1 = ds1.write('dataframe')
    # deretter dataframe med koder
    df_id1 = ds1.write('dataframe', naming='id')
    # returnerer også ds i tilfelle en trenger metadata
    return df1, df_id1, ds1

df1, df_id1, ds1 = apiToDataframe(postUrl, apiQuery)


# In[80]:


# lager plot for reisemåter
fig2 = px.pie(df1, values='value', names='reiselivsnæring')


# In[81]:


# henter inn datasett for hotel 
postUrl = "https://data.ssb.no/api/v0/no/table/10638"

apiQuery2 ={
  "query": [
    {
      "code": "Reiseliv",
      "selection": {
        "filter": "item",
        "values": [
          "01.01"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Priser"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "2017",
          "2018",
          "2019",
          "2020"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

def apiToDataframe(postUrl, query2):

    # postUrl som spørringen skal postes mot
    # Spørringen og endepunktet til API-et kan hentes fra Statistikkbanken.

    res2 = requests.post(postUrl, json=query2)
    # legger resultat i ds. DS har i tillegg en del metadata
    ds2 = pyjstat.Dataset.read(res2.text)
    # skriver resultatet til to dataframes
    # først dataframe med tekst
    df2 = ds2.write('dataframe')
    # deretter dataframe med koder
    df_id2 = ds2.write('dataframe', naming='id')
    # returnerer også ds i tilfelle en trenger metadata
    return df2, df_id2, ds2

df2, df_id2, ds2 = apiToDataframe(postUrl, apiQuery2)


# # <center> MAPPEOPPGAVE 1
# ### <center> Kandidatnummer: 8
# 
# ### Innholdsfortegnelse:
# 
# 1.	Innledning
# 
# 2.	Turistnæringen i Norge
# 
# 3.	Samfunnsøkonomiske effekter av turistskatt
# 
# 4. Konklusjon og oppsummering av resultater
# 
# ## <center> Innledning
#     
# #### Samfunnsøkonomi er faget om hvordan økonomien til verden fungerer, og hvordan ulike faktorer påvirker økonomien. Denne teksten har som formål å sette søkelys på ulike faktorer innen turisme i Norge, mer spesifikt handler det om kunngjøringen fra Nærings- og fiskeridepartementet i januar 2023. Kunngjøringen går ut på at den norske regjeringen vil gi ulike kommuner muligheten til å innføre et besøksbidrag, dette vil si en turistskatt der ulike overnattingssteder må kreve inn denne skatten fra per besøkende per overnatting. Teksten skal se på ulike faktorer som kan bli påvirket av en slik ordning og se på ulike markedseksempler. Skatt er alltid noe man må være presis med siden økonomien henger sammen med hver minste detalj og kan føre til enten positive, negative eller nøytrale effekter på økonomien. Skatten eller besøksbidraget skal fungere gjennom en handlingsplan der de har ulike pilotprosjekter som de bruker for å teste hvordan en turistskatt hadde fungert, skatten skal fremme næringen med bedre lønnsomhet, mer bærekraftighet og mer konkurransedyktighet. Men en ny skatt kan være vanskelig å få til på riktig måte, det er mange faktorer som kan gå feil og ha en motsatt virkning på næringen, man må nøye se på mange perspektiver innen økonomien for å finne ut den mest optimale løsningen. 
# 
# ### Hva er begrunnelsen for en slik ordning?
# 
# #### Det denne ordningen kommer av ifølge næringsministeren, er at et besøksbidrag vil føre til en mer bærekraftig og helårlig reiselivsnæring. Dette sitatet begrunner noe mer; «Norske reisemål inneholder en rekke fellesgoder som ikke tilfaller en enkelt næringsaktør, men som er av betydning for reisemålets attraksjonsverdi for gjestene. Dermed har de også betydning for bedriftenes kundegrunnlag og omsetning.» 
#     
# #### Formålet med en slik turistskatt som staten snakker om er å sette en ekstra kostnad for turister, denne kostnaden er ekstra inntekter for ulike kommuner. Dette vil bidra til å opprettholde ulike offentlige tjenester og infrastruktur, disse godene blir brukt av beboere, men også turister som fører til slitasje og opprettholdelses kostnader, eksempler på slike goder kan være offentlige parker, offentlige attraksjoner, veier osv. Det er kommunen selv som må betale kostnadene, men en slik turistskatt som vi snakker om vil føre til at det blir mindre belastning på kommunen sin økonomi, den ekstra inntekten kan også brukes til å få generelt bedre offentlige goder som alle kan få noe ut av, men mest for at turistnæringen skal utvikle seg og bli en mer bærekraftig næring. Turistskatt kan også brukes som en reguleringsfunksjon som regulerer den totale andelen turister, hvis man innfører turistskatt i en svært ofte besøkt kommune vil det føre til at konsumenter med lav betalingsvillighet vil velge et annet sted enn den gjeldene kommunen, dette betyr at den totale andelen tursiter vil synke og belastningen på kommunen vil bli lettere. En økt pris per overnatting er noe hotelaktører er bekymret for siden de ikke vil miste kunder, det kan bli en sterk vekst i konkurranse blant aktørene og de fleste må forvente en negativ effekt på ulike faktorer som salg, inntekt, arbeidsforhold osv. 
# 
# ### Hvordan har en turistskatt fungert andre steder?
# 
# #### «I land som Nederland, Italia, Frankrike, Tyskland, Spania, Østerrike, Belgia, Hellas, Ungarn, Portugal, Romania, Slovenia, Bulgaria, Kroatia og Sveits er dette allerede innført.» , ifølge Stortinget har disse landende innført turistskatt på grunn av en økende turisme som gir negative konsekvenser for økonomien og samfunnet generelt. Disse konsekvensene kan for eksempel være for store mengder med tursiter på et sted, kostnader på slitasje av fellesgoder som blir brukt av turistene, finansiering av infrastruktur og tjenester og miljøeffekter av turisme. Disse eksemplene er alle gode grunner til å innføre en turistskatt som kan være behjelpelig med slike problemer, det viser også at turisme er et økende problem for mange land og turistskatt har vært en løsning som har fungert bra for noen av dem. Skatten skal gi en ekstra inntekt til kommunen slik at ulike belastninger og slitasje får dekket kostnadene, inntekten kan også brukes til å utvikle og forbedre ulike offentlige goder og turistnæringen generelt. Problemet med en slik turistskatt kan være konsekvenser på den gjeldene turismen hvis man ikke utfører det på riktig måte, en andel av turistene kan velge å dra andre steder istedenfor slik at det fører til en økt turistbelastning andre steder, det kan også føre til mindre turister generelt på grunn av den økte prisen som kan være svært negativt for ulike aktører innenfor turistnæringen. Turistskatt er et sensitivt tema på grunn av at turisme er et eksklusivt gode og når prisen øker kan det få store utfall i ulike faktorer, men turistskatt kan være en bra løsning på ulike problemer hvis det blir gjort på riktig måte.
#     
# #### Oppgaven er bygget opp av fire kapitler med innledning, turistnæringen i Norge, samfunnsøkonomiske effekter og konklusjon. Vi skal gjennom teksten få en god forståelse av Norges turistnæring og hvordan denne er bygd opp, deretter skal vi se på hvordan effekter av en turistskatt påvirker næringen på flere forskjellige måter. Til slutt kommer vi med en konklusjon som sier noe om en turistskatt er et positivt tak eller ikke. 
#     
# # <center> Turistnæringen i Norge
# 
# #### I oppgaven blir det brukt data fra SSB sin statistikk, desverre er det bare data for 2020 og før som gjør at vi ikke kan si noe om de nylige årene. Men vi kan fremdeles se på de tidligere årene og få kunnskap fra disse, 2020 var året corona startet og dette har ført til store forskjeller i det året som fører til data som viser en stor nedgang i 2020 blant de fleste faktorer. Turistnæringen er ikke et sterkt tema for Norge, det meste av turismen skjer på grunn av den fine naturen og opplevelser rundt om i Norge men kan ikke sammenlignes med turistnæringen i andre land som har turistnæring som et av hovedtemaene i nasjonaløkonomien. Norge har andre faktorer som gir oss god inntekt og en stabil økonomi, turisme er kjent for å være ustabilt og er vanskelig å utvikle tilbud hvis for eksempel turismen er sesongbasert. I Norge er turismen svært sesongbasert og uforutsigbar siden de fleste som kommer til Norge vil oppleve naturen, et eksempel på dette kan være nordlys som man ikke har noe garanti på, dette gjør at turistnæringen kan være vanskelig å håndtere. 
#     
# #### Turistnæringen bidrar til økonomisk vekst i hele Norge og er en del av den helhetlige norske økonomien. Turistnæringen er kanskje liten i Norge men den skaper fremdeles arbeidsplasser og økonomisk vekst, eksempler på dette kan være overnattingssteder, transportmuligheter, serveringsmuligheter og ulike reisebyrå som planlegger og gir muligheten til turisme. Det er disse faktorene og mange fler som får utnyttelse av turismen.  
# 
# #### I figur 1 kan vi se fordeling av total konsum av turistfaktorer, plottet viser oss "Norske husholdningers turistkonsum i Norge" (BLÅ), "Utlendingenes konsum i Norge" (Rød) og "Norske næringers utgifter til forretningsreiser i Norge" (GRØNN). Vi kan tydelig se at turistnæringen får sitt konsum i størst andel av den Norske befolkningen på 74% ikke folk fra utlandet, utlendingenes konsum er betydelig mindre og består 14.7% av den totale konsum av tursitnæring. Dette betyr at den Norske befolkningen er svært viktig når det gjelder turistnæringen som igjen betyr at ulike endringer på turistnæringen vil påvirke den norske befolkningen mest. Vi kan se at den grønne delen for forretningsreiser i Norge har nesten en like stor andel som utlendingers konsum, de har en andel på 11.3% som betyr at store mengder av turistnæringen får inntekt og konsum fra forretningsreiser. Hvilke grupper av konsumentene er viktig å se på for å finne ut hvem som kommer til å bli påvirket av endringer i pris. 

# In[11]:


fig1.show()


# #### Hvis vi ser på fordelingen for reisemåte i figur 2, får vi at de fleste kommer til med fly med en andel på 63.9%, så kommer transport med skip og ferger med en andel på 18.4%, resten bruker transport med buss, dorsje og jernbane. Fly er nok den enkleste reisemåten til, fra og innad i Norge, dette kan være grunnen til at flytransport er den mest brukte. Transport er en viktig faktor i økonomien siden den er grunnleggende for alle som bor i Norge og alle som er på besøk i Norge, vi kan tydelig se at fly er mest brukt og fly er også det mest forrurensende av transportmåtene. Hvis vi sammenligner fly med jernbanetransport kan vi se at jernbanetranporten er på 5.29% sammenliknet med fly på 63.9%, tydelig kan vi se at transportmåter er noe som må bli tatt hånd om for en mer bærekraftig og miljøvennlig turistnæring. Andelen med transpory av skip og ferger er på 18.4%, denne reisemåten er også svært forrurensende og er blitt godt omdiskutert siden de blir brukt ofte og kjører langs norskekysten konstant. 

# In[12]:


fig2.show()


# #### Hotel og overnattingstjenester er der turistskatten faktisk blir implementert og er de som kommer til å se en tydelig forskjell i pristilbudene de har. Hvis vi ser på hvordan hotelnæringen har utviklet seg over tid får vi at utviklingen hadde en jevn og positiv gang men i 2020 har den en sterk nedgang. Nedgangen kommer mest sannsynlig av Corona-pandemien som startet samme år. Men før pandemi året kan man se en konstant positiv utvikling som betyr at turistnæringen var på god vei før corona pandemien, denne positive utviklingen er noe man må hente opp igjen etter skadene fra pandemi året, en turistskatt er noe som kan utfordre en slik positiv utvikling enten for noe bedre eller dårligere. Det har også blitt mer vanlig å bruke AirBNB løsninger istedenfor hotel overnattinger, dette øker markedskonkurransen blant aktørene og kan gjøre markedet enda mer utfordrene. En turistskatt som det er snakk om her kommer ikke til å bli innført i AirBNB overnattinger, dette gjør at hotelnæringen kan bli svært utsatt i forhold til andre aktører som AirBNB. 

# In[13]:


# lager plot for reisemåter
fig3 = df2.plot.bar(xlabel = 'År fra 2017-2020', ylabel= 'Konsum', color='green', title='Hotel konsum over tid')


# In[31]:


# henter inn datasett for total andel konsum
postUrl = "https://data.ssb.no/api/v0/no/table/10603/"

apiQuery = {
  "query": [
    {
      "code": "HovedstReise",
      "selection": {
        "filter": "item",
        "values": [
          "BPROD"
        ]
      }
    },
    {
      "code": "Reiseliv",
      "selection": {
        "filter": "item",
        "values": [
          "OTV",
          "SEV",
          "UTL",
          "RBAV",
          "KUV",
          "SAF"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "LopPriser"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "2016",
          "2017",
          "2018",
          "2019",
          "2020",
          "2021"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

def apiToDataframe(postUrl, query):

    # postUrl som spørringen skal postes mot
    # Spørringen og endepunktet til API-et kan hentes fra Statistikkbanken.

    res = requests.post(postUrl, json=query)
    # legger resultat i ds. DS har i tillegg en del metadata
    ds = pyjstat.Dataset.read(res.text)
    # skriver resultatet til to dataframes
    # først dataframe med tekst
    df = ds.write('dataframe')
    # deretter dataframe med koder
    df_id = ds.write('dataframe', naming='id')
    # returnerer også ds i tilfelle en trenger metadata
    return df, df_id, ds

df, df_id, ds = apiToDataframe(postUrl, apiQuery)

df.drop(columns = ['hovedstørrelse', 'statistikkvariabel'])

fig3 = px.pie(df, values='value', names='reiselivsnæring')


# #### Under kan man se en visning av de forskjellige næringene som blir påvirket av turisme. Serveringsvirksomhet tar den største delen på hele 34.7% og utleie- og leasingsvirksomhet har en andel på 24.1%, disse næringene bruker turister effektivt og godt for å få optimal økonomi som betyr at en endring i turisme vil få endringer mange andre steder enn bare turisme. Alle disse næringene som er vist under vil kjenne på endringer i markedet. Det er viktig å ikke bare se på en næring, men man må se på det store bildet for å få en forståelse om hva og hvordan økonomien blir påvirket. 

# In[32]:


fig3


# # <center> Samfunnsøkonomiske effekter av turistskatt
#     
# #### For å kunne se effektene av en turistskatt må vi først se på hvordan økonomien er uten en slik skatt. Uten en slik turistskatt som det er snakk om her ville turistøkonomien i Norge vært et fritt marked hvor tilbud og etterspørsel og andre grunnleggende faktorer som beliggenhet, når på året, hva man har å tilby og ulik konkurranse i nærområdet bestemmer det meste av priser. De vanlige kostnadene som man har i hvilken som helst bedriftsøkonomi vil også være med på å påvirke prisen per overnatting. For kommunen sin del vil de være ansvarlige for ulike vedlikeholdskostnader og det er dette som er hovedtemaet når det gjelder en turistskatt. Men en turistskatt vil påvirke pris per overnatting betraktelig for besøkende, spesielt kan etterspørselen bli påvirket siden det kan bli for dyrt for ulike konsumentgrupper som gjør at turistnæringen kan miste konsumenter. Dette kan føre til en sterkere konkurranse om konsumentene blant ulike bedrifter. Vi skal se nærmere på forholdene mellom etterspørsel og tilbud i økonomien, vi antar at det er fullkommen konkurranse, det er viktig å se på disse faktorene siden etterspørselen forklarer hvor mye som blir ønsket kjøpt av godet, mens tilbudet forklarer hvor mye som er produsert som man kan konsumere.  
# 
# #### De ulike forventningene etter en innføring av turistskatt vil tenkes å være:
# 
# - Økning i pris
# - Svekket etterspørsel 
# - Økt inntekt for kommunen 
# - Reduksjon i antall overnattinger
# - Redusert inntekt for lokale aktører 
#     
# #### Etterspørselen til en konsument er viktig å se på siden det er konsumentene som bruker penger og konsumerer tilbud. Uten dette hadde det ikke vært noe marked som man kan oppnå økonomisk vekst i, vi må se på etterspørselen for å få en forståelse av dens rolle i økonomien. Tilbudet er på den andre siden de som gir noe man kan konsumere, uten disse hadde det ikke vært noe man kunne kjøpe og bruke pengene sine på. Samspillet mellom disse to faktorene er helt grunnleggende i samfunnsøkonomien og brukes til å se påvirkninger av endringer og for å få en forståelse av markedet generelt. Markedsetterspørselen og markedstilbudet kan beskrives slik matemastisk: 
# 
# ### Markedsetterspørsel:
# $$ 
# X^D = D(p)
# $$
# 
# ### Markedstilbud:
# $$
# X^S = S(p-t)
# $$ 
#     
# #### Etterspørselen viser etterspørsel etter et gode, i dette tilfelle hotelovernatting, og hvor mye konsumenten ønsker å kjøpe av godet. Andre priser og inntekten må holdes kosntant for å se etterspørselen for spesifkt denne etterspørslen. Helningen på etterspørselen er lik (1/den deriverte til etterspørselslikningen). Dette kan da forklares med markedsetterspørsels formelen som viser pris per enhet (p) og konsumentens etterspørsel ettter godet i markedet X^D. Etterspørselens linje er fallende og dette betyr at når prisen faller vil konsumenten ha mulighet til å kjøpe mer av godet og omvendt, dette er loven om den fallende etterspørsel. Markedstilbudet handler om S (supply) istendenfor D (demand), tusitskatten blir vist frem her som t. Vanligvis ser man på etterspørsel og tilbud fra flere forskjellige, dette kommer av at det er mange konsumenter og mange tilbudere som har forskjellige tilbud og betalingsvillighet, tilbudslinjen viser til marginalkostnadene for hotel overnattinger. I grafen under kan man se grafen til etterspørsel (oransje) og tilbud (blå). Dette viser hordan etterspørsel og tilbud fungerer, man kan se at etterspørselen har en fallende gang mens tilbud har en økende gang. Tilbudet har en økende gang på grunn av at når prisen øker vil aktørene ha mulighet til å produsere flere enheter av godet. 
# 
# #### Markedslikevekt viser sammenhengen mellom markedstilbud og markedsetterspørsel, helt konkret viser det hvor tilbudet av et gode møter konsumentens etterspørsel helt perfekt slik at det ikke blir noe overskudd eller underskudd. Dette kan vises i en graf som i figuren under. Her er tilbudet i økende gang og etterspørsel i synkende gang, dette blir vist i et pris-mengde diagram. Der tilbud og etterspørsel krysser viser likevekten, uten en turistskatt vil økonomien ha en verdi veldig nærme likevekten siden de har gjennom mange år og erfaringer greid å optimalisere tilbudet i forhold til etterspørselen. Antall hotel og pris samsvarer med antall turister og deres betalingsvillighet. Men etterspørselen og tilbudet kan endre seg siden forskjellige faktorer kan bli påvirket av ulike endringer, et eksempel på dette kan være corona-pandemien som gjorde at totale hotelovernattinger sank drastisk i 2020 som vist tidligere. Hvis det ikke er likevekt kan det enten være etterspørselsoverskudd eller tilbudsoverskudd i markedet.
# 

# In[33]:


import matplotlib.pyplot as plt
  
# x axis values
x1 = [1,2,3,4,5,6, 7, 8, 9, 10]
# corresponding y axis values
y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# corresponding y axis values
y2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# plotting the points 

plt.plot(x1, y1, label='Tilbud')
plt.plot(x1, y2, label='Etterspørsel')
# setting x and y axis range
plt.ylim(1,10)
plt.xlim(1,10)

plt.axhline(y = 5.5444, xmin = 0, xmax = 0.5, linestyle = 'dashed', color='k')
plt.axvline(x = 5.5444, ymin = 0, ymax = 0.5, linestyle = 'dashed', color='k')
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# fjerner x og y verdier
plt.xticks([])
plt.yticks([])

# giving a title to my graph
plt.title('Likevekt mellom Etterspørsel og Tilbud')

plt.legend()
# function to show the plot
plt.show()


# ### Hvordan funker markedslikevekt med en innføring av turistskatt?
# 
# #### En endring i pris per overnatting som kommer av en innføring av turistskatt vil vi få et venstreskift i tilbudet, dette kan vises i grafen under. Vi kan da se at den oprinnelige markedslikevekten blir flyttet til venstre med en høyere prisverdi og en lavre kvantumsverdi, dette kommer av at prisen øker etter en turistskatt og når en pris øker vil etterspørselen synke på grunn av konsumentgrupper med lav betalingsvillighet vil velge bort godet mot noe annet. En turistskatt som vi snakker om her vil påvirke konsumenten direkte siden det er de som skal betale skatten ikke aktørene, dette gjør at størrelsen på andelen skatt vil påvirke konsumentene drastisk. 

# In[34]:


# definer symbolene som vi kommer til å bruke
x,p,t,a,b,A,B=sp.symbols('x p t a b A B', positive=True, real=True)

# Etterspørsel

def x_d(p,a,b, t):
    return a - b*(p-t)

#Tilbud

def x_s(p,A,B):
    return -A+B*(p)

likev=sp.Eq(x_d(p,a,b,t),x_s(p,A,B))
likev


# #### Dette viser da likevektsbetingelsen for et generelt eksempel med turistskatt, turistskatten blir tydelig vist med t som blir trukket fra prisen. 

# In[35]:


eq_d=sp.Eq(x,x_d(p,a,b, t))
eq_s=sp.Eq(x,x_s(p,A,B))

sol_dict=sp.solve ((eq_d, eq_s), (p,x))

# likevektsbetingelse for x kvantum og p pris
print('Pris:')
display(sol_dict[p])
print('Kvantum:')
display(sol_dict[x])


# #### Her kan vi se likevektsbetingelsen løsningen for p pris og x kvantum
# 
# #### Total skatteproveny kan vises slik:

# In[36]:


# total proveny
proveny = sp.lambdify((a,b,A,B,t), t*sol_dict[x])
print('Proveny:')
proveny(a,b,A,B,t)


# #### Vanligvis ser man på fordelingen av hvem som betaler skatten, er det konsumentene eller er det aktørene. I dette tilfelle er turistskatten pålagt at konsumentene betaler den, det betyr da at tilbudet endrer seg i form av pris men skatten blir direkte betalt av konsumenten som en andel av prisen. 
# 
# #### Grafen under viser oss et venstreskift i tilbudslinjen med markerte områder, områdene som er markerte viser ulike verdier på faktorer etter en endring. Etterspørselsoverskudd defineres som en situasjon der prisen er lavere enn likevektsprisen, dette betyr at konsumentene er villige til å etterspørre mer enn det aktørene er villige til å tilby, dette vises som det konsumenten må betale trukket fra betalingsvilligheten. Produsentsoverskudd kan defineres som en situasjon der prisen er høyere enn likevektsprisen, her tilbyr aktørene mer enn det konsumentene etterspør, dette vises som marginalkostnaden til aktøren truket fra den prisen aktøren får . Disse to faktorene skjer hvis det ikke er likevekt i markedet. Skatteproveny er de inntektene kommunen får, aktøren betaler dette til kommunen mens konsumenten får en høyere pris dette kan vises i det røde markerte område som funker som et skille mellom KO og PO. Man kan tydelig se skiftet i tilbudet, når overskuddet fra produsentene og konsumentene er optimalisert vil mam få størt velferd fra dette, dette oppstår når den marginale betalingsvilligheten er lik grensekostnadene som man kan se i krysspunktet mellom x1 og y1 (uten skatt), men markedslikevekten med turistskatt blir vist i punktet x2, y2. Man kan her se en tydelig forflytning og det er her man kan se effektene av turistskatten. Dødvektstap er det som viser en ineffektiv del av markedsskjemaet, dette viser hva man mister av produskjon og salg etter skatten. Det samfunnsøkonomiske overskuddet kan man finne ut av å plusse sammen KO og PO, vi kan se at dette overskuddet blir mindre med den nye skatten som betyr at det blir lite samfunnsøkonomisk effektivt. 

# In[69]:


import matplotlib.pyplot as plt
  
# lager linje verdier 
x1 = [1,2,3,4,5,6, 7, 8, 9, 10]
y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
y3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# plotter de forskjellige linje verdiene 
plt.plot(x1, y1, label='Tilbud')
plt.plot(x1, y2, label='Etterspørsel')
plt.plot(x1, y3, label='Tilbud etter skatt')

# setter x og y limit
plt.ylim(1,10)
plt.xlim(1,10)

# lager ulike visningslinjer
plt.axhline(y = 5.5444, xmin = 0, xmax = 0.5, linestyle = 'dashed', color='k')
plt.axvline(x = 5.5444, ymin = 0, ymax = 0.5, linestyle = 'dashed', color='k')
plt.axhline(y = 6, xmin = 0, xmax = 0.45, linestyle = 'dashed', color='k')
plt.axvline(x = 5, ymin = 0, ymax = 0.55, linestyle = 'dashed', color= 'k')

x = np.linspace(1, 10)

# lager ulike markerte områder
rectangle = plt.Rectangle((0,5),5, 1, fc='red', alpha = 0.3, label = 'Skatteproveny')
plt.gca().add_patch(rectangle)

pts = np.array([[0,6], [0,11], [5,6]])
p = Polygon(pts, alpha = 0.3, label = 'konsumentoverskudd')
plt.gca().add_patch(p)

pts1 = np.array([[0,0], [0,5], [5,5]])
p1 = Polygon(pts1, alpha = 0.3, label = 'produsentoverskudd', color = 'green')
plt.gca().add_patch(p1)

pts2 = np.array([[5,5], [5.5,5.5], [5,6]])
p1 = Polygon(pts2, alpha = 0.3, label = 'dødvektstap', color = 'yellow')
plt.gca().add_patch(p1)

# lager pil for å vise endring 
plt.arrow(7,7.1,0,0.4,width=0.1)

# lager punkt tekst 
plt.text(5, 6, 'Skatt')
plt.text(5.5444, 5.5, 'Uten Skatt')
plt.text(5.5844, 1, 'x1')
plt.text(5, 1, 'x2')
plt.text(1, 6.2, 'y2')
plt.text(1, 5.5844, 'y1')


# setter navn til aksene
plt.xlabel('kvantum')
plt.ylabel('pris')
  
# setter tittel 
plt.title('Likevekt mellom Etterspørsel og Tilbud')

plt.legend()
plt.show()


# #### Men hva er det som avgjør hvor store effekter man får av en slik endring, jo da må man se på priselastisiteten. Elastisiteten er et mål på hvordan markedsetterspørselen og markedstilbudet blir påvirket av en endring i prisen, dette kan skje hvis man antar at alle andre variabler som påvirker tilbud og etterspørsel er konstante. Markedsetterspørselens priselastisitet kan defineres slik: 
# 
# #### markedsetterspørselens priselastisitet:
# $$ x^{D} = \frac{\frac{\Delta X^D}{X^D}}{\frac{\Delta p}{p}} = \frac{\Delta X^D}{\Delta p}\frac{p}{X^D} = \frac{\delta X^D}{\delta p}\frac{p}{X^D}$$
# 
# $$ x > -1 $$
# 
# #### Dette viser den prosentvise endringen i etterspørsel når prisen øker med 1 prosent. Dersom elastisiteten er -1 er godet prisnøytralt, hvis elastisiteten er negativ men større en -1 er godet prisuelastisk, hvis elastisiteten er mindre enn -1 er godet priselastisk. Den er bygget opp av å dele den prosentvise endringer i etterspørselen med den prosentvise endringen i pris.
# 
# #### markedstilbudets priselastisitet
# $$ x^{S} = \frac{\frac{\Delta X^S}{X^s}}{\frac{\Delta p}{p}} = \frac{\Delta X^s}{\Delta p}\frac{p}{X^s} = \frac{\delta X^s}{\delta p}\frac{p}{X^s}$$
# 
# $$ x > 1 $$
# 
# #### Når det gjelder hotelovernattinger som godet kan etterspørselen være svært priselastisk, dette kommer av at reiser og ferier er et luksusgode for de fleste. Dette betyr at en endring vil få store konsekvenser selvom endringen ikke er betraktelig stor. Konsumentene er da prisfølsomme, med en innføring av turistskatt vil prisen øke dette kommer også an på hvor stor andel skatten skal være, men en endring i pris vil uansett skape endringer i etterspørselen. Elastisiteten når den er følsom eller elastisk kan vises med en slak etterspørselslinje som i grafen over, men en uelastisk etterspørsel vil vises som en brattere ettterspørselslinje, forskjellen mellom disse to grafene er enkle å se, man kan se at de markerte områdene som viser oss ulike verdier til faktorer er større hos grafen med slak etterspørselslinje enn grafen med bratt etterspørselslinje. Dette betyr at påvirkningen av endring i pris vil være avhengig av hva elastisiteten er. Elastisiteten har en direkte kobling til priselastisiteten siden etterspørselens stigningstall står i funksjonen for etterspørselens priselastisitet som:
# 
# $$
# \frac{\delta X^D}{\delta p}
# $$
# 

# In[65]:


import matplotlib.pyplot as plt

# lager en ny linjeverdi
y4 = [10, 8, 6, 4, 2, 0, 0, 0, 0, 0]

# plotter linjeverdier
plt.plot(x1, y1, label='Tilbud')
plt.plot(x1, y4, label='Etterspørsel')
plt.plot(x1, y3, label='Tilbud 2')

# setter x og y limit
plt.ylim(1,10)
plt.xlim(1,10)

# lager ulike visningslinjer
plt.axhline(y = 4.65, xmin = 0, xmax = 0.3, linestyle = 'dashed', color='k')
plt.axvline(x = 3.65, ymin = 0, ymax = 0.4, linestyle = 'dashed', color='k')
plt.axhline(y = 4, xmin = 0, xmax = 0.34, linestyle = 'dashed', color='k')
plt.axvline(x = 4, ymin = 0, ymax = 0.34, linestyle = 'dashed', color= 'k')

x = np.linspace(1, 10)

# lager ulike markerte områder
rectangle = plt.Rectangle((0,3.65), 3.65, 1, fc='red', alpha = 0.3, label = 'Skatteproveny')
plt.gca().add_patch(rectangle)

pts = np.array([[0,4.65], [0,12], [3.65,4.65]])
p = Polygon(pts, alpha = 0.3, label = 'konsumentoverskudd')
plt.gca().add_patch(p)

pts1 = np.array([[0,0], [0,3.65], [3.65,3.65]])
p1 = Polygon(pts1, alpha = 0.3, label = 'produsentoverskudd', color = 'green')
plt.gca().add_patch(p1)

pts2 = np.array([[3.65,3.65], [4,4], [3.65,4.65]])
p1 = Polygon(pts2, alpha = 0.3, label = 'dødvektstap', color = 'yellow')
plt.gca().add_patch(p1)

# lager pil for å vise endring 
plt.arrow(7,7.1,0,0.4,width=0.1)

# lager punkt tekst
plt.text(3.65, 4.65, 'Skatt')
plt.text(4, 4, 'Uten Skatt')

# fjerner x og y verdier
plt.xticks([])
plt.yticks([])

# setter navn til aksene
plt.xlabel('kvantum')
plt.ylabel('pris')
  
# setter tittel 
plt.title('Likevekt mellom Etterspørsel og Tilbud')

plt.legend()
plt.show()


# #### Dette er effekter av en endring i pris på grunn av turistskatt, har desverre ingen etterspørsel og tilbuds linkninger fra den virkelige verden som gjør at vi bare kan bruke generelle eksempler, men de kan fremdeles gi uttrykk for hva som kan skje med en slik endring.

# ### Konklusjon 
# 
# #### Det som er funnet ut er at en prisendring på grunn av en turistskatt vil være svært ufortutsigbart, man må være presise og forsiktige med hvordan og hva denne skatten skal bety. Reiser er allerede et luksusgode så en endring i pris kan få store konsekvenser for markedet generelt, vi kan tydelig se at etterspørselen vil falle samtidig som at prisen vil øke, tilbudet vil måtte utvikle seg videre ut ifra dette. Som vi så i kap 2 har vi sett at omsetting blant overnattinger økte før pandemien som betyr at næringen var i positiv gang, en turistskatt kan påvirke denne utviklingen. Presist hvor store konsekvenser markedet vil få er avhengig av hvor elastisk markedet er, men som sagt vil man tro at markedet er elastisk som betyr store konsekvenser av en endring i pris. Turistnæringen er mye mer enn bare hotelovernattinger siden tursime påvirker store deler av den generelle økonomien, dette kommer av at en økning i pris vil føre til lavere etterspørsel som kan føre til et lavere total konsum som igjen vil påvirke andre deler av økonomien. Et lavere antall konsumenter kan være vanskelig for andre næringer som benytter seg av turismen. En turistskatt har fungert bra mange andre steder i verden, men Norge er ikke store på turisme i forhold til disse landene som betyr at en allerede liten økonomi med dyre priser og lite tilbud vil få usikre konsekvenser av en turistskatt. En annen ting å tenke på er hvordan disse ekstra inntektene etter en skatt vil bli brukt, disse inntektene må bli brukt på en god og bærekraftig måte for at det skal fungere, hvis inntekten ikke blir brukt til å fremme og forbedre turistnæringen vil det hele få motsatt effekt av det man håper på. Hvis en turiskskatt skal oppnå målene og fungere som den skal må man kunne se markedet fra et helhetlig perspektiv, dette gjør at man kan se endringer i hele markedet og forhåpentligvis finne en skatt som ligger bra til slik at den gir tilbake til turismen istedenfor å ta fra dem. 

# #### kilder:
# - Andreassen, Bredesen, Thøgersen, Innføring i mirkoøkonomi 3 utgave, 2020
# - https://snl.no/elastisitet_-_%C3%B8konomi#:~:text=Elastisitet%20er%20innen%20samfunns%C3%B8konomi%20en,endring%20i%20pris%20eller%20inntekt Martin Eckhoff Andresen, sist oppdatert 20. desember 2021
# - https://www.ssb.no/en/statbank/list/turismesat/ statistisk sentralbyrå
# - https://www.regjeringen.no/no/aktuelt/vurderer-destinasjoner-for-besoksbidrag/id2959885/?expand=factbox2959954 regjeringen, sist oppdatert 19. januar 2021
