import csv

#def loe_tooted(failinimi):
 #   tooted = [] #uus tühjas list
#    with open(failinimi, encoding="utf-8", newline="") as f: # kodeering sest ä, ü, Õ + newline soovitakse kui csv failid, et töödeldaksid õigesti. With sulgub faili.
 #       loe_read = csv.DictReader(f, delimiter=";") # Sõnastik, võtab (inventari_nr;nimetus;hind_km_ta;laoseis;km_maar) nagu veergude nimed
 #       for rida in loe_read: # Lappab faili read
#            toode = { # Uus sõnastik
        #        "inventari_nr": rida["inventari_nr"],
       #         "nimetus": rida["nimetus"],
      #          "hind_km_ta": float(rida["hind_km_ta"]),
     #           "laoseis": int(rida["laoseis"]),
    #            "km_maar": int(rida["km_maar"]),
   #         }
  #          tooted.append(toode) # Lisab veerule otsas uut toode
 #   return tooted


#def main():
   # tooted = loe_tooted("tooted.csv")
  #  print(len(tooted))        # Näitab 1000 - good
 #   print(tooted[0])
#    print(tooted[1])


#if __name__ == "__main__":
#    main()

def loe_read(failinimi, kodeering="utf-8"):
    with open(failinimi, encoding=kodeering) as f:
        next(f, None)
        for rida in f:
            yield rida.rstrip("\n")
                              
toodete_arv = 0
toode_rida = []
vanad_mm = {}
otsas_toode = {}
eks_toode = {}

def lisa_toode(nimekiri, toode):
    nimekiri[nimekiri_nr] = { # Uus sõnastik
                "inventari_nr": toode[0],
                "nimetus": toode[1],
                "hind_km_ta": toode[2],
                "laoseis": toode[3],
                "km_maar": toode[4],
            }
    
def kontrolli_eks_toode(nimekiri, toode):
    if nimekiri.get("max_toode")["hind"] > toode[2]:
        lisa_toode()
    
for rida in loe_read("tooted.csv"):
    ["inventari_nr;nimetus;hind_km_ta;laoseis;km_maar"]
    ["INV-101894;Veebikaamera Lite;60.19;240;22"]
    toode_rida = rida.split(";")
    toodete_arv += 1
    vanad_mm[toode_rida[4]] = vanad_mm.get(toode_rida[4], 0) + 1
    
    toote_kogus_int = int(toode_rida[3])
    if toote_kogus_int <= 0:
        lisa_toode(otsas_toode, toode_rida)