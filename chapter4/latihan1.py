#tarif
tarifawal = 200000 #12jam
tarifnext = 10000 #per-jam
awalwakturental = 6.00
akhirwakturental = 23.50
#menghitung berapa lama rental
lamarental = int (akhirwakturental-awalwakturental)
#menghitung lama next rental
lamanextrental = lamarental - 12
#menghitung tarif next rental
tarifnextrental = lamanextrental * tarifnext
totaltarif = tarifawal + tarifnextrental
print(totaltarif)
