import quoteAPI
import jikanapi

# This usually gives the right MAL link to go along with the character but sometimes the character name given back from the quote finder is not compatible with the character search (the character name is spelled differently or the character name in the quote API output has something added at the end of their name)

def main(): 
  try:
    quote = quoteAPI.getQuote(title = input('\nInput Anime Name: '))
    quoteResult = quote.get()
    quote = quoteResult['quote']
    character = quoteResult['character']
    anime = quoteResult['anime']
    jikan = jikanapi.jikan(search = character)
    jikanResult = jikan.get()
    url = jikanResult['data'][0]['url']
    
    print(f"\n\"{quote}\" \n-{character} from \'{anime}\'\n")
    print(f"Character MAL Page: {url}")
    
  except:
    print('Error, probably invalid anime name')


main()

