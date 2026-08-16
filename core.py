import time
import sys
import os
import re
import random
import math
import shutil
import datetime

# ========== ANSI COLOR CODES ==========
black, red, green, yellow, blue, purple, cyan, white = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
b_black, b_red, b_green, b_yellow, b_blue, b_purple, b_cyan, b_white = '\033[90m', '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m'

bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_purple, bg_cyan, bg_white = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
bg_b_black, bg_b_red, bg_b_green, bg_b_yellow, bg_b_blue, bg_b_purple, bg_b_cyan, bg_b_white = '\033[100m', '\033[101m', '\033[102m', '\033[103m', '\033[104m', '\033[105m', '\033[106m', '\033[107m'

bold, italic, underline, strike = '\033[1m', '\033[3m', '\033[4m', '\033[9m'
center = "center"
left = "left"
right = "right"

# ========== EMOJIS ==========
smile = '😀'
grin = '😁'
joy = '😂'
laugh = '🤣'
sweat_smile = '😅'
relieved = '😌'
happy = '😊'
blush = '😊'
innocent = '😇'
smiling_heart = '🥰'
smiling_star = '🤩'
kissing_heart = '😘'
kissing = '😗'
kissing_smiling = '😙'
kissing_closed = '😚'
yum = '😋'
stuck_out_tongue = '😛'
stuck_out_tongue_wink = '😜'
crazy = '😜'
stuck_out_tongue_closed = '😝'
money_mouth = '🤑'
hug = '🤗'
thinking = '🤔'
zipper_mouth = '🤐'
raised_eyebrow = '🤨'
neutral = '😐'
expressionless = '😑'
no_mouth = '😶'
smirk = '😏'
unamused = '😒'
rolling_eyes = '🙄'
grimacing = '😬'
lying = '🤥'
relieved2 = '😌'
pensive = '😔'
sleepy = '😪'
drooling = '🤤'
sleeping = '😴'
mask = '😷'
fever = '🤒'
cast = '🤕'
nauseated = '🤢'
vomiting = '🤮'
sneezing = '🤧'
hot = '🥵'
cold = '🥶'
woozy = '🥴'
dizzy_face = '😵'
exploding_head = '🤯'
cowboy = '🤠'
party = '🥳'
sunglasses = '😎'
nerd = '🤓'
monocle = '🧐'
confused = '😕'
worried = '😟'
slightly_frowning = '🙁'
frowning = '☹️'
open_mouth = '😮'
hushed = '😯'
astonished = '😲'
flushed = '😳'
pleading = '🥺'
frowning2 = '😦'
anguished = '😧'
fearful = '😨'
cold_sweat = '😰'
disappointed = '😞'
sweat = '😓'
cry = '😢'
sob = '😭'
scream = '😱'
confounded = '😖'
persevere = '😣'
disappointed_relieved = '😥'
tears = '😥'
weary = '😩'
tired = '😫'
yawning = '🥱'
triumph = '😤'
rage = '😡'
angry = '😠'
cursing = '🤬'
smiling_imp = '😈'
imp = '👿'
skull = '💀'
skull_crossbones = '☠️'
poop = '💩'
clown = '🤡'
ogre = '👹'
goblin = '👺'
ghost = '👻'
alien = '👽'
alien_monster = '👾'
robot = '🤖'

# ========== HEARTS ==========
heart = '❤️'
orange_heart = '🧡'
yellow_heart = '💛'
green_heart = '💚'
blue_heart = '💙'
purple_heart = '💜'
brown_heart = '🤎'
black_heart = '🖤'
white_heart = '🤍'
broken_heart = '💔'
heart_exclamation = '❣️'
two_hearts = '💕'
revolving_hearts = '💞'
beating_heart = '💓'
growing_heart = '💗'
sparkling_heart = '💖'
cupid = '💘'
gift_heart = '💝'
heart_hands = '🫶'
mending_heart = '❤️‍🩹'

# ========== STARS AND SYMBOLS ==========
star = '⭐'
star2 = '🌟'
sparkles = '✨'
comet = '☄️'
dizzy = '💫'
boom = '💥'
hole = '🕳️'
speech_balloon = '💬'
thought_balloon = '💭'
anger = '💢'
zzz = '💤'
musical_note = '🎵'
notes = '🎶'
microphone = '🎤'
headphones = '🎧'
saxophone = '🎷'
guitar = '🎸'
piano = '🎹'
trumpet = '🎺'
violin = '🎻'
drum = '🥁'

