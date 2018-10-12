story='''
{}.But! {} only if ye be {} of valor!
For {} is guarded by a {} so {},
so {},that no {} yet has {}
with it... and {}!
'''



def main():
    command=input("Enter a command (eg:Eat ): ")
    plural_noun=input("Enter a plural_noun (eg: trees): ")
    animal=input("Enter an animal (eg:Cow ): ")
    location=input("Enter a location (eg:Maine or the playground ): ")
    singular_noun=input("Enter a singular_noun (eg:tree ): ")

    adjectives=[]
    adjectives.append(input("Enter an adjective  (e.g ., big): "))
    adjectives.append(input("Enter an another adjective :"))
    
    past_participles=[]
    past_participles.append(input("Enter a past_participle (e.g., played )"))
    past_participles.append(input("Enter an another past_participle "))

    mad_lib= story.format(command,command,
                            plural_noun,location,animal,
                            adjectives[0],adjectives[1],singular_noun,
                            past_participles[0],past_participles[1])

    print(mad_lib)


main()