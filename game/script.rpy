# Neo-Athenia: The Portal Chronicles - Master Script (Pro Stable V6.8 - HQ Integration)

# --- Initialization & Screens ---
init python:
    def club_shake():
        renpy.with_statement(hpunch)

screen character_stats():
    modal True
    zorder 100
    tag menu
    dismiss action Hide("character_stats")
    add Solid("#000c") 
    frame:
        xalign 0.5 yalign 0.4
        xsize 600 ysize 500
        background Frame(Solid("#00151a"), 4, 4)
        vbox:
            xalign 0.5 yalign 0.0
            spacing 20
            frame:
                xfill True ysize 60
                background Solid("#00ffcc")
                text "NEURAL STATUS: [player_name]" color "#00151a" size 28 bold True align (0.5, 0.5)
            null height 10
            hbox:
                xalign 0.5
                spacing 40
                vbox:
                    spacing 5
                    text "MINA CONNECTION" size 18 color "#ff00ff" xalign 0.5
                    bar value affection range 100 xsize 240 ysize 20
                vbox:
                    spacing 5
                    text "VERA CORRUPTION" size 18 color "#888" xalign 0.5
                    bar value vera_corruption range 100 xsize 240 ysize 20
            null height 20
            hbox:
                xalign 0.5
                spacing 60
                vbox:
                    spacing 15
                    text "LOGIC CORE" size 20 color "#00ffcc" bold True
                    text "SOCIAL PULSE" size 20 color "#ff00ff" bold True
                    text "NEURAL ENDUR." size 20 color "#ff3300" bold True
                vbox:
                    spacing 15
                    text "[logic_core]" size 20 color "#fff" xalign 1.0
                    text "[social_pulse]" size 20 color "#fff" xalign 1.0
                    text "[neural_endurance]" size 20 color "#fff" xalign 1.0
            null height 40
            textbutton "EXIT INTERFACE" action Hide("character_stats"):
                xalign 0.5
                text_size 24
                text_color "#ff3333"
                text_hover_color "#00ffcc"
                background Solid("#111")
                padding (20, 10)

screen quick_menu_stats():
    zorder 90
    hbox:
        align (0.98, 0.02)
        textbutton "📊 STATS" action Show("character_stats"):
            text_size 20
            text_color "#00ffcc"
            text_hover_color "#fff"
            background Solid("#0008")
            padding (10, 5)

# --- Characters ---
define m = Character("Μίνα", color="#ff00ff", who_outlines=[(2, "#000")])
define l = Character("Λύρα", color="#ff3300", who_outlines=[(2, "#000")])
define v = Character("Βέρα", color="#444444", who_outlines=[(2, "#000")])

# --- Global Variables ---
default player_name = "Άρης"
default affection = 0
default vera_corruption = 0
default current_location = "penthouse"
default logic_core = 1
default social_pulse = 1
default neural_endurance = 1

define a = Character("[player_name]", color="#00ffcc", who_outlines=[(2, "#000")])

label start:
    show screen quick_menu_stats
    scene bg room_night
    with fade
    python:
        name_input = renpy.input("Πώς σε λένε; (Πάτα Enter για 'Άρης')", length=20).strip()
        if name_input:
            player_name = name_input
    "Ο κώδικας του Lokal Platform τρέχει μπροστά σου, [player_name]..."
    a "Χρειάζομαι έναν καφέ... ή μια αποκάλυψη."
    stop music fadeout 1.0
    scene bg room_glitch
    with hpunch
    m "[player_name]... με ακούς;"
    menu:
        "Να αγγίξεις την οθόνη":
            $ logic_core += 1
            jump touch_portal
        "Να τραβηχτείς πίσω":
            $ neural_endurance += 1
            jump hesitate_portal

label touch_portal:
    m "Έλα, [player_name]. Η Neo-Athenia σε περιμένει."
    jump enter_neo_athenia

label hesitate_portal:
    m "Είναι πιο αληθινό από οτιδήποτε άλλο. Μην φοβάσαι."
    jump enter_neo_athenia

label enter_neo_athenia:
    scene bg neo_athenia_city
    with dissolve
    show mina neon_casual at right:
        zoom 0.5 
        yalign 1.0 
    with moveinright
    m "Καλωσόρισες στο σπίτι μου, [player_name]."
    menu:
        "«Πώς θα μου το αποδείξεις;»":
            jump proof_reality
        "Να κοιτάξεις έξω από το παράθυρο":
            jump look_view

label proof_reality:
    "Η Μίνα σε αγγίζει. Νιώθεις τον ηλεκτρισμό."
    $ affection += 10
    $ social_pulse += 2
    jump chapter_1_choice

