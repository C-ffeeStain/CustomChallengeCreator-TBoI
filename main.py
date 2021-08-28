from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


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
}

with open("VERSION") as f:
    version = f.read().strip()
    if version.find("-beta") != -1:
        print(
            "WARNING: You are using a beta version of the program. Please report any bugs."
        )
    else:
        pass


# fmt: off
items = {"The Sad Onion": 1,"The Inner Eye": 2,"Spoon Bender": 3,"Cricket's Head": 4,"My Reflection": 5,"Number One": 6,"Blood of the Martyr": 7,"Skatole": 9,"Magic Mushroom": 12,"The Virus": 13,"Roid Rage": 14,"<3": 15,"Raw Liver": 16,"Skeleton Key": 17,"A Dollar": 18,"Boom!": 19,"Transcendence": 20,"The Compass": 21,"Lunch": 22,"Dinner": 23,"Dessert": 24,"Breakfast": 25,"Rotten Meat": 26,"Wooden Spoon": 27,"The Belt": 28,"Mom's Underwear": 29,"Mom's Heels": 30,"Mom's Lipstick": 31,"Wire Coat Hanger": 32,"Lucky Foot": 46,"Cupid's Arrow": 48,"Steven": 50,"Pentagram": 51,"Dr. Fetus": 52,"Magneto": 53,"Treasure Map": 54,"Mom's Eye": 55,"The Ladder": 60,"Charm of the Vampire": 62,"The Battery": 63,"Steam Sale": 64,"Technology": 68,"Chocolate Milk": 69,"Growth Hormones": 70,"Mini Mush": 71,"Rosary": 72,"A Quarter": 74,"PHD": 75,"X-Ray Vision": 76,"The Mark": 79,"The Pact": 80,"Lord of the Pit": 82,"Loki's Horns": 87,"Spider Bite": 89,"The Small Rock": 90,"Spelunker Hat": 91,"Super Bandage": 92,"The Halo": 101,"The Common Cold": 103,"The Parasite": 104,"Mr. Mega": 106,"The Wafer": 108,"Money = Power": 109,"Mom's Contacts": 110,"Mom's Knife": 114,"Ouija Board": 115,"9 Volt": 116,"Dead Bird": 117,"Brimstone": 118,"Blood Bag": 119,"Odd Mushroom": 121,"Whore of Babylon": 122,"Bobby-Bomb": 125,"Bucket of Lard": 129,"A Lump of Coal": 132,"Guppy's Tail": 134,"Stigmata": 138,"Mom's Purse": 139,"Bob's Curse": 140,"Pageant Boy": 141,"Scapular": 142,"Speed Ball": 143,"Infestation": 148,"Ipecac": 149,"Tough Love": 150,"The Mulligan": 151,"Technology 2": 152,"Mutant Spider": 153,"Chemical Peel": 154,"Habit": 156,"Bloody Lust": 157,"Spirit of the Night": 159,"Ankh": 161,"Celtic Cross": 162,"Cat-o-nine-tails": 165,"Epic Fetus": 168,"Polyphemus": 169,"Mitre": 173,"Stem Cells": 176,"Fate": 179,"The Black Bean": 180,"Sacred Heart": 182,"Tooth Picks": 183,"Holy Grail": 184,"Dead Dove": 185,"SMB Super Fan": 189,"Pyro": 190,"3 Dollar Bill": 191,"MEAT!": 193,"Magic 8 Ball": 194,"Mom's Coin Purse": 195,"Squeezy": 196,"Jesus Juice": 197,"Box": 198,"Mom's Key": 199,"Mom's Eyeshadow": 200,"Iron Bar": 201,"Midas' Touch": 202,"Humbleing Bundle": 203,"Fanny Pack": 204,"Sharp Plug": 205,"Champion Belt": 208,"Butt Bombs": 209,"Gnawed Leaf": 210,"Spiderbaby": 211,"Guppy's Collar": 212,"Lost Contact": 213,"Anemic": 214,"Goat Head": 215,"Ceremonial Robes": 216,"Mom's Wig": 217,"Placenta": 218,"Old Bandage": 219,"Sad Bombs": 220,"Rubber Cement": 221,"Anti-Gravity": 222,"Pyromaniac": 223,"Cricket's Body": 224,"Gimpy": 225,"Black Lotus": 226,"Piggy Bank": 227,"Mom's Perfume": 228,"Monstro's Lung": 229,"Abaddon": 230,"Ball of Tar": 231,"Stop Watch": 232,"Tiny Planet": 233,"Infestation 2": 234,"E. Coli": 236,"Death's Touch": 237,"Experimental Treatment": 240,"Contract from Below": 241,"Infamy": 242,"Trinity Shield": 243,"Tech.5": 244,"20/20": 245,"Blue Map": 246,"BFFS!": 247,"Hive Mind": 248,"There's Options": 249,"BOGO Bombs": 250,"Starter Deck": 251,"Little Baggy": 252,"Magic Scab": 253,"Blood Clot": 254,"Screw": 255,"Hot Bombs": 256,"Fire Mind": 257,"Missing No.": 258,"Dark Matter": 259,"Black Candle": 260,"Proptosis": 261,"Missing Page 2": 262,"Taurus": 299,"Aries": 300,"Cancer": 301,"Leo": 302,"Virgo": 303,"Libra": 304,"Scorpio": 305,"Sagittarius": 306,"Capricorn": 307,"Aquarius": 308,"Pisces": 309,"Eve's Mascara": 310,"Judas' Shadow": 311,"Maggy's Bow": 312,"Holy Mantle": 313,"Thunder Thighs": 314,"Strange Attractor": 315,"Cursed Eye": 316,"Mysterious Liquid": 317,"The Polaroid": 327,"The Negative": 328,"The Ludovico Technique": 329,"Soy Milk": 330,"Godhead": 331,"Lazarus' Rags": 332,"The Mind": 333,"The Body": 334,"The Soul": 335,"Dead Onion": 336,"Broken Watch": 337,"Safety Pin": 339,"Caffeine Pill": 340,"Torn Photo": 341,"Blue Cap": 342,"Latch Key": 343,"Match Book": 344,"Synthoil": 345,"A Snack": 346,"Toxic Shock": 350,"Bomber Boy": 353,"Crack Jacks": 354,"Mom's Pearls": 355,"Car Battery": 356,"The Wiz": 358,"8 Inch Nails": 359,"Scatter Bombs": 366,"Sticky Bombs": 367,"Epiphora": 368,"Continuum": 369,"Mr. Dolly": 370,"Curse of the Tower": 371,"Dead Eye": 373,"Holy Light": 374,"Host Hat": 375,"Restock": 376,"Bursting Sack": 377,"No. 2": 378,"Pupula Duplex": 379,"Pay To Play": 380,"Eden's Blessing": 381,"Betrayal": 391,"Zodiac": 392,"Serpent's Kiss": 393,"Marked": 394,"Tech X": 395,"Tractor Beam": 397,"God's Flesh": 398,"Maw Of The Void": 399,"Spear Of Destiny": 400,"Explosivo": 401,"Chaos": 402,"Purity": 407,"Athame": 408,"Empty Vessel": 409,"Evil Eye": 410,"Lusty Blood": 411,"Cambion Conception": 412,"Immaculate Conception": 413,"More Options": 414,"Crown Of Light": 415,"Deep Pockets": 416,"Fruit Cake": 418,"Black Powder": 420,"Circle of Protection": 423,"Sack Head": 424,"Night Light": 425,"PJs": 428,"Head of the Keeper": 429,"Glitter Bombs": 432,"My Shadow": 433,"Binky": 438,"Kidney Stone": 440,"Dark Prince's Crown": 442,"Apple!": 443,"Lead Pencil": 444,"Dog Tooth": 445,"Dead Tooth": 446,"Linger Bean": 447,"Shard of Glass": 448,"Metal Plate": 449,"Eye of Greed": 450,"Tarot Cloth": 451,"Varicose Veins": 452,"Compound Fracture": 453,"Polydactyly": 454,"Dad's Lost Coin": 455,"Midnight Snack": 456,"Cone Head": 457,"Belly Button": 458,"Sinus Infection": 459,"Glaucoma": 460,"Parasitoid": 461,"Eye of Belial": 462,"Sulfuric Acid": 463,"Glyph of Balance": 464,"Analog Stick": 465,"Contagion": 466,"Adrenaline": 493,"Jacob's Ladder": 494,"Ghost Pepper": 495,"Euthanasia": 496,"Camo Undies": 497,"Duality": 498,"Eucharist": 499,"Greed's Gullet": 501,"Large Zit": 502,"Little Horn": 503,"Poke Go": 505,"Backstabber": 506,"Bozo": 513,"Broken Modem": 514,"Fast Bombs": 517,"Jumper Cables": 520,"Technology Zero": 524,"Pop!": 529,"Death's List": 530,"Haemolacria": 531,"Lachryphagy": 532,"Trisagion": 533,"Schoolbag": 534,"Blanket": 535,"Marbles": 538,"Flat Stone": 540,"Marrow": 541,"Dad's Ring": 546,"Divorce Papers": 547,"Brittle Bones": 549,"Broken Shovel": 550,"The Bible": 33,"The Book of Belial": 34,"The Necronomicon": 35,"The Poop": 36,"Mr. Boom": 37,"Tammy's Head": 38,"Mom's Bra": 39,"Kamikaze!": 40,"Mom's Pad": 41,"Bob's Rotten Head": 42,"Teleport!": 44,"Yum Heart": 45,"Doctor's Remote": 47,"Shoop da Whoop!": 49,"Lemon Mishap": 56,"Book of Shadows": 58,"Anarchist Cookbook": 65,"The Hourglass": 66,"My Little Unicorn": 77,"Book of Revelations": 78,"The Nail": 83,"We Need To Go Deeper!": 84,"Deck of Cards": 85,"Monstro's Tooth": 86,"The Gamekid": 93,"The Book of Sin": 97,"Mom's Bottle of Pills": 102,"The D6": 105,"The Pinking Shears": 107,"The Bean": 111,"Monster Manual": 123,"Dead Sea Scrolls": 124,"Razor Blade": 126,"Forget Me Now": 127,"A Pony": 130,"Guppy's Paw": 133,"IV Bag": 135,"Best Friend": 136,"Remote Detonator": 137,"Guppy's Head": 145,"Prayer Card": 146,"Notched Axe": 147,"Crystal Ball": 158,"Crack the Sky": 160,"The Candle": 164,"D20": 166,"Spider Butt": 171,"Dad's Key": 175,"Portable Slot": 177,"White Pony": 181,"Blood Rights": 186,"Telepathy For Dummies": 192,"Clear Rune": 263,"How to Jump": 282,"D100": 283,"D4": 284,"D10": 285,"Blank Card": 286,"Book of Secrets": 287,"Box of Spiders": 288,"Red Candle": 289,"The Jar": 290,"Flush!": 291,"Satanic Bible": 292,"Head of Krampus": 293,"Butter Bean": 294,"Magic Fingers": 295,"Converter": 296,"Pandora's Box": 297,"Unicorn Stump": 298,"Isaac's Tears": 323,"Undefined": 324,"Scissors": 325,"Breath of Life": 326,"The Boomerang": 338,"Diplopia": 347,"Placebo": 348,"Wooden Nickel": 349,"Mega Bean": 351,"Glass Cannon": 352,"Box of Friends": 357,"Friendly Ball": 382,"Tear Detonator": 383,"D12": 386,"Ventricle Razor": 396,"D8": 406,"Teleport 2.0": 419,"Kidney Bean": 421,"Glowing Hour Glass": 422,"Mine Crafter": 427,"Jar of Flies": 434,"D7": 437,"Mom's Box": 439,"Mega Blast": 441,"Plan C": 475,"D1": 476,"Void": 477,"Pause": 478,"Smelter": 479,"Compost": 480,"Dataminer": 481,"Clicker": 482,"Mama Mega!": 483,"Wait What?": 484,"Crooked Penny": 485,"Dull Razor": 486,"Potato Peeler": 487,"Metronome": 488,"D infinity": 489,"Eden's Soul": 490,"Brown Nugget": 504,"Sharp Straw": 507,"Delirious": 510,"Black Hole": 512,"Mystery Gift": 515,"Sprinkler": 516,"Coupon": 521,"Telekinesis": 522,"Moving Box": 523,"Mr. ME!": 527,"Sacrificial Altar": 536,"Book of the Dead": 545,"Mom's Shovel": 552,}
trinkets = {"Swallowed Penny": 1,"Petrified Poop": 2,"AAA Battery": 3,"Broken Remote": 4,"Purple Heart": 5,"Broken Magnet": 6,"Rosary Bead": 7,"Cartridge": 8,"Pulse Worm": 9,"Wiggle Worm": 10,"Ring Worm": 11,"Flat Worm": 12,"Store Credit": 13,"Callus": 14,"Lucky Rock": 15,"Mom's Toenail": 16,"Black Lipstick": 17,"Bible Tract": 18,"Paper Clip": 19,"Monkey Paw": 20,"Mysterious Paper": 21,"Daemon's Tail": 22,"Missing Poster": 23,"Butt Penny": 24,"Mysterious Candy": 25,"Hook Worm": 26,"Whip Worm": 27,"Broken Ankh": 28,"Fish Head": 29,"Pinky Eye": 30,"Push Pin": 31,"Liberty Cap": 32,"Umbilical Cord": 33,"Child's Heart": 34,"Curved Horn": 35,"Rusted Key": 36,"Goat Hoof": 37,"Mom's Pearl": 38,"Cancer": 39,"Red Patch": 40,"Match Stick": 41,"Lucky Toe": 42,"Cursed Skull": 43,"Safety Cap": 44,"Ace of Spades": 45,"Isaac's Fork": 46,"A Missing Page": 48,"Bloody Penny": 49,"Burnt Penny": 50,"Flat Penny": 51,"Counterfeit Penny": 52,"Tick": 53,"Isaac's Head": 54,"Maggy's Faith": 55,"Judas' Tongue": 56,"???'s Soul": 57,"Samson's Lock": 58,"Cain's Eye": 59,"Eve's Bird Foot": 60,"The Left Hand": 61,"Shiny Rock": 62,"Safety Scissors": 63,"Rainbow Worm": 64,"Tape Worm": 65,"Lazy Worm": 66,"Cracked Dice": 67,"Super Magnet": 68,"Faded Polaroid": 69,"Louse": 70,"Bob's Bladder": 71,"Watch Battery": 72,"Blasting Cap": 73,"Stud Finder": 74,"Error": 75,"Poker Chip": 76,"Blister": 77,"Second Hand": 78,"Endless Nameless": 79,"Black Feather": 80,"Blind Rage": 81,"Golden Horse Shoe": 82,"Store Key": 83,"Rib of Greed": 84,"Karma": 85,"Lil Larva": 86,"Mom's Locket": 87,"NO!": 88,"Child Leash": 89,"Brown Cap": 90,"Meconium": 91,"Cracked Crown": 92,"Used Diaper": 93,"Fish Tail": 94,"Black Tooth": 95,"Ouroboros Worm": 96,"Tonsil": 97,"Nose Goblin": 98,"Super Ball": 99,"Vibrant Bulb": 100,"Dim Bulb": 101,"Fragmented Card": 102,"Equality!": 103,"Wish Bone": 104,"Bag Lunch": 105,"Lost Cork": 106,"Crow Heart": 107,"Walnut": 108,"Duct Tape": 109,"Silver Dollar": 110,"Bloody Crown": 111,"Pay To Win": 112,"Locust of War": 113,"Locust of Pestilence": 114,"Locust of Famine": 115,"Locust of Death": 116,"Locust of Conquest": 117,"Bat Wing": 118,"Stem Cell": 119,"Hairpin": 120,"Wooden Cross": 121,"Butter!": 122,"Filigree Feather": 123,"Door Stop": 124,"Extension Cord": 125,"Rotten Penny": 126,"Baby-Bender": 127,"Finger Bone": 128}
# fmt: on

