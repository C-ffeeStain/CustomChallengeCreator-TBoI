from PyQt5.QtWidgets import (
    QDesktopWidget,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QComboBox,
    QCheckBox,
    QListView,
    QListWidget,
    QListWidgetItem,
    QDesktopWidget,
    QFileDialog,
)
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt, QPoint
from smelt_preset import generate_file
from page_handler import pageHandler
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from constants import BASE_DIR, IS_EXE
from platform import system as get_os

try:

    import winreg
except ImportError:
    winreg = None

if get_os() != "Windows":
    print("This program is only compatible with Windows.")
    sys.exit(0)

playertypes = [
    "Isaac",
    "Magdalene",
    "Cain",
    "Judas",
    "???",
    "Eve",
    "Samson",
    "Azazel",
    "Lazarus",
    "Eden",
    "The Lost",
    "Lazarus Risen",
    "Dark Judas",
    "Lilith",
    "Keeper",
    "Apollyon",
    "The Forgotten",
    "The Soul",
    "Bethany",
    "Jacob",
    "Esau",
    "Tainted Isaac",
    "Tainted Magdalene",
    "Tainted Cain",
    "Tainted Judas",
    "Tainted ???",
    "Tainted Eve",
    "Tainted Samson",
    "Tainted Azazel",
    "Tainted Lazarus",
    "Tainted Eden",
    "Tainted Lost",
    "Tainted Lilith",
    "Tainted Keeper",
    "Tainted Apollyon",
    "Tainted Forgotten",
    "Tainted Bethany",
    "Tainted Jacob",
    "Dead Tainted Lazarus",
    "Tainted Jacob 2",
    "Tainted Soul",
]

end_bosses = {
    "Basement 1 Boss": 1,
    "Basement 2 Boss": 2,
    "Caves 1 Boss": 3,
    "Caves 2 Boss": 4,
    "Depths 1 Boss": 5,
    "Mom": 6,
    "Womb 1 Boss": 7,
    "Mom's Heart/It Lives": 8,
    "Hush": 9,
    "Satan": 10,
    "The Lamb": 11,
    "Delirium": 12,
    "The Beast": 13,
    "Mega Satan": 14,
    "Mother": 15,
}