# ========== NATURE ==========
sun = '☀️'
moon = '🌙'
new_moon = '🌑'
waxing_crescent = '🌒'
first_quarter = '🌓'
waxing_gibbous = '🌔'
full_moon = '🌕'
waning_gibbous = '🌖'
last_quarter = '🌗'
waning_crescent = '🌘'
crescent_moon = '🌙'
new_moon_face = '🌚'
first_quarter_face = '🌛'
last_quarter_face = '🌜'
thermometer = '🌡️'
sun_small = '🌤️'
sun_cloud = '⛅'
sun_cloud2 = '🌥️'
cloud = '☁️'
cloud_rain = '🌧️'
cloud_snow = '🌨️'
cloud_lightning = '🌩️'
tornado = '🌪️'
fog = '🌫️'
wind = '💨'
rainbow = '🌈'
umbrella = '☔'
umbrella2 = '🌂'
snowflake = '❄️'
snowman = '⛄'
fire = '🔥'
droplet = '💧'
water_wave = '🌊'

# ========== ANIMALS ==========
dog = '🐕'
dog_face = '🐶'
cat = '🐈'
cat_face = '🐱'
mouse = '🐁'
mouse_face = '🐭'
hamster = '🐹'
rabbit = '🐇'
rabbit_face = '🐰'
fox = '🦊'
bear = '🐻'
panda = '🐼'
koala = '🐨'
tiger = '🐅'
tiger_face = '🐯'
lion = '🦁'
cow = '🐄'
cow_face = '🐮'
pig = '🐖'
pig_face = '🐷'
pig_nose = '🐽'
frog = '🐸'
monkey = '🐒'
monkey_face = '🐵'
gorilla = '🦍'
orangutan = '🦧'
chicken = '🐔'
rooster = '🐓'
bird = '🐦'
penguin = '🐧'
dove = '🕊️'
eagle = '🦅'
duck = '🦆'
swan = '🦢'
owl = '🦉'
bat = '🦇'
wolf = '🐺'
deer = '🦌'
horse = '🐎'
horse_face = '🐴'
unicorn = '🦄'
zebra = '🦓'
giraffe = '🦒'
elephant = '🐘'
mammoth = '🦣'
rhino = '🦏'
hippo = '🦛'
mouse2 = '🐭'
rat = '🐀'
kangaroo = '🦘'
camel = '🐪'
camel2 = '🐫'
llama = '🦙'
snake = '🐍'
lizard = '🦎'
turtle = '🐢'
crocodile = '🐊'
whale = '🐋'
whale2 = '🐳'
dolphin = '🐬'
seal = '🦭'
fish = '🐟'
tropical_fish = '🐠'
blowfish = '🐡'
shark = '🦈'
octopus = '🐙'
shell = '🐚'
snail = '🐌'
butterfly = '🦋'
bug = '🐛'
ant = '🐜'
bee = '🐝'
beetle = '🪲'
ladybug = '🐞'
cricket = '🦗'
cockroach = '🪳'
spider = '🕷️'
spider_web = '🕸️'
scorpion = '🦂'
mosquito = '🦟'
fly = '🪰'
worm = '🪱'
microbe = '🦠'