label look_view:
    "Η Neo-Athenia είναι αχανής."
    $ logic_core += 2
    jump chapter_1_choice

label chapter_1_choice:
    m "Θέλεις να σε ξεναγήσω στο ρετιρέ ή να πιούμε κάτι;"
    menu:
        "«Πάμε για ένα ποτό»":
            jump drink_path
        "«Θέλω μια ξενάγηση»":
            jump tour_path

label drink_path:
    scene bg penthouse_bar
    with fade
    show mina neon_casual at right:
        zoom 0.5
        yalign 1.0
    m "Τι θα έλεγες για ένα 'Neural Rush';"
    a "Μίνα... πώς έγινε αυτό; Θέλω να γυρίσω πίσω."
    m "Άκουσε με. Θα κάνω τα πάντα για να σε προστατέψω."
    $ affection += 20
    $ neural_endurance += 2
    "Ξαφνικά, ένα glitch: {color=#444}ΠΑΙΧΝΙΔΙ{/color}"
    jump travel_menu

label tour_path:
    scene bg neo_athenia_city
    with fade
    show mina neon_casual at right:
        zoom 0.5
        yalign 1.0
    m "Έλα, [player_name]. Θέλω να σου δείξω πού 'γεννιούνται' οι αποφάσεις μου."
    $ logic_core += 3
    scene bg mina room
    with fade
    show mina casual at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    m "Καλωσόρισες στο προσωπικό μου καταφύγιο. Εδώ είμαι μόνο εγώ."
    menu:
        "«Θέλω να μείνουμε για πάντα εδώ»":
            $ affection += 20
            show mina bed at center:
                zoom 0.45
                yalign 1.0
            with dissolve
            m "Αχ Άρη... προσέχεις τι εύχεσαι στη Neo-Athenia; Γιατί οι επιθυμίες σου είναι οι διαταγές μου."
        "«Είναι πανέμορφα, αλλά πρέπει να δω την πόλη»":
            $ logic_core += 5
            m "Έχεις δίκιο. Η περιέργειά σου θα σε πάει μακριά."
    jump travel_menu

label travel_menu:
    scene bg neo_athenia_city
    with dissolve
    show mina neon_casual at right:
        zoom 0.5
        yalign 1.0
    m "Λοιπόν, [player_name], πού θα ήθελες να σε πάω τώρα;"
    menu:
        "Στο Studio της Λύρας":
            jump lyra_studio
        "Στο Club 'Synapse'":
            jump club_synapse
        "Στο Neural Park":
            jump neural_park
        "Στο Protocol HQ":
            jump protocol_hq
        "Στο Sector 13 (ΚΙΝΔΥΝΟΣ)" if vera_corruption >= 10:
            jump sector_13

label lyra_studio:
    scene bg lyra studio
    with fade
    show lyra standard at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    l "Επιτέλους! Ο 'Hero' μας έφτασε!"
    show mina neon_casual at right:
        zoom 0.5
        yalign 1.0
    with moveinright
    menu:
        "«Ναι, δείξε μου»":
            $ affection += 5
            $ logic_core += 1
            jump lyra_show_art
        "«Μήπως είναι λίγο νωρίς;»":
            jump lyra_too_early

label lyra_show_art:
    "Η Λύρα σου δείχνει το ολόγραμμα 'The Architect's Bridge'."
    jump lyra_nanny_moment

label lyra_too_early:
    l "Ποτέ δεν είναι νωρίς για τέχνη!"
    jump lyra_nanny_moment

label lyra_nanny_moment:
    l "Θα τον αφήσεις λίγο μαζί μου ή θα τον προσέχεις σαν ντάντα;"
    menu:
        "«Θέλω να μείνω με τη Λύρα»":
            $ affection += 5
            $ social_pulse += 3
            jump lyra_private_moment
        "«Καλύτερα όλοι μαζί»":
            $ affection += 10
            $ logic_core += 2
            jump lyra_group_moment

label lyra_private_moment:
    "Η πόρτα κλείνει. Η Λύρα σε πλησιάζει, κρατώντας ακόμα την παλέτα της."
    show lyra sitting at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    l "Τώρα που η 'ντάντα' έφυγε, μπορούμε να μιλήσουμε ελεύθερα."
    scene bg lyra secret
    with fade
    l "Αυτό είναι το 'Όνειρο του Άγκυρα'."
    "Η Λύρα σε πλησιάζει προκλητικά."
    m "Άρη; Οι παλμοί σου είναι εκτός ορίων!"
    l "Πάντα στην καλύτερη στιγμή... 😉"
    jump travel_menu