# fmt: off
items = {"The Sad Onion": 1,"The Inner Eye": 2,"Spoon Bender": 3,"Cricket's Head": 4,"My Reflection": 5,"Number One": 6,"Blood of the Martyr": 7,"Skatole": 9,"Magic Mushroom": 12,"The Virus": 13,"Roid Rage": 14,"<3": 15,"Raw Liver": 16,"Skeleton Key": 17,"A Dollar": 18,"Boom!": 19,"Transcendence": 20,"The Compass": 21,"Lunch": 22,"Dinner": 23,"Dessert": 24,"Breakfast": 25,"Rotten Meat": 26,"Wooden Spoon": 27,"The Belt": 28,"Mom's Underwear": 29,"Mom's Heels": 30,"Mom's Lipstick": 31,"Wire Coat Hanger": 32,"Lucky Foot": 46,"Cupid's Arrow": 48,"Steven": 50,"Pentagram": 51,"Dr. Fetus": 52,"Magneto": 53,"Treasure Map": 54,"Mom's Eye": 55,"The Ladder": 60,"Charm of the Vampire": 62,"The Battery": 63,"Steam Sale": 64,"Technology": 68,"Chocolate Milk": 69,"Growth Hormones": 70,"Mini Mush": 71,"Rosary": 72,"A Quarter": 74,"PHD": 75,"X-Ray Vision": 76,"The Mark": 79,"The Pact": 80,"Lord of the Pit": 82,"Loki's Horns": 87,"Spider Bite": 89,"The Small Rock": 90,"Spelunker Hat": 91,"Super Bandage": 92,"The Halo": 101,"The Common Cold": 103,"The Parasite": 104,"Mr. Mega": 106,"The Wafer": 108,"Money = Power": 109,"Mom's Contacts": 110,"Mom's Knife": 114,"Ouija Board": 115,"9 Volt": 116,"Dead Bird": 117,"Brimstone": 118,"Blood Bag": 119,"Odd Mushroom": 121,"Whore of Babylon": 122,"Bobby-Bomb": 125,"Bucket of Lard": 129,"A Lump of Coal": 132,"Guppy's Tail": 134,"Stigmata": 138,"Mom's Purse": 139,"Bob's Curse": 140,"Pageant Boy": 141,"Scapular": 142,"Speed Ball": 143,"Infestation": 148,"Ipecac": 149,"Tough Love": 150,"The Mulligan": 151,"Technology 2": 152,"Mutant Spider": 153,"Chemical Peel": 154,"Habit": 156,"Bloody Lust": 157,"Spirit of the Night": 159,"Ankh": 161,"Celtic Cross": 162,"Cat-o-nine-tails": 165,"Epic Fetus": 168,"Polyphemus": 169,"Mitre": 173,"Stem Cells": 176,"Fate": 179,"The Black Bean": 180,"Sacred Heart": 182,"Tooth Picks": 183,"Holy Grail": 184,"Dead Dove": 185,"SMB Super Fan": 189,"Pyro": 190,"3 Dollar Bill": 191,"MEAT!": 193,"Magic 8 Ball": 194,"Mom's Coin Purse": 195,"Squeezy": 196,"Jesus Juice": 197,"Box": 198,"Mom's Key": 199,"Mom's Eyeshadow": 200,"Iron Bar": 201,"Midas' Touch": 202,"Humbleing Bundle": 203,"Fanny Pack": 204,"Sharp Plug": 205,"Champion Belt": 208,"Butt Bombs": 209,"Gnawed Leaf": 210,"Spiderbaby": 211,"Guppy's Collar": 212,"Lost Contact": 213,"Anemic": 214,"Goat Head": 215,"Ceremonial Robes": 216,"Mom's Wig": 217,"Placenta": 218,"Old Bandage": 219,"Sad Bombs": 220,"Rubber Cement": 221,"Anti-Gravity": 222,"Pyromaniac": 223,"Cricket's Body": 224,"Gimpy": 225,"Black Lotus": 226,"Piggy Bank": 227,"Mom's Perfume": 228,"Monstro's Lung": 229,"Abaddon": 230,"Ball of Tar": 231,"Stop Watch": 232,"Tiny Planet": 233,"Infestation 2": 234,"E. Coli": 236,"Death's Touch": 237,"Experimental Treatment": 240,"Contract from Below": 241,"Infamy": 242,"Trinity Shield": 243,"Tech.5": 244,"20/20": 245,"Blue Map": 246,"BFFS!": 247,"Hive Mind": 248,"There's Options": 249,"BOGO Bombs": 250,"Starter Deck": 251,"Little Baggy": 252,"Magic Scab": 253,"Blood Clot": 254,"Screw": 255,"Hot Bombs": 256,"Fire Mind": 257,"Missing No.": 258,"Dark Matter": 259,"Black Candle": 260,"Proptosis": 261,"Missing Page 2": 262,"Taurus": 299,"Aries": 300,"Cancer": 301,"Leo": 302,"Virgo": 303,"Libra": 304,"Scorpio": 305,"Sagittarius": 306,"Capricorn": 307,"Aquarius": 308,"Pisces": 309,"Eve's Mascara": 310,"Judas' Shadow": 311,"Maggy's Bow": 312,"Holy Mantle": 313,"Thunder Thighs": 314,"Strange Attractor": 315,"Cursed Eye": 316,"Mysterious Liquid": 317,"The Polaroid": 327,"The Negative": 328,"The Ludovico Technique": 329,"Soy Milk": 330,"Godhead": 331,"Lazarus' Rags": 332,"The Mind": 333,"The Body": 334,"The Soul": 335,"Dead Onion": 336,"Broken Watch": 337,"Safety Pin": 339,"Caffeine Pill": 340,"Torn Photo": 341,"Blue Cap": 342,"Latch Key": 343,"Match Book": 344,"Synthoil": 345,"A Snack": 346,"Toxic Shock": 350,"Bomber Boy": 353,"Crack Jacks": 354,"Mom's Pearls": 355,"Car Battery": 356,"The Wiz": 358,"8 Inch Nails": 359,"Scatter Bombs": 366,"Sticky Bombs": 367,"Epiphora": 368,"Continuum": 369,"Mr. Dolly": 370,"Curse of the Tower": 371,"Dead Eye": 373,"Holy Light": 374,"Host Hat": 375,"Restock": 376,"Bursting Sack": 377,"Number Two": 378,"Pupula Duplex": 379,"Pay To Play": 380,"Eden's Blessing": 381,"Betrayal": 391,"Zodiac": 392,"Serpent's Kiss": 393,"Marked": 394,"Tech X": 395,"Tractor Beam": 397,"God's Flesh": 398,"Maw of the Void": 399,"Spear of Destiny": 400,"Explosivo": 401,"Chaos": 402,"Purity": 407,"Athame": 408,"Empty Vessel": 409,"Evil Eye": 410,"Lusty Blood": 411,"Cambion Conception": 412,"Immaculate Conception": 413,"More Options": 414,"Crown of Light": 415,"Deep Pockets": 416,"Fruit Cake": 418,"Black Powder": 420,"Circle of Protection": 423,"Sack Head": 424,"Night Light": 425,"PJs": 428,"Head of the Keeper": 429,"Glitter Bombs": 432,"My Shadow": 433,"Binky": 438,"Kidney Stone": 440,"Dark Prince's Crown": 442,"Apple!": 443,"Lead Pencil": 444,"Dog Tooth": 445,"Dead Tooth": 446,"Linger Bean": 447,"Shard of Glass": 448,"Metal Plate": 449,"Eye of Greed": 450,"Tarot Cloth": 451,"Varicose Veins": 452,"Compound Fracture": 453,"Polydactyly": 454,"Dad's Lost Coin": 455,"Midnight Snack": 456,"Cone Head": 457,"Belly Button": 458,"Sinus Infection": 459,"Glaucoma": 460,"Parasitoid": 461,"Eye of Belial": 462,"Sulfuric Acid": 463,"Glyph of Balance": 464,"Analog Stick": 465,"Contagion": 466,"Adrenaline": 493,"Jacob's Ladder": 494,"Ghost Pepper": 495,"Euthanasia": 496,"Camo Undies": 497,"Duality": 498,"Eucharist": 499,"Greed's Gullet": 501,"Large Zit": 502,"Little Horn": 503,"Poke Go": 505,"Backstabber": 506,"Bozo": 513,"Broken Modem": 514,"Fast Bombs": 517,"Jumper Cables": 520,"Technology Zero": 524,"Pop!": 529,"Death's List": 530,"Haemolacria": 531,"Lachryphagy": 532,"Trisagion": 533,"Schoolbag": 534,"Blanket": 535,"Marbles": 538,"Flat Stone": 540,"Marrow": 541,"Dad's Ring": 546,"Divorce Papers": 547,"Brittle Bones": 549,"Broken Shovel": 550,"Mucormycosis": 553,"2Spooky": 554,"Eye Sore": 558,"120 Volt": 559,"It Hurts": 560,"Almond Milk": 561,"Rock Bottom": 562,"Nancy Bombs": 563,"A Bar of Soap": 564,"Dream Catcher": 566,"Divine Intervention": 568,"Playdough Cookie": 570,"Orphan Socks": 571,"Eye of the Occult": 572,"Immaculate Heart": 573,"Monstrance": 574,"Dirty Mind": 576,"Spirit Sword": 579,"Rocket in a Jar": 583,"Book of Virtues": 584,"The Stairway": 586,"Sol": 588,"Luna": 589,"Mercurius": 590,"Venus": 591,"Terra": 592,"Mars": 593,"Jupiter": 594,"Saturnus": 595,"Uranus": 596,"Neptunus": 597,"Pluto": 598,"Voodoo Head": 599,"Eye Drops": 600,"Act of Contrition": 601,"Member Card": 602,"Battery Pack": 603,"Ocular Rift": 606,"Blood Bombs": 614,"Bird's Eye": 616,"Lodestone": 617,"Rotten Tomato": 618,"Birthright": 619,"Red Stew": 621,"Booster Pack": 624,"Evil Charm": 632,"Dogma": 633,"Purgatory": 634,"Knockout Drops": 637,"Akeldama": 641,"Revelation": 643,"Consolation Prize": 644,"Brimstone Bombs": 646,"4.5 Volt": 647,"False PHD": 654,"Vasculitis": 657,"Giant Cell": 658,"Tropicamide": 659,"Card Reading": 660,"Quints": 661,"Tooth and Nail": 663,"Binge Eater": 664,"Guppy's Eye": 665,"Dad's Note": 668,"Sausage": 669,"Options?": 670,"Candy Heart": 671,"A Pound of Flesh": 672,"Redemption": 673,"Spirit Shackles": 674,"Cracked Orb": 675,"Empty Heart": 676,"Astral Projection": 677,"C Section": 678,"Montezuma's Revenge": 680,"Bone Spurs": 683,"Hungry Soul": 684,"Soul Locket": 686,"Inner Child": 688,"Glitched Crown": 689,"Belly Jelly": 690,"Sacred Orb": 691,"Sanguine Bond": 692,"The Swarm": 693,"Heartbreak": 694,"Bloody Gust": 695,"Salvation": 696,"Azazel's Rage": 699,"Echo Chamber": 700,"Isaac's Tomb": 701,"Vengeful Spirit": 702,"Supper": 707,"Stapler": 708,"Keeper's Sack": 716,"Keeper's Kin": 717,"TMTRAINER": 721,"Hypercoagulation": 724,"IBS": 725,"Hemoptysis": 726,"Ghost Bombs": 727,"The Bible": 33,"The Book of Belial": 34,"The Necronomicon": 35,"The Poop": 36,"Mr. Boom": 37,"Tammy's Head": 38,"Mom's Bra": 39,"Kamikaze!": 40,"Mom's Pad": 41,"Bob's Rotten Head": 42,"Teleport!": 44,"Yum Heart": 45,"Doctor's Remote": 47,"Shoop da Whoop!": 49,"Lemon Mishap": 56,"Book of Shadows": 58,"Anarchist Cookbook": 65,"The Hourglass": 66,"My Little Unicorn": 77,"Book of Revelations": 78,"The Nail": 83,"We Need To Go Deeper!": 84,"Deck of Cards": 85,"Monstro's Tooth": 86,"The Gamekid": 93,"The Book of Sin": 97,"Mom's Bottle of Pills": 102,"The D6": 105,"The Pinking Shears": 107,"The Bean": 111,"Monster Manual": 123,"Dead Sea Scrolls": 124,"Razor Blade": 126,"Forget Me Now": 127,"A Pony": 130,"Guppy's Paw": 133,"IV Bag": 135,"Best Friend": 136,"Remote Detonator": 137,"Guppy's Head": 145,"Prayer Card": 146,"Notched Axe": 147,"Crystal Ball": 158,"Crack the Sky": 160,"The Candle": 164,"D20": 166,"Spider Butt": 171,"Dad's Key": 175,"Portable Slot": 177,"White Pony": 181,"Blood Rights": 186,"Telepathy For Dummies": 192,"Clear Rune": 263,"How to Jump": 282,"D100": 283,"D4": 284,"D10": 285,"Blank Card": 286,"Book of Secrets": 287,"Box of Spiders": 288,"Red Candle": 289,"The Jar": 290,"Flush!": 291,"Satanic Bible": 292,"Head of Krampus": 293,"Butter Bean": 294,"Magic Fingers": 295,"Converter": 296,"Pandora's Box": 297,"Unicorn Stump": 298,"Isaac's Tears": 323,"Undefined": 324,"Scissors": 325,"Breath of Life": 326,"The Boomerang": 338,"Diplopia": 347,"Placebo": 348,"Wooden Nickel": 349,"Mega Bean": 351,"Glass Cannon": 352,"Box of Friends": 357,"Friendly Ball": 382,"Tear Detonator": 383,"D12": 386,"Ventricle Razor": 396,"D8": 406,"Teleport 2.0": 419,"Kidney Bean": 421,"Glowing Hour Glass": 422,"Mine Crafter": 427,"Jar of Flies": 434,"D7": 437,"Mom's Box": 439,"Mega Blast": 441,"Broken Glass Cannon": 474,"Plan C": 475,"D1": 476,"Void": 477,"Pause": 478,"Smelter": 479,"Compost": 480,"Dataminer": 481,"Clicker": 482,"Mama Mega!": 483,"Wait What?": 484,"Crooked Penny": 485,"Dull Razor": 486,"Potato Peeler": 487,"Metronome": 488,"D infinity": 489,"Eden's Soul": 490,"Brown Nugget": 504,"Sharp Straw": 507,"Delirious": 510,"Black Hole": 512,"Mystery Gift": 515,"Sprinkler": 516,"Coupon": 521,"Telekinesis": 522,"Moving Box": 523,"Mr. ME!": 527,"Sacrificial Altar": 536,"Book of the Dead": 545,"Mom's Shovel": 552,"Golden Razor": 555,"Sulfur": 556,"Fortune Cookie": 557,"Damocles": 656,"Free Lemonade": 578,"Red Key": 580,"Wavy Cap": 582,"Alabaster Box": 585,"Mom's Bracelet": 604,"The Scooper": 605,"Eternal D6": 609,"Larynx": 611,"Genesis": 622,"Sharp Key": 623,"Mega Mush": 625,"Death Certificate": 628,"Meat Cleaver": 631,"Stitches": 635,"R Key": 636,"Eraser": 638,"Yuck Heart": 639,"Urn of Souls": 640,"Magic Skin": 642,"Plum Flute": 650,"Vade Retro": 653,"Spin to Win": 655,"Jar of Wisps": 685,"Friend Finder": 687,"Esau Jr.": 703,"Berserk!": 704,"Dark Arts": 705,"Abyss": 706,"Suplex!": 709,"Bag of Crafting": 710,"Flip": 711,"Lemegeton": 712,"Sumptorium": 713,"Recall": 714,"Hold": 715,"Keeper's Box": 719,"Everything Jar": 720,"Anima Sola": 722,"Spindown Dice": 723,"Gello": 728,"Decap Attack": 729,"Brother Bobby": 8,"Halo of Flies": 10,"1up!": 11,"Distant Admiration": 57,"Sister Maggy": 67,"Cube of Meat": 73,"Dead Cat": 81,"Little Chubby": 88,"Sack of Pennies": 94,"Robo-Baby": 95,"Little C.H.A.D.": 96,"The Relic": 98,"Little Gish": 99,"Little Steven": 100,"Guardian Angel": 112,"Demon Baby": 113,"Forever Alone": 128,"Bomb Bag": 131,"Bum Friend": 144,"The Peeper": 155,"Ghost Baby": 163,"Harlequin Baby": 167,"Daddy Longlegs": 170,"Sacrificial Dagger": 172,"Rainbow Baby": 174,"Holy Water": 178,"Guppy's Hairball": 187,"Abel": 188,"Guillotine": 206,"Ball of Bandages": 207,"Key Piece 1": 238,"Key Piece 2": 239,"Smart Fly": 264,"Dry Baby": 265,"Juicy Sack": 266,"Robo-Baby 2.0": 267,"Rotten Baby": 268,"Headless Baby": 269,"Leech": 270,"Mystery Sack": 271,"BBF": 272,"Bob's Brain": 273,"Best Bud": 274,"Lil Brimstone": 275,"Isaac's Heart": 276,"Lil Haunt": 277,"Dark Bum": 278,"Big Fan": 279,"Sissy Longlegs": 280,"Punching Bag": 281,"Gemini": 318,"Cain's Other Eye": 319,"???'s Only Friend": 320,"Samson's Chains": 321,"Mongo Baby": 322,"Incubus": 360,"Fate's Reward": 361,"Lil Chest": 362,"Sworn Protector": 363,"Friend Zone": 364,"Lost Fly": 365,"Charged Baby": 372,"Lil Gurdy": 384,"Bumbo": 385,"Censer": 387,"Key Bum": 388,"Rune Bag": 389,"Seraphim": 390,"Spider Mod": 403,"Farting Baby": 404,"GB Bug": 405,"Succubus": 417,"Obsessed Fan": 426,"Papa Fly": 430,"Multidimensional Baby": 431,"Lil Loki": 435,"Milk!": 436,"Finger!": 467,"Shade": 468,"Depression": 469,"Hushy": 470,"Lil Monstro": 471,"King Baby": 472,"Big Chubby": 473,"Acid Baby": 491,"YO LISTEN!": 492,"Sack of Sacks": 500,"Mom's Razor": 508,"Bloodshot Eye": 509,"Angry Fly": 511,"Buddy in a Box": 518,"Lil Delirium": 519,"Leprosy": 525,"7 Seals": 526,"Angelic Prism": 528,"Lil Spewer": 537,"Mystery Egg": 539,"Slipped Rib": 542,"Hallowed Ground": 543,"Pointy Rib": 544,"Jaw Bone": 548,"Blood Puppy": 565,"Paschal Candle": 567,"Blood Oath": 569,"The Intruder": 575,"Psy Fly": 581,"Boiled Baby": 607,"Freezer Baby": 608,"Bird Cage": 610,"Lost Soul": 612,"Lil Dumpy": 615,"Knife Piece 1": 626,"Knife Piece 2": 627,"Bot Fly": 629,"Tinytoma": 645,"Fruity Plum": 649,"Star of Bethlehem": 651,"Cube Baby": 652,"Strawman": 667,"Lil Abaddon": 679,"Lil Portal": 681,"Worm Friend": 682,"Vanishing Twin": 697,"Twisted Pair": 698,}
trinkets = {"Swallowed Penny": 1,"Petrified Poop": 2,"AAA Battery": 3,"Broken Remote": 4,"Purple Heart": 5,"Broken Magnet": 6,"Rosary Bead": 7,"Cartridge": 8,"Pulse Worm": 9,"Wiggle Worm": 10,"Ring Worm": 11,"Flat Worm": 12,"Store Credit": 13,"Callus": 14,"Lucky Rock": 15,"Mom's Toenail": 16,"Black Lipstick": 17,"Bible Tract": 18,"Paper Clip": 19,"Monkey Paw": 20,"Mysterious Paper": 21,"Daemon's Tail": 22,"Missing Poster": 23,"Butt Penny": 24,"Mysterious Candy": 25,"Hook Worm": 26,"Whip Worm": 27,"Broken Ankh": 28,"Fish Head": 29,"Pinky Eye": 30,"Push Pin": 31,"Liberty Cap": 32,"Umbilical Cord": 33,"Child's Heart": 34,"Curved Horn": 35,"Rusted Key": 36,"Goat Hoof": 37,"Mom's Pearl": 38,"Cancer": 39,"Red Patch": 40,"Match Stick": 41,"Lucky Toe": 42,"Cursed Skull": 43,"Safety Cap": 44,"Ace of Spades": 45,"Isaac's Fork": 46,"A Missing Page": 48,"Bloody Penny": 49,"Burnt Penny": 50,"Flat Penny": 51,"Counterfeit Penny": 52,"Tick": 53,"Isaac's Head": 54,"Maggy's Faith": 55,"Judas' Tongue": 56,"???'s Soul": 57,"Samson's Lock": 58,"Cain's Eye": 59,"Eve's Bird Foot": 60,"The Left Hand": 61,"Shiny Rock": 62,"Safety Scissors": 63,"Rainbow Worm": 64,"Tape Worm": 65,"Lazy Worm": 66,"Cracked Dice": 67,"Super Magnet": 68,"Faded Polaroid": 69,"Louse": 70,"Bob's Bladder": 71,"Watch Battery": 72,"Blasting Cap": 73,"Stud Finder": 74,"Error": 75,"Poker Chip": 76,"Blister": 77,"Second Hand": 78,"Endless Nameless": 79,"Black Feather": 80,"Blind Rage": 81,"Golden Horse Shoe": 82,"Store Key": 83,"Rib of Greed": 84,"Karma": 85,"Lil Larva": 86,"Mom's Locket": 87,"NO!": 88,"Child Leash": 89,"Brown Cap": 90,"Meconium": 91,"Cracked Crown": 92,"Used Diaper": 93,"Fish Tail": 94,"Black Tooth": 95,"Ouroboros Worm": 96,"Tonsil": 97,"Nose Goblin": 98,"Super Ball": 99,"Vibrant Bulb": 100,"Dim Bulb": 101,"Fragmented Card": 102,"Equality!": 103,"Wish Bone": 104,"Bag Lunch": 105,"Lost Cork": 106,"Crow Heart": 107,"Walnut": 108,"Duct Tape": 109,"Silver Dollar": 110,"Bloody Crown": 111,"Pay To Win": 112,"Locust of War": 113,"Locust of Pestilence": 114,"Locust of Famine": 115,"Locust of Death": 116,"Locust of Conquest": 117,"Bat Wing": 118,"Stem Cell": 119,"Hairpin": 120,"Wooden Cross": 121,"Butter!": 122,"Filigree Feather": 123,"Door Stop": 124,"Extension Cord": 125,"Rotten Penny": 126,"Baby-Bender": 127,"Finger Bone": 128,"Jawbreaker": 129,"Chewed Pen": 130,"Blessed Penny": 131,"Broken Syringe": 132,"Short Fuse": 133,"Gigante Bean": 134,"A Lighter": 135,"Broken Padlock": 136,"Myosotis": 137," 'M": 138,"Teardrop Charm": 139,"Apple of Sodom": 140,"Forgotten Lullaby": 141,"Beth's Faith": 142,"Old Capacitor": 143,"Brain Worm": 144,"Perfection": 145,"Devil's Crown": 146,"Charged Penny": 147,"Friendship Necklace": 148,"Panic Button": 149,"Blue Key": 150,"Flat File": 151,"Telescope Lens": 152,"Mom's Lock": 153,"Dice Bag": 154,"Holy Crown": 155,"Mother's Kiss": 156,"Torn Card": 157,"Torn Pocket": 158,"Gilded Key": 159,"Lucky Sack": 160,"Wicked Crown": 161,"Azazel's Stump": 162,"Dingle Berry": 163,"Ring Cap": 164,"Nuh Uh!": 165,"Modeling Clay": 166,"Polished Bone": 167,"Hollow Heart": 168,"Kid's Drawing": 169,"Crystal Key": 170,"Keeper's Bargain": 171,"Cursed Penny": 172,"Your Soul": 173,"Number Magnet": 174,"Strange Key": 175,"Lil Clot": 176,"Temporary Tattoo": 177,"Swallowed M80": 178,"RC Remote": 179,"Found Soul": 180,"Expansion Pack": 181,"Beth's Essence": 182,"The Twins": 183,"Adoption Papers": 184,"Cricket Leg": 185,"Apollyon's Best Friend": 186,"Broken Glasses": 187,"Ice Cube": 188,"Sigil of Baphomet": 189}
# fmt: on

