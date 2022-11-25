# Structure: (level, upgrade required power points, upgrade required Coins
HERO_POWER_LEVEL_UPGRADE_REQUIRED = [
    (0, 0, 0),
    (1, 20, 20),
    (2, 30, 35),
    (3, 50, 75),
    (4, 80, 140),
    (5, 130, 290),
    (6, 210, 480),
    (7, 340, 800),
    (8, 550, 1250),
    (9, 890, 1875),
    (10, 1440, 2800)
]
HERO_RANKs = [
    (20, 500),
    (21, 550),
    (22, 600),
    (23, 650),
    (24, 700),
    (25, 750),
    (26, 800),
    (27, 850),
]

HERO_TYPE = ("STARTING BRAWLER", "TROPHY ROAD REWARD", "RARE", "SUPER RARE", "EPIC", "MYTHIC", "LEGENDARY", "CHROMATIC")
FIGHT_TYPE = ("DAMAGE DEALER", "TANK", )
HERO_PARAS = ("Name", "Trophies", "Power Level", "Power Points", "Rank", "Hero Type", "Fight Type", "Gadget",
              "Star Power", "Gear")

# hero list is a list of data type "HERO_PARAS"
TRAVIS_HERO_LIST = [
    ('SHELLY', 809, 11, 0, 26, 'STARTING BRAWLER', 'DAMAGE DEALER'),
    ('BULL', 733, 10, 648, 25, 'TROPHY ROAD REWARD', 'TANK'),
    ('EMZ', 692, 11, 0, 24, 'TROPHY ROAD REWARD', 'DAMAGE DEALER'),
    ('PENNY', 687, 10, 465, 24),
    ('JACKY', 678, 10, 812, 25),
    ('EDGAR', 675, 11, 0, 23, 'EPIC'),
    ('LEON', 649, 9, 1199, 23),
    ('BEE', 642, 11, 0, 23, 'EPIC'),
    ('SPIKE', 639, 10, 281, 22),
    ('GALE', 624, 10, 186, 22),
    ('BO', 623, 9, 1048, 22),
    ('BELLE', 619, 11, 0, 23, 'CHROMATIC'),
    ('COLETTE', 608, 9, 975, 22),
    ('AMBER', 603, 9, 423, 22),
    ('RUFFS', 601, 9, 1087,22),
    ('JESSIE', 601, 9, 993, 22),
    ('NITA', 599, 9, 1116, 22),
    ('MR.P', 599, 9, 687, 22),
    ('8-BIT', 599, 9, 1136, 23),
    ('BIBI', 590, 9, 1037, 22),
    ('MAX', 582, 9, 1074, 22),
    ('CROW', 579, 9, 285, 22),
    ('SURGE', 575, 9, 839, 23),
    ('EL PRIMO', 564, 9, 1263, 23),
    ('PAM', 557, 9, 990, 21),
    ('LOU', 555, 9, 1195, 22),
    ('ROSA', 554, 9, 901, 21),
    ('STU', 551, 10, 297, 21),
    ('FANG', 549, 9, 182, 21),
    ('MORTIS', 534, 10, 137, 20),
    ('LOLA', 530, 9, 132, 21),
    ('TICK', 522, 9, 988, 21),
    ('DARRYL', 518, 8, 1332, 22),
    ('BYRON', 512, 9, 960, 21),
    ('BARLEY', 508, 7, 1917, 21),
    ('POCO', 506, 7, 1587, 20),
    ('SPROUT', 505, 8, 1481, 20),
    ('BUZZ', 505, 8, 589, 20),
    ('TARA', 503, 8, 1142, 20),
    ('DYNAMIKE', 501, 9, 1030, 20),
    ('RICO', 500, 9, 1007, 22),
    ('PIPER', 500, 7, 1823, 20),
    ('NANI', 500, 7, 1883, 20),
    ('JANET', 500, 8, 372, 20),
    ('GRIFF', 500, 8, 1247, 21),
    ('GENE', 500, 7, 759, 20),
    ('FRANK', 500, 9, 920, 21),
    ('COLT', 500, 7, 1824, 20),
    ('CARL', 500, 7, 1903, 20),
    ('BROCK', 500, 8, 1415, 21),
    ('ASH', 500, 8, 712, 21),
    ('BONNIE', 498, 8, 379, 20),
    ('SQUEAK', 497, 7, 471, 20),
    ('GROM', 470, 7, 477, 19),
    ('EVE', 441, 7, 600, 18),
    ('OTIS', 428, 8, 308, 18),
    ('SAM', 351, 7, 102, 16),
    ('MEG', 345, 7, 376, 16),
    ('GUS', 277, 8, 9, 14),
    ('BUSTER', 229, 6, 340, 13),
    ('SANDY', 0, 0, 0, 0)
]
# {"name" : "string", "required power points": uint, "required coins" : uint}
TRAVIS_HERO_FINAL = []