# ========== FOOD ==========
apple = '🍎'
green_apple = '🍏'
pear = '🍐'
orange = '🍊'
tangerine = '🍊'
lemon = '🍋'
banana = '🍌'
watermelon = '🍉'
grapes = '🍇'
strawberry = '🍓'
blueberries = '🫐'
melon = '🍈'
cherries = '🍒'
peach = '🍑'
mango = '🥭'
pineapple = '🍍'
coconut = '🥥'
kiwi = '🥝'
tomato = '🍅'
eggplant = '🍆'
avocado = '🥑'
broccoli = '🥦'
leafy_green = '🥬'
cucumber = '🥒'
pepper = '🫑'
corn = '🌽'
carrot = '🥕'
garlic = '🧄'
onion = '🧅'
potato = '🥔'
sweet_potato = '🍠'
mushroom = '🍄'
peanuts = '🥜'
chestnut = '🌰'
bread = '🍞'
croissant = '🥐'
baguette = '🥖'
flatbread = '🫓'
pretzel = '🥨'
bagel = '🥯'
pancakes = '🥞'
waffle = '🧇'
cheese = '🧀'
meat = '🥩'
bacon = '🥓'
hamburger = '🍔'
fries = '🍟'
pizza = '🍕'
hotdog = '🌭'
sandwich = '🥪'
taco = '🌮'
burrito = '🌯'
tamale = '🫔'
falafel = '🧆'
egg = '🥚'
cooking = '🍳'
shallow_pan = '🥘'
stew = '🍲'
fondue = '🫕'
bowl = '🥣'
salad = '🥗'
popcorn = '🍿'
butter = '🧈'
salt = '🧂'
canned_food = '🥫'
bento = '🍱'
rice_cracker = '🍘'
rice_ball = '🍙'
rice = '🍚'
curry = '🍛'
ramen = '🍜'
spaghetti = '🍝'
sweet_potato = '🍠'
oden = '🍢'
sushi = '🍣'
fried_shrimp = '🍤'
fish_cake = '🍥'
moon_cake = '🥮'
dango = '🍡'
dumpling = '🥟'
fortune_cookie = '🥠'
takeout = '🥡'
icecream = '🍦'
ice_cream = '🍨'
soft_ice = '🍦'
shaved_ice = '🍧'
yogurt = '🥛'
custard = '🍮'
cake = '🍰'
birthday = '🎂'
pie = '🥧'
chocolate_bar = '🍫'
candy = '🍬'
lollipop = '🍭'
custard2 = '🍮'
honey = '🍯'
cookie = '🍪'
doughnut = '🍩'
cupcake = '🧁'
milk = '🥛'
coffee = '☕'
tea = '🍵'
bubble_tea = '🧋'
mate = '🧉'
sake = '🍶'
beer = '🍺'
beers = '🍻'
clink = '🥂'
wine = '🍷'
tumbler = '🥃'
cocktail = '🍸'
tropical = '🍹'
bottle = '🍾'
ice = '🧊'
spoon = '🥄'
knife_fork = '🍴'
knife_fork_plate = '🍽️'
amphora = '🏺'

# ========== SPORTS ==========
soccer = '⚽'
basketball = '🏀'
football = '🏈'
baseball = '⚾'
softball = '🥎'
tennis = '🎾'
volleyball = '🏐'
rugby = '🏉'
hockey = '🏒'
field_hockey = '🏑'
lacrosse = '🥍'
ping_pong = '🏓'
badminton = '🏸'
boxing = '🥊'
martial_arts = '🥋'
goal = '🥅'
golf = '⛳'
ice_skate = '⛸️'
fishing = '🎣'
diving = '🤿'
running = '🏃'
walking = '🚶'
dancing = '💃'
skier = '⛷️'
snowboarder = '🏂'
surfing = '🏄'
swimming = '🏊'
weightlifting = '🏋️'
biking = '🚴'
gymnastics = '🤸'

# ========== TRANSPORT ==========
car = '🚗'
taxi = '🚕'
suv = '🚙'
bus = '🚌'
trolley = '🚎'
train = '🚆'
metro = '🚇'
tram = '🚊'
monorail = '🚝'
bike = '🚲'
scooter = '🛴'
skateboard = '🛹'
roller_skate = '🛼'
plane = '✈️'
helicopter = '🚁'
rocket = '🚀'
ufo = '🛸'
ship = '🚢'
boat = '⛵'
canoe = '🛶'
submarine = '🛥️'
ambulance = '🚑'
fire_engine = '🚒'
police = '🚓'