item_names = sorted(items.keys())
trinket_names = sorted(trinkets.keys())
all_items = sorted(item_names + trinket_names)


class CreateNewChallengeWindow(QWidget):
    def browse_button_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.install_path_input.setText(path)
        self.next_button.setEnabled(True)

    def add_item_clicked(self):
        if self.all_items_layout.selectedItems() == []:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("No items selected!")
            dialog.setText("Please select an item from the list on the left to add.")
            dialog.exec_()
        else:
            item_name = self.all_items_layout.selectedItems()[0].text()
            self.data["items"] = self.data.get("items", []) + [item_name]
            self.added_items_layout.addItem(item_name)

    def remove_item_clicked(self):
        if self.added_items_layout.selectedItems() == []:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("No items selected!")
            dialog.setText(
                "Please select an item from the list on the right to remove."
            )
            dialog.exec_()
        else:
            item = self.added_items_layout.selectedItems()[0]
            self.added_items_layout.takeItem(self.added_items_layout.row(item))

    def prev_page(self):
        if self.page == 1:
            self.confirmClose()
            return
        self.page -= 1
        pageHandler(self)

    def next_page(self):
        if self.page >= 4:
            self.page = 4
            return
        self.page += 1
        pageHandler(self)

    def alt_path_checked(self):
        self.end_boss_input.removeItem(10)
        self.end_boss_input.removeItem(9)
        if self.altPath.isChecked():
            self.end_boss_input.insertItem(9, "???")
            self.end_boss_input.insertItem(9, "Isaac")
        else:
            self.end_boss_input.insertItem(9, "The Lamb")
            self.end_boss_input.insertItem(9, "Satan")

    def confirm_close(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Cancel Challenge Creation")
        dialog.setText("Are you sure you want to cancel creating a new challenge?")
        dialog.setModal(True)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        dialog.setIcon(QMessageBox.Question)
        code = dialog.exec_()
        if code == QMessageBox.Yes:
            self.close()
            sys.exit()

    def __init__(self, parent=None):
        super(CreateNewChallengeWindow, self).__init__(parent)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Create New Challenge")
        self.setFont(QFont(str(BASE_DIR / "resources/main_font.ttf"), 10))
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.center()

        self.page = 1

        self.challenge_name = QLabel("Name:", self)
        self.challenge_name.move(10, 40)

        self.challenge_name_input = QLineEdit(self)
        self.challenge_name_input.setPlaceholderText("Input challenge name...")
        self.challenge_name_input.move(60, 38)
        self.challenge_name_input.setMinimumWidth(200)

        self.character = QLabel("Character:", self)
        self.character.move(10, 80)

        self.character_input = QComboBox(self)
        for plr in playertypes:
            self.character_input.addItem(plr)
        self.character_input.move(75, 78)

        self.end_boss = QLabel("End Boss:", self)
        self.end_boss.move(10, 120)

        self.end_boss_input = QComboBox(self)
        for boss in end_bosses:
            self.end_boss_input.addItem(boss)
        self.end_boss_input.move(75, 118)

        self.alt_path = QCheckBox("Alternate Path (Cathedral/The Chest)", self)
        self.alt_path.move(10, 160)
        self.alt_path.stateChanged.connect(self.alt_path_checked)

        self.blindfolded = QCheckBox("Blindfolded", self)
        self.blindfolded.move(10, 185)

        self.hard_mode = QCheckBox("Hard Mode", self)
        self.hard_mode.move(10, 210)

        # page 2

        self.redhp = QLabel("Heart Containers:", self)
        self.redhp.move(10, 40)
        self.redhp.adjustSize()

        self.redhp_input = QLineEdit(self)
        self.redhp_input.setPlaceholderText("6")
        self.redhp_input.setFixedWidth(25)
        self.redhp_input.setValidator(QIntValidator(0, 24))
        self.redhp_input.move(115, 38)

        self.fullredhp = QLabel("Empty Red Hearts:", self)
        self.fullredhp.move(10, 80)
        self.fullredhp.adjustSize()

        self.fullredhp_input = QLineEdit(self)
        self.fullredhp_input.setPlaceholderText("0")
        self.fullredhp_input.move(120, 78)
        self.fullredhp_input.setFixedWidth(25)
        self.fullredhp_input.setValidator(QIntValidator(0, 24))

        self.soul_hearts = QLabel("Soul Hearts:", self)
        self.soul_hearts.move(10, 120)
        self.soul_hearts.adjustSize()

        self.soul_hearts_input = QLineEdit(self)
        self.soul_hearts_input.setPlaceholderText("0")
        self.soul_hearts_input.setFixedWidth(25)
        self.soul_hearts_input.setValidator(QIntValidator(0, 24))
        self.soul_hearts_input.move(83, 118)

        self.black_hearts = QLabel("Black Hearts:", self)
        self.black_hearts.move(10, 160)
        self.black_hearts.adjustSize()

        self.black_hearts_input = QLineEdit(self)
        self.black_hearts_input.setPlaceholderText("0")
        self.black_hearts_input.setFixedWidth(25)
        self.black_hearts_input.setValidator(QIntValidator(0, 24))
        self.black_hearts_input.move(98, 158)

        self.coins = QLabel("Coins:", self)
        self.coins.move(10, 185)
        self.coins.adjustSize()

        self.coins_input = QLineEdit(self)
        self.coins_input.setPlaceholderText("0")
        self.coins_input.setFixedWidth(25)
        self.coins_input.setValidator(QIntValidator(0, 99))
        self.coins_input.move(50, 183)

        self.hp_desc = QLabel(
            "All heart values in this page are measured in half hearts. So 24 = 12 hearts.",
            self,
        )
        self.hp_desc.setFont(QFont(str(BASE_DIR / "resources/main_font.ttf"), 8))
        self.hp_desc.setAlignment(Qt.AlignCenter)
        self.hp_desc.move(50, 245)

        self.fullredhp.setVisible(False)
        self.fullredhp_input.setVisible(False)
        self.redhp.setVisible(False)
        self.redhp_input.setVisible(False)
        self.soul_hearts.setVisible(False)
        self.soul_hearts_input.setVisible(False)
        self.black_hearts.setVisible(False)
        self.black_hearts_input.setVisible(False)
        self.coins.setVisible(False)
        self.coins_input.setVisible(False)
        self.hp_desc.setVisible(False)

        # page 3

        self.all_items_label = QLabel("All Items", self)
        self.all_items_label.setAlignment(Qt.AlignCenter)
        self.all_items_label.setFont(
            QFont(str(BASE_DIR / "resources/main_font.ttf"), 10, QFont.Bold)
        )
        self.all_items_label.move(65, 40)
        self.all_items_label.adjustSize()

        self.all_items_layout = QListWidget(self)
        self.all_items_layout.setFixedWidth(180)
        self.all_items_layout.setFixedHeight(205)
        self.all_items_layout.setSpacing(1)
        self.all_items_layout.setViewMode(QListView.ListMode)
        self.all_items_layout.move(10, 60)

        self.added_items_label = QLabel("Added Items", self)
        self.added_items_label.setAlignment(Qt.AlignCenter)
        self.added_items_label.setFont(
            QFont(str(BASE_DIR / "resources/main_font.ttf"), 10, QFont.Bold)
        )
        self.added_items_label.move(360, 40)

        self.added_items_layout = QListWidget(self)
        self.added_items_layout.setFixedWidth(180)
        self.added_items_layout.setFixedHeight(205)
        self.added_items_layout.setSpacing(1)
        self.added_items_layout.setViewMode(QListView.ListMode)
        self.added_items_layout.move(310, 60)

        self.add_item = QPushButton("Add Item", self)
        self.add_item.move(210, 110)
        self.add_item.adjustSize()
        self.add_item.clicked.connect(self.add_item_clicked)

        self.remove_item = QPushButton("Remove Item", self)
        self.remove_item.move(207, 140)
        self.remove_item.adjustSize()
        self.remove_item.clicked.connect(self.remove_item_clicked)

        self.smelt_trinket = QPushButton("Smelt Trinket", self)
        self.smelt_trinket.move(207, 160)
        self.smelt_trinket.adjustSize()

        for item_name in all_items:
            if item_name in trinket_names:
                qlwi = QListWidgetItem(item_name, self.all_items_layout)
                qlwi.setText(item_name + " (T)")
                continue
            QListWidgetItem(item_name, self.all_items_layout)

        self.all_items_label.setVisible(False)
        self.all_items_layout.setVisible(False)
        self.added_items_label.setVisible(False)
        self.added_items_layout.setVisible(False)
        self.add_item.setVisible(False)
        self.remove_item.setVisible(False)
        self.smelt_trinket.setVisible(False)

        # page 4

        self.install_label = QLabel(
            "If you don't know where The Binding of Isaac Rebirth is on\nYOUR system, go into Steam, click on the game, and from\nthere, click on the gear icon.Click 'Manage...', then \nBrowse Local Files. ",
            self,
        )
        self.install_label.setAlignment(Qt.AlignCenter)
        self.install_label.move(5, 25)
        self.install_label.setFont(QFont(str(BASE_DIR / "resources/main_font.ttf"), 8))
        self.install_label.adjustSize()

        self.install_path_label = QLabel("Game Folder:", self)
        self.install_path_label.move(10, 80)
        self.install_path_label.adjustSize()

        self.install_path_input = QLineEdit(self)
        self.install_path_input.setPlaceholderText(
            "The Binding of Isaac steam folder..."
        )
        winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        self.install_path_input.setFixedWidth(150)
        self.install_path_input.setReadOnly(True)
        self.install_path_input.move(10, 110)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.move(310, 80)
        self.browse_button.adjustSize()
        self.browse_button.clicked.connect(self.browse_button_clicked)

        self.install_label.setVisible(False)
        # widgets on every page

        self.title = QLabel("Create New Challenge", self)
        self.title.setFont(QFont("normal.ttf", 12, QFont.Bold))
        self.title.move(7, 7)

        self.page_num = QLabel("1/4", self)
        self.page_num.setFont(QFont("normal.ttf", 9))
        self.page_num.setAlignment(Qt.AlignCenter)
        self.page_num.move(280, 5)

        self.next_button = QPushButton("Next", self)
        self.next_button.move(175, 275)  # 275, 275
        self.next_button.clicked.connect(self.next_page)

        self.back_button = QPushButton("Back", self)
        self.back_button.move(50, 275)  # 155, 275
        self.back_button.clicked.connect(self.prev_page)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
