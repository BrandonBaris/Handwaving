label start:
    # SHOW SPLASH BG

    python:
        PLAYER_NAME = renpy.input("What is your name?")
        PLAYER_NAME = PLAYER_NAME.strip()

        if not PLAYER_NAME:
          PLAYER_NAME = "Null"

    "Conjurer [PLAYER_NAME]!  That's my class title as a mage when I graduated the academy."

    # CHANGE BG

    "Magic in its many forms exists on the world of Myrth that I live in, shaping it it to what it is today."
    "{b}ALL POWERFUL MAGIC!{/b}"
    "Able to create and destroy nations in a day."
    "That's what it used to be in the past."
    "In these peaceful times, magic is so common and regulated that this once coveted discipline is about as special as a normal job."

    # CHANGE BG
    "At the academy we learned how to use all the sorts of magic specializations and how to cast them."
    "After learning the basics, they recommended us to think carefully and choose a magic type to specialize in if we didn't already have one."
    "Difficulty, lineage, and restrictions were the largest factor when it came to it.  There were many ways to achieve the same goal and a lot of times it was just preference and style."
    "Summoning, transport, elemental, enchantment, healing... Thousands to choose from."
    "I decided to do something practical and went with {b}conjuring{/b}."  

    call conjuring_exp
    
    "After years of toiling and struggling, I finally became a certified magic user."
    "..."
    "All those years of studying an amazing art just to barely eke out a living conjuring rental tools in the city of Pom that I recently moved to."
    "Here I am sitting on the toilet as I practice my craft using hand movements to freecast it."

    call freecasting_exp

    "What should I conjure?"

    menu:

        "Bread.":
            "A circular motion, a grabbing motion, some wavy gesture, and finally a pinch..."
            "SUCCESS!"
            "I just pinched a loaf in two different ways at the same time."
            "One for the highlight reel!"
        "Booze.":
            "One of my most common go-to spells."
            "My hands are a frenzied blur as muscle memory conjures it in record time."
            "Eh...{i}Good enough.{/i}"
            "I'm going to be in here for a while."
        "Fire.":
            "HAND SEALING!"
            "BOAR!"
            "HORSE!"
            "TIGER!"
            "FIRE ARTS TECHNIQUE: KATON!"
            "..."
            "I laugh at myself as I practice being a lame ninja."

    # CHANGE BG
    "One day an invitation arrives from the Pom Mage Guild that I am registered with to work in this city."

    "{i}To Conjurer [PLAYER_NAME]:{/i}"
    "{i}Please join us as we promote magic diversity and creation at this year's magic weaving event at the Pom Mage Guild!{/i}"
    "{i}Mana coffee and cheesy bread things will be provided for free.{/i}"
    "{i}We hope to see you there!{/i}"
    "{i}{b}-- POM MAGE GUILD{/b}{/i}"

    "Should I go?"

    menu:
      "MANA COFFEE?! YES!":
          "On top of that, I may meet others mages that live in this city."
          "I eagerly prepare as the day finally arrived for the event."
          jump act_1_start

      "Sounds interesting. Alright.":
          "I guess this could be a good break from work and meet other mages."
          "Maybe I can create something like an invisibility cloak to disappear from some of my annoying clients."
          jump act_1_start

      "Boring.":
          "This conjurer doesn't need to waste time making friends that that could be used for crafting."
          "I toss the invitation into the trash as I conjure some wine to drown my existence in."
          jump bad_ending

    return