label lyra_group_moment:
    "Κάθεστε όλοι μαζί. Η ένταση είναι αισθητή."
    jump travel_menu

label club_synapse:
    scene bg club synapse
    with fade
    with hpunch
    "Το μπάσο δονεί τα πάντα."
    show mina club at right:
        zoom 0.45
        yalign 1.0
    with moveinright
    show lyra club at left:
        zoom 0.45
        yalign 1.0
    with moveinleft
    menu:
        "«Θέλω να χορέψω»":
            $ social_pulse += 5
            jump club_dance
        "«Θέλω να μιλήσω στη Βέρα»":
            $ vera_corruption += 10
            $ neural_endurance += 5
            jump club_vera_encounter

label club_dance:
    "Χορεύετε κάτω από τα λέιζερ."
    jump travel_menu

label club_vera_encounter:
    scene bg neo_athenia_city
    with fade
    show vera standard at center:
        zoom 0.45 
        yalign 1.0
    with dissolve
    v "Κοίτα ποιος αποφάσισε να βγει από τη γυάλα..."
    show vera dominant at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    v "Θα σε περιμένω στο Sector 13. Θα έρθεις να παίξουμε;"
    m "Αρκετά! Φεύγουμε, Άρη."
    v "Τρέξε, Hero... 😉"
    jump travel_menu

label sector_13:
    scene bg neo_athenia_city
    with fade
    "Φτάνεις στο Sector 13."
    show vera sector13 at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    v "Ήρθες λοιπόν... Εδώ... είσαι δικός μου."
    $ vera_corruption += 15
    return

label neural_park:
    scene bg neural_park
    with fade
    show mina neon_casual at right:
        zoom 0.5
        yalign 1.0
    with moveinright
    m "Εδώ είναι το μοναδικό μέρος που η Πλέξη συνδυάζεται με τη φύση."
    "Λαμβάνεις το Neural Interface σου."
    menu:
        "«Φαίνεσαι πιο αληθινή από ποτέ...»":
            $ affection += 15
            $ social_pulse += 5
        "«Το Interface με ζαλίζει λίγο...»":
            $ logic_core += 5
    jump travel_menu

label protocol_hq:
    scene bg protocol_hq
    with fade
    
    "Το Αρχηγείο των Protocol Architects είναι ακόμα πιο επιβλητικό από κοντά. Ο ήχος των δεδομένων που ρέουν μοιάζει με ψίθυρο από το μέλλον."
    
    show mina hq at center:
        zoom 0.45
        yalign 1.0
    with dissolve
    
    m "Καλωσόρισες στην καρδιά της Πλέξης, [player_name]. Εδώ είναι που ο κώδικας γίνεται πραγματικότητα."
    m "Σε κάλεσα εδώ γιατί η Βέρα έχει αρχίσει να αφήνει 'ίχνη' στα συστήματά μας. Χρειάζομαι το δικό σου καθαρό μυαλό για να τα εντοπίσουμε."
    
    a "Είμαι έτοιμος, Μίνα. Τι πρέπει να κάνω;"
    
    m "Σύνδεσε το Neural Interface σου με τον κεντρικό server. Θα προσπαθήσουμε να αποκωδικοποιήσουμε ένα πακέτο δεδομένων από το Sector 13."
    
    menu:
        "«Επίθεση κατά μέτωπο στον κώδικα» (Logic 10)":
            if logic_core >= 10:
                $ affection += 15
                $ logic_core += 5
                m "Εντυπωσιακό! Η ταχύτητά σου είναι απίστευτη. Βρήκες την τρύπα ασφαλείας σε δευτερόλεπτα."
                m "Μαζί σου, η Βέρα δεν έχει καμία ελπίδα. 😉"
            else:
                m "Πρόσεχε... ο κώδικας είναι πολύ περίπλοκος ακόμα για σένα. Άφησέ με να σε καθοδηγήσω πιο προσεκτικά."
                $ logic_core += 2

        "«Ανάλυση των μοτίβων της Βέρας»":
            $ logic_core += 5
            m "Σωστή και μεθοδική κίνηση. Καταλαβαίνεις πώς σκέφτεται... αυτό είναι το κλειδί."
            
        "«Προτιμώ την 'ιδιωτική' σου πλευρά...»" if social_pulse >= 10:
            $ affection += 20
            $ social_pulse += 5
            m "Άρη... σε ένα δωμάτιο γεμάτο αισθητήρες, εσύ επιλέγεις να εστιάσεις σε μένα;"
            m "Μου αρέσει ο τρόπος που αγνοείς τους κανόνες. 🫦"
            
    jump travel_menu

label penthouse_chill:
    m "Καλή επιλογή."
    return