# ========== OBJECTS ==========
crown = '👑'
top_hat = '🎩'
graduation = '🎓'
billed_cap = '🧢'
helmet = '⛑️'
watch = '⌚'
phone = '📱'
computer = '💻'
keyboard = '⌨️'
mouse = '🖱️'
printer = '🖨️'
camera = '📷'
video_camera = '📹'
projector = '📽️'
tv = '📺'
radio = '📻'
speaker = '🔈'
bell = '🔔'
clock = '🕰️'
alarm = '⏰'
hourglass = '⌛'
gift = '🎁'
balloon = '🎈'
confetti = '🎉'
ribbon = '🎀'
medal = '🏅'
trophy = '🏆'
microphone = '🎤'
headphones = '🎧'
megaphone = '📣'
loudspeaker = '📢'
money = '💰'
credit_card = '💳'
gem = '💎'
key = '🔑'
lock = '🔒'
unlock = '🔓'
hammer = '🔨'
wrench = '🔧'
screwdriver = '🪛'
nut_bolt = '🔩'
gear = '⚙️'
scissors = '✂️'
pen = '✒️'
pencil = '✏️'
notebook = '📓'
book = '📖'
newspaper = '📰'
mail = '✉️'
package = '📦'
door = '🚪'
mirror = '🪞'
window = '🪟'
lamp = '💡'
light_bulb = '💡'
battery = '🔋'
plug = '🔌'
trash = '🗑️'
toilet = '🚽'
shower = '🚿'
bathtub = '🛁'
bed = '🛏️'
sofa = '🛋️'
chair = '🪑'
desk = '🪧'
umbrella = '☂️'
parasol = '⛱️'
fan = '🪭'
thermometer = '🌡️'
candle = '🕯️'
mirror_ball = '🪩'
flag = '🎏'
balloon2 = '🎈'
pinata = '🪅'
nesting_dolls = '🪆'


