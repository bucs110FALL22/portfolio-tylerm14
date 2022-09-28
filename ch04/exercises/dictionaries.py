article = ("The Pokémon Company revealed a sort-of-new Pokémon coming to Pokémon Scarlet and Pokémon Violet this November: Wiglett, a Paldean region-spin on the lovable ground-type, Diglett. Wiglett is long, white, and loves hanging out on the beach. Wiglett was revealed in a somewhat unusual fashion, as part of a faux Zoom call between members of the World Ecological Pokémon Society, which is being shown a presentation on the Paldean region by Jacq, the player’s homeroom teacher in Pokémon Scarlet and Violet. During the video, various biomes and Paldean Pokémon are shown, including another newcomer, Paldean Wooper. Society members remark on Wiglett’s appearance, likening it to a region-specific version of Diglett — even though it is apparently a separate species. Whether Wiglett will evolve into another form — as Diglett does into Dugtrio — is unknown. You can watch the Wiglett reveal in this video uploaded by Serebii, if you don’t want to sit through the entire World Ecological Pokémon Society presentation. Pokémon Scarlet and Violet will be released Nov. 18 for Nintendo Switch. The newest mainline game will introduce the ninth generation of Pokémon and the new Paldean region. Players will be able to catch brand-new Pokémon like Armarouge, Ceruledge, Klawf, Grafaiai, Fidough, Paldean Wooper (aka Pooper), Cetitan, Cyclizar, Smoliv, Lechonk, and Pawmi. Those new creatures join Scarlet and Violet’s new starters Sprigatito, Fuecoco, and Quaxly, and two new Legendary Pokémon (Koraidon and Miraidon), in the series’ Pokédex.")

subs = {
  "Wiglett":"[REDACTED]",
  "Pokémon":"Pokémon \(^.^)/",
  "Scarlet":"Red",
  "Violet":"Purple"
}

for key, value in subs.items():
  article = article.replace(key, value)


print(article)