item_names = sorted(items.keys())
trinket_names = sorted(trinkets.keys())
all_items = sorted(item_names + trinket_names)

xml = "<challenges><challenge name={{NAME}} id={{ID}} startingitems={{ITEMS}} startingtrinkets={{TRINKETS}} startingpill={{PILL}} startingcard={{CARD}} playertype={{PLRTYPE}} endstage={{ENDBOSS}} ></challenge></challenges>"


class CreateNewChallengeWindow(QWidget):
    data = {}

    def prevPage(self):
        if self.page == 1:
            self.confirmClose()
        self.page -= 1
        self.pageHandler()

    def nextPage(self):
        if self.page >= 3:
            self.page = 3
            return
        self.page += 1
        self.pageHandler()

    def pageHandler(self):
        if self.page == 1:
            self.page_num.setText("1/3")
            self.page_num.move(280, 5)

            self.setGeometry(self.x(), self.y(), 300, 300)

            self.redhp.setVisible(False)
            self.redhp_input.setVisible(False)
            self.fullredhp.setVisible(False)
            self.fullredhp_input.setVisible(False)
            self.soul_hearts.setVisible(False)
            self.soul_hearts_input.setVisible(False)
            self.black_hearts.setVisible(False)
            self.black_hearts_input.setVisible(False)
            self.coins.setVisible(False)
            self.coins_input.setVisible(False)
            self.hp_desc.setVisible(False)
            self.all_items_layout.setVisible(False)
            self.all_items_label.setVisible(False)
            self.added_items_label.setVisible(False)
            self.added_items_layout.setVisible(False)
            self.add_item.setVisible(False)
            self.remove_item.setVisible(False)

            self.challenge_name.setVisible(True)
            self.challenge_name_input.setVisible(True)
            self.character.setVisible(True)
            self.character_input.setVisible(True)
            self.end_boss.setVisible(True)
            self.end_boss_input.setVisible(True)
            self.altPath.setVisible(True)
            self.blindfolded.setVisible(True)
            self.hard_mode.setVisible(True)
        elif self.page == 2:
            self.page_num.move(280, 5)
            self.page_num.setText("2/3")

            self.setGeometry(self.x(), self.y(), 300, 300)

            self.challenge_name.setVisible(False)
            self.challenge_name_input.setVisible(False)
            self.character.setVisible(False)
            self.character_input.setVisible(False)
            self.end_boss.setVisible(False)
            self.end_boss_input.setVisible(False)
            self.altPath.setVisible(False)
            self.blindfolded.setVisible(False)
            self.hard_mode.setVisible(False)
            self.all_items_label.setVisible(False)
            self.all_items_layout.setVisible(False)
            self.added_items_label.setVisible(False)
            self.added_items_layout.setVisible(False)
            self.add_item.setVisible(False)
            self.remove_item.setVisible(False)

            self.redhp.setVisible(True)
            self.redhp_input.setVisible(True)
            self.fullredhp.setVisible(True)
            self.fullredhp_input.setVisible(True)
            self.soul_hearts.setVisible(True)
            self.soul_hearts_input.setVisible(True)
            self.black_hearts.setVisible(True)
            self.black_hearts_input.setVisible(True)
            self.coins.setVisible(True)
            self.coins_input.setVisible(True)
            self.hp_desc.setVisible(True)
        elif self.page == 3:
            self.setGeometry(self.x(), self.y(), 500, 300)

            self.page_num.setText("3/3")
            self.page_num.move(480, 5)

            self.redhp.setVisible(False)
            self.redhp_input.setVisible(False)
            self.fullredhp.setVisible(False)
            self.fullredhp_input.setVisible(False)
            self.soul_hearts.setVisible(False)
            self.soul_hearts_input.setVisible(False)
            self.black_hearts.setVisible(False)
            self.black_hearts_input.setVisible(False)
            self.coins.setVisible(False)
            self.coins_input.setVisible(False)
            self.hp_desc.setVisible(False)

            self.all_items_label.setVisible(True)
            self.all_items_layout.setVisible(True)
            self.added_items_label.setVisible(True)
            self.added_items_layout.setVisible(True)
            self.add_item.setVisible(True)
            self.remove_item.setVisible(True)

    def altPathChecked(self):
        bosses = end_bosses
        self.end_boss_input.removeItem(10)
        self.end_boss_input.removeItem(9)
        if self.altPath.isChecked():
            self.end_boss_input.insertItem(9, "???")
            self.end_boss_input.insertItem(9, "Isaac")
        else:
            self.end_boss_input.insertItem(9, "The Lamb")
            self.end_boss_input.insertItem(9, "Satan")

    def confirmClose(self):
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
        self.setFont(QFont("fonts/Montserrat.ttf", 10))
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

        self.altPath = QCheckBox("Alternate Path (Cathedral/The Chest)", self)
        self.altPath.move(10, 160)
        self.altPath.stateChanged.connect(self.altPathChecked)

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
        self.fullredhp_input.setValidator(QIntValidator(-24, 24))

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
            "All heart values in this page are measured\nin half hearts. So 24 = 12 hearts.",
            self,
        )
        self.hp_desc.setFont(QFont("fonts/Montserrat.ttf", 8))
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
        self.all_items_label.setFont(QFont("fonts/Montserrat.ttf", 10, QFont.Bold))
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
        self.added_items_label.setFont(QFont("fonts/Montserrat.ttf", 10, QFont.Bold))
        self.added_items_label.move(360, 40)

        self.added_items_layout = QListWidget(self)
        self.added_items_layout.setFixedWidth(180)
        self.added_items_layout.setFixedHeight(205)
        self.added_items_layout.setSpacing(1)
        self.added_items_layout.setViewMode(QListView.ListMode)
        self.added_items_layout.move(310, 60)

        for item_name in all_items:
            if item_name in trinket_names:
                qlwi = QListWidgetItem(item_name, self.all_items_layout)
                qlwi.setText(item_name + " (T)")
                continue
            QListWidgetItem(item_name, self.all_items_layout)

        self.all_items_label.setVisible(False)
        self.all_items_layout.setVisible(False)

        # widgets on every page

        self.title = QLabel("Create New Challenge", self)
        self.title.setFont(QFont("Montserrat.ttf", 12, QFont.Bold))
        self.title.move(7, 7)

        self.page_num = QLabel("1/3", self)
        self.page_num.setFont(QFont("Montserrat.ttf", 9))
        self.page_num.setAlignment(Qt.AlignCenter)
        self.page_num.move(280, 5)

        self.nextButton = QPushButton("Next", self)
        self.nextButton.move(50, 275)
        self.nextButton.clicked.connect(self.nextPage)

        self.backButton = QPushButton("Back", self)
        self.backButton.move(175, 275)
        self.backButton.clicked.connect(self.prevPage)

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


class Main(QMainWindow):
    def createNewChallengeClicked(self):
        self.createNewChallengeWindow = CreateNewChallengeWindow()
        self.createNewChallengeWindow.move(self.x(), self.y())
        self.createNewChallengeWindow.show()
        self.destroy()

    def loadChallengeClicked(self):
        pass

    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("Custom Challenge Generator - TBoI")
        self.setGeometry(300, 300, 450, 300)
        self.setFont(QFont("fonts/Montserrat.ttf", 10))
        self.setFixedSize(300, 200)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.center()

        self.title = QLabel("Custom Challenge Generator\n(TBoI: Repentance)", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("fonts/Montserrat-Bold.ttf", 12, QFont.Bold))
        self.title.move(30, 20)
        self.title.adjustSize()

        self.createNewChallenge = QPushButton("Create New Challenge", self)
        self.createNewChallenge.clicked.connect(self.createNewChallengeClicked)
        self.createNewChallenge.move(85, 75)
        self.createNewChallenge.adjustSize()

        self.loadChallenge = QPushButton("Load Challenge", self)
        self.loadChallenge.clicked.connect(self.loadChallengeClicked)
        self.loadChallenge.move(105, 110)
        self.loadChallenge.adjustSize()

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


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())