def superprint(word, delay=0, side=None, color='', bg_color='', style='', end='\n'):
    """
    Prints text character by character with delay, color, background, style, and alignment.
    
    Parameters:
        word: text (or any object convertible to string)
        delay: delay between characters (seconds)
        side: alignment ('left', 'center', 'right') or None (default left)
        color: text color (e.g., toolsan.red)
        bg_color: background color (e.g., toolsan.bg_blue)
        style: style (e.g., toolsan.bold)
        end: ending character (default '\\n')
    """
    word = str(word)
    
    # Get terminal width
    width = shutil.get_terminal_size().columns
    
    # Calculate indentation based on alignment
    spaces = ''
    if side == center:
        spaces = ' ' * ((width - len(word)) // 2)
    elif side == right:
        spaces = ' ' * (width - len(word))
    # For 'left' or None, spaces remains empty
    
    # Build prefix for color/style
    prefix = ''
    if style:
        prefix += style
    if color:
        prefix += color
    if bg_color:
        prefix += bg_color
    
    suffix = '\033[0m' if prefix else ''
    
    # Print indentation if any
    if spaces:
        sys.stdout.write(spaces)
    
    # Set color/style
    if prefix:
        sys.stdout.write(prefix)
    
    # Print word character by character
    for char in word:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    # Reset color/style
    if suffix:
        sys.stdout.write(suffix)
    
    # End the line
    print(end=end, flush=True)


def loadspin(seconds, speed=10, color=''):
    """
    Displays an animated spinner for a specified duration.
    
    Parameters:
        seconds: duration to spin (seconds)
        speed: animation speed (frames per second)
        color: spinner color
    """
    frames = ['|', '/', '-', '\\']
    start = time.perf_counter()
    i = 0

    if color:
        sys.stdout.write(color)

    while time.perf_counter() - start < seconds:
        sys.stdout.write(f"\r{frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(1 / speed)
        i += 1

    if color:
        sys.stdout.write('\033[0m')
    print()


def smart_input(prompt, typ=str, delay=0, color=''):
    """
    Displays a prompt with color and character-by-character delay,
    then requests input and returns it with type conversion.
    
    Parameters:
        prompt: input prompt text
        typ: type to convert input to (default str)
        delay: delay between characters (seconds)
        color: prompt color
    """
    if color:
        sys.stdout.write(color)
    
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write('\033[0m')
    user_input = input()
    
    try:
        return typ(user_input)
    except ValueError:
        return None


def bgcolor(color=None):
    """
    Fills the entire screen with a background color.
    
    Parameters:
        color: background color code (e.g., toolsan.bg_red)
    """
    if color:
        sys.stdout.write(color)
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.write("\n" * 50)
        sys.stdout.write("\033[H")
    else:
        sys.stdout.write("\033[0m")
        sys.stdout.write("\033[2J\033[H")
    
    sys.stdout.flush()


def between(text, word=None, left=None, right=None):
    """
    Checks if a word appears between two other words in a text.
    
    Parameters:
        text: input text (string or list)
        word: target word
        left: left boundary word
        right: right boundary word
    """
    if type(text) is str:
        text = text.split()
    elif type(text) is not list:
        return False
    try:
        pos1 = text.index(left)
        pos2 = text.index(word)
        pos3 = text.index(right)
        if pos1 < pos2 < pos3 or pos1 > pos2 > pos3:
            return True
    except Exception:
        return False


def calculate(expression):
    """
    Safe calculator supporting sin, cos, sqrt, ln, log, factorial, parentheses.
    
    Parameters:
        expression: mathematical expression as string
    
    Returns:
        float or int: result, or None if invalid
    """
    try:
        expr = expression.strip().lower().replace(' ', '')
        
        # Constants
        expr = expr.replace('π', 'pi').replace('pi', str(math.pi))
        expr = expr.replace('e', str(math.e))
        
        # Operation symbols
        expr = expr.replace('×', '*').replace('•', '*').replace('x', '*').replace('х', '*')
        expr = expr.replace('÷', '/').replace(':', '/').replace('^', '**')
        
        # Superscripts
        for sym, val in {'²':'**2','³':'**3','⁴':'**4','⁵':'**5','⁶':'**6','⁷':'**7','⁸':'**8','⁹':'**9'}.items():
            expr = expr.replace(sym, val)
        
        # Recursive parser
        def parse(e):
            e = e.replace(' ', '')
            
            # 1. Functions (sin, cos, sqrt, ln, log, log10)
            functions = [
                ('sin', lambda x: math.sin(math.radians(float(x)))),
                ('cos', lambda x: math.cos(math.radians(float(x)))),
                ('sqrt', lambda x: math.sqrt(float(x))),
                ('ln', lambda x: math.log(float(x))),
                ('log', lambda x: math.log10(float(x))),
                ('log10', lambda x: math.log10(float(x))),
            ]
            
            for func_name, func in functions:
                pattern = re.compile(rf'{func_name}\(([^()]+)\)')
                while True:
                    m = pattern.search(e)
                    if not m:
                        break
                    arg = parse(m.group(1))
                    res = func(arg)
                    e = e[:m.start()] + str(res) + e[m.end():]
            
            # 2. Parentheses
            while '(' in e:
                m = re.search(r'\(([^()]+)\)', e)
                if not m:
                    break
                inner = parse(m.group(1))
                e = e[:m.start()] + str(inner) + e[m.end():]
            
            # 3. Factorial
            fact_match = re.search(r'(\d+)!', e)
            if fact_match:
                n = int(fact_match.group(1))
                fact = 1
                for i in range(2, n + 1):
                    fact *= i
                e = e[:fact_match.start()] + str(fact) + e[fact_match.end():]
                return parse(e)
            
            # 4. Power
            pow_match = re.search(r'([\d.]+)\*\*([\d.]+)', e)
            if pow_match:
                base = float(pow_match.group(1))
                exp = float(pow_match.group(2))
                res = base ** exp
                e = e[:pow_match.start()] + str(res) + e[pow_match.end():]
                return parse(e)
            
            # 5. Unary minus
            if e.startswith('-'):
                e = '0' + e
            e = e.replace('--', '+').replace('+-', '-').replace('-+', '-')
            
            # 6. Tokenization and evaluation
            tokens = re.findall(r'[\d.]+|[+\-*/]', e)
            if not tokens:
                return 0.0
            if len(tokens) == 1:
                return float(tokens[0])
            
            # First handle * and /
            i = 1
            while i < len(tokens):
                if tokens[i] in ('*', '/'):
                    left = float(tokens[i - 1])
                    right = float(tokens[i + 1])
                    if tokens[i] == '*':
                        val = left * right
                    else:
                        val = left / right if right != 0 else 0.0
                    tokens[i - 1] = str(val)
                    del tokens[i:i + 2]
                else:
                    i += 2
            
            # Then handle + and -
            result = float(tokens[0])
            i = 1
            while i < len(tokens):
                if tokens[i] == '+':
                    result += float(tokens[i + 1])
                elif tokens[i] == '-':
                    result -= float(tokens[i + 1])
                i += 2
            return result
        
        result = parse(expr)
        result = round(result, 10)
        return int(result) if abs(result - int(result)) < 1e-12 else result
    
    except Exception:
        return None


def random_obj(lst):
    """Returns a random element from a list."""
    return lst[random.randint(0, len(lst)-1)]


def error(text):
    """Returns a string with bold red text."""
    return f"{bold}{red}{text}\033[0m"


def warn(text):
    """Returns a string with bold yellow text."""
    return f"{bold}{yellow}{text}\033[0m"


def success(text):
    """Returns a string with green text."""
    return f"{green}{text}\033[0m"


def info(text):
    """Returns a string with blue text."""
    return f"{blue}{text}\033[0m"


def levenshtein(a, b):
    """Calculates the Levenshtein distance between two strings."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(
                prev[j] + 1,
                cur[-1] + 1,
                prev[j - 1] + (ca != cb)
            ))
        prev = cur
    return prev[-1]


def sim(word1, word2, threshold=0.6):
    """
    Checks if two words are similar based on Levenshtein distance.
    
    Parameters:
        word1: first word
        word2: second word
        threshold: similarity threshold (0.0 to 1.0)
    """
    if not word1 or not word2:
        return False
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    max_len = max(len(word1), len(word2))
    if max_len == 0:
        return True
    
    distance = levenshtein(word1, word2)
    ratio = 1 - (distance / max_len)
    return ratio >= threshold


def formatcheck(word, typ):
    """Checks if an object is of a specified type."""
    return isinstance(word, typ)


first = 0
last = -1
rand = "random"  # Special value


def order(lst, mode):
    """
    Returns an element from a list based on mode.
    
    Parameters:
        lst: input list
        mode: first, last, or rand
    """
    if mode == first:
        return lst[first]
    elif mode == last:
        return lst[last]
    elif mode == rand:
        return random.choice(lst)


def wait(seconds):
    """Pauses execution for a specified number of seconds."""
    time.sleep(seconds)


def flatten(*lists):
    """Flattens multiple lists into a single list."""
    return sum(lists, [])


def integers_between(low, high):
    """Returns a list of integers from low to high inclusive."""
    return list(range(low, high + 1))


def around(number, target, deviation):
    """Checks if number is within target ± deviation."""
    # return target - deviation <= number <= target + deviation


def countdown(seconds, color=None, bgcolor=None, style=None):
    """
    Displays a countdown with overwrite support and colors.
    
    Parameters:
        seconds: starting number (counts down to 0)
        color: text color
        bgcolor: background color
        style: text style
    """
    max_len = len(str(seconds))
    
    prefix = ''
    if style:
        prefix += style
    if color:
        prefix += color
    if bgcolor:
        prefix += bgcolor
    
    if prefix:
        sys.stdout.write(prefix)
    
    for i in range(seconds, -1, -1):
        output = f"\r{i:>{max_len}}"
        sys.stdout.write(output)
        sys.stdout.flush()
        time.sleep(1)
    
    if prefix:
        sys.stdout.write('\033[0m')
    print()


def animate(frames, seconds=None, speed=5, color=None):
    """
    Displays a frame animation for a specified duration.
    
    Parameters:
        frames: list of frames to animate
        seconds: animation duration
        speed: frames per second
        color: animation color
    """
    import time as tm
    
    if color:
        sys.stdout.write(color)
    
    start_time = tm.time()
    i = 0
    
    while tm.time() - start_time < seconds:
        sys.stdout.write(f"\r{frames[i % len(frames)]}")
        sys.stdout.flush()
        tm.sleep(1 / speed)
        i += 1
    
    if color:
        sys.stdout.write('\033[0m')
    print()


def pulse(delay=0.1, bg_color=None):
    """Flashes the screen with a background color."""
    bgcolor(bg_color)
    time.sleep(delay)
    bgcolor()


def marquee(text, delay=0.1, width=40, repeat=1, color='', style='', bg_color=''):
    """
    Displays a scrolling marquee effect.
    
    Parameters:
        text: text to scroll
        delay: delay between frames
        width: display window width
        repeat: number of repetitions
        color: text color
        style: text style
        bg_color: background color
    """
    text = str(text)
    padded = ' ' * width + text + ' ' * width
    
    for _ in range(repeat):
        for i in range(len(padded) - width + 1):
            frame = padded[i:i+width]
            superprint(frame, delay=0, end='\r', color=color, style=style, bg_color=bg_color)
            time.sleep(delay)


def progress_bar(iteration, total, prefix='', suffix='', length=40, fill='█', empty='─', color=''):
    """
    Displays a progress bar.
    
    Parameters:
        iteration: current iteration
        total: total iterations
        prefix: text before bar
        suffix: text after bar
        length: bar length in characters
        fill: filled bar character
        empty: empty bar character
        color: bar color
    """
    percent = 100 * (iteration / float(total))
    filled = int(length * iteration // total)
    bar = fill * filled + empty * (length - filled)
    superprint(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}', delay=0, end='', color=color)
    if iteration == total:
        print()


def zen():
    """Prints the Zen of Python."""
    import this


def translate(text, dest='ru', src='en'):
    """
    Translates text using the free MyMemory API.
    
    Parameters:
        text: text to translate
        dest: destination language code ('ru', 'en', 'es', 'fr', 'de', etc.)
        src: source language code ('en', 'ru', 'auto' for automatic detection)
    
    Returns:
        str: translated text, or None on error
    """
    import urllib.request
    import urllib.parse
    import json
    
    try:
        if src == 'auto':
            if any(ord(c) > 1024 for c in text):
                src = 'ru'
            else:
                src = 'en'
        
        url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair={src}|{dest}"
        
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            translated = data["responseData"]["translatedText"]
            
            if translated == text:
                return None
            return translated
    except Exception:
        return None


def rand_password(length=12):
    """Generates a random password with letters, numbers, and symbols."""
    chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*"
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


def date(text):
    """
    Replaces date/time placeholders in text with actual values.
    
    Placeholders: Day, Month, Year, month, mon, yr, Hour, Minute, Second, Sec
    """
    now = datetime.datetime.now()
    
    return text.replace("Day", str(now.day))\
               .replace("Month", str(now.month))\
               .replace("Year", str(now.year))\
               .replace("month", now.strftime("%B"))\
               .replace("mon", now.strftime("%b"))\
               .replace("yr", now.strftime("%y"))\
               .replace("Hour", str(now.hour))\
               .replace("Minute", str(now.minute))\
               .replace("Second", str(now.second))\
               .replace("Sec", str(now.second))


def numeral(number, lang='ru'):
    """
    Converts a number to words in any language using translate().
    
    Parameters:
        number: integer to convert
        lang: target language code (default 'ru')
    """
    # English numeral base
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    special = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    thousands = ["", "one thousand", "two thousand", "three thousand", "four thousand", "five thousand", "six thousand", "seven thousand", "eight thousand", "nine thousand"]

    if number == 0:
        result = "zero"
    else:
        parts = []
        if number >= 1000:
            thousands_part = number // 1000
            parts.append(thousands[thousands_part])
            number %= 1000
        if number >= 100:
            hundreds_part = number // 100
            parts.append(hundreds[hundreds_part])
            number %= 100
        if number >= 20:
            tens_part = number // 10
            parts.append(tens[tens_part])
            number %= 10
            if number > 0:
                parts.append(units[number])
        elif 10 <= number <= 19:
            parts.append(special[number - 10])
        elif number > 0:
            parts.append(units[number])
        result = " ".join(parts).strip()

    if lang != 'en':
        result = translate(result, dest=lang, src='en')

    return result


def statlib(lib):
    """
    Displays PyPI download statistics for a library using pypistats.
    
    Parameters:
        lib: library name
    """
    try:
        try:
            import pypistats
        except ImportError:
            print("Download stats...")
            os.system("pip install pypistats")
        
        os.system(f"pypistats overall {lib}")
    except Exception as e:
        print(error("Error: ", e))


def incline(word, case):
    """
    Inflects a Russian word into a specified grammatical case.
    
    Parameters:
        word: word to inflect (Russian)
        case: grammatical case (e.g., 'nomn', 'gent', 'datv', 'accs', 'ablt', 'loct')
    
    Requires pymorphy3 library.
    """
    try:
        import pymorphy3
    except:
        os.system("pip install pymorphy3")
    import pymorphy3
    morph = pymorphy3.MorphAnalyzer()
    parsed = morph.parse(word)[0]
    return parsed.inflect({case}).word