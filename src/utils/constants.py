# constants.py
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ['Brigide', 'Imbolka', 'Floralis', 'Lithara', 'Heliax', 'Aestium', 'Mabonel', 'Ceresio', 'Yulith', 'Hibernis']
DAY_NAMES = ['Restony', 'Serement', 'Chronesis', 'Tempetude', 'Solament', 'Helioris', 'Duratonis', 'Resporal', 'Sabbathal', 'Noctitude']

# Character Needs
MAX_HUNGER = 100
MAX_THIRST = 100
MAX_ENERGY = 100
MAX_SOCIAL = 100
MAX_RELIEF = 100
MAX_CLEANLINESS = 100
MAX_COMFORT = 100
MAX_SAFETY = 100
MAX_HEALTH = 100

MIN_HUNGER = 0
MIN_THIRST = 0
MIN_ENERGY = 0
MIN_SOCIAL = 0
MIN_RELIEF = 0
MIN_CLEANLINESS = 0
MIN_COMFORT = 0
MIN_SAFETY = 0
MIN_HEALTH = 0

# Decay rates
HUNGER_DECAY = 2  # 2 points every in-game hour
THIRST_DECAY = 3  # 3 points every in-game hour
ENERGY_DECAY = 1  # 1 point every in-game hour
SOCIAL_DECAY = 1  # 1 point every in-game hour
RELIEF_DECAY = 2  # 2 points every in-game hour
CLEANLINESS_DECAY = 0.5  # 0.5 points every in-game hour
COMFORT_DECAY = 1  # 1 point every in-game hour
SAFETY_DECAY = 0.2  # 0.2 points every in-game hour
HEALTH_DECAY = 0.1  # 0.1 points every in-game hour


# Character Traits
SEX = ['x', 'y']
GENDER = ['masc', 'fem', 'androgynous']
TONE = ['pale', 'medium', 'tan', 'dark', 'deep']
UNDERTONE = ['warm', 'neutral', 'cool']
HEIGHT = ['short', 'average', 'tall']
BSHAPE = ['slim', 'average', 'athletic', 'curvy']
BSIZE = ['small', 'medium', 'large']
HCOLOR = ['black', 'brown', 'blonde', 'ginger']
HTEXT = ['straight', 'wavy', 'curly']
ESHAPE = ['round', 'almond', 'upturned', 'downturned', 'hooded']
ECOLOR = ['brown', 'hazel', 'green', 'blue', 'grey']
NPROFILE = ['small', 'medium', 'tall']
NSHAPE = ['refined', 'hero', 'soft', 'perky', 'dainty', 'strong', 'bulb']
MSHAPE = ['thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped']
RSHAPE = ['round', 'pointed']
RSIZE = ['small', 'medium', 'large']


RESPONSES = ['recpetive', 'motive', 'apprehensive', 'refusal']

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

TRAITS = {
    'temperament': {
        'positive': ['easy-going', 'adaptable', 'content', 'cheerful', 'calm'],
        'neutral': ['active', 'regular', 'slow-to-warm-up', 'moderate', 'observant'],
        'negative': ['fussy', 'irritable', 'unpredictable', 'restless', 'overactive']
    }, 
    'socialization': {
        'positive': ['sociable', 'playful', 'affectionate', 'friendly', 'engaging'],
        'neutral': ['observant', 'independent', 'cautious', 'curious', 'mellow'],
        'negative': ['clingy', 'aggressive', 'withdrawn', 'hyperactive', 'impulsive']
    },
    'emotional': {
        'positive': ['cheerful', 'calm', 'optimistic', 'joyful', 'hopeful'],
        'neutral': ['sensitive', 'passionate', 'reflective', 'balanced', 'realistic'],
        'negative': ['moody', 'anxious', 'pessimistic', 'irritable', 'doubtful']
    },
    'interaction': {
        'positive': ['friendly', 'cooperative', 'empathetic', 'supportive', 'generous'],
        'neutral': ['reserved', 'independent', 'adaptable', 'neutral', 'pragmatic'],
        'negative': ['shy', 'confrontational', 'manipulative', 'aloof', 'dismissive']
    },
    'cognition': {
        'positive': ['curious', 'diligent', 'creative', 'inquisitive', 'motivated'],
        'neutral': ['practical', 'analytical', 'intuitive', 'theoretical', 'exploratory'],
        'negative': ['distracted', 'stubborn', 'uncritical', 'complacent', 'disinterested']
    },
    'identity': {
        'positive': ['confident', 'principled', 'open-minded', 'self-aware', 'authentic'],
        'neutral': ['questioning', 'experimental', 'idealistic', 'reflective', 'curious'],
        'negative': ['insecure', 'conformist', 'rebellious', 'conflicted', 'doubtful']
    }, 
    'ambition': {
        'positive': ['ambitious', 'dedicated', 'innovative', 'goal-oriented', 'driven'],
        'neutral': ['flexible', 'specialized', 'risk-taking', 'pragmatic', 'adaptable'],
        'negative': ['unmotivated', 'workaholic', 'indecisive', 'complacent', 'disengaged']
    },
    'morals': {
        'positive': ['honest', 'compassionate', 'resilient', 'fair-minded', 'generous'],
        'neutral': ['traditional', 'pragmatic', 'individualistic', 'balanced', 'neutral'],
        'negative': ['materialistic', 'judgmental', 'hedonistic', ' selfish', 'cynical']
    },
    'perspective': {
        'positive': ['wise', 'content', 'grateful', 'optimistic', 'hopeful'],
        'neutral': ['philosophical', 'nostalgic', 'accepting', 'realistic', 'pragmatic'],
        'negative': ['cynical', 'regretful', 'bitter', 'pessimistic', 'resentful']
    },
    'legacy': {
        'positive': ['mentoring', 'philanthropic', 'inspiring', 'guiding', 'visionary'],
        'neutral': ['reflective', 'private', 'traditional', 'conservative', 'practical'],
        'negative': ['disengaged', 'controlling', 'resentful', 'Manipulative', 'Detached']
    }
}

CATAGORIES_PER_AGE = {
    AGES[0]: [TRAITS[0]],
    AGES[1]: [TRAITS[0], TRAITS[1]],
    AGES[2]: [TRAITS[2], TRAITS[3], TRAITS[4]],
    AGES[3]: [TRAITS[2], TRAITS[3], TRAITS[4], TRAITS[5]],
    AGES[4]: [TRAITS[2], TRAITS[3], TRAITS[6], TRAITS[7]],
    AGES[5]: [TRAITS[2], TRAITS[3], TRAITS[6], TRAITS[7], TRAITS[8]],
    AGES[6]: [TRAITS[2], TRAITS[3], TRAITS[7], TRAITS[8], TRAITS[9]]
}
TRAIT_EVOLUTIONS = [
    ('curious', 'inquisitive', 'AGES[3]'),
    ('inquisitive', 'analytical', 'AGES[4]'),
    ('cheerful', 'optimistic', 'AGES[3]'),
    ('optimistic', 'resilient', 'AGES[5]'),
    ('friendly', 'empathetic', 'AGES[3]'),
    ('empathetic', 'compassionate', 'AGES[5]'),
    ('diligent', 'dedicated', 'AGES[4]'),
    ('dedicated', 'ambitious', 'AGES[5]'),
    ('creative', 'innovative', 'AGES[4]'),
    ('innovative', 'visionary', 'AGES[5]'),
    ('shy', 'reserved', 'AGES[3]'),
    ('reserved', 'independent', 'AGES[5]'),
    ('moody', 'passionate', 'AGES[3]'),
    ('passionate', 'intense', 'AGES[5]'),
    ('anxious', 'sensitive', 'AGES[3]'),
    ('sensitive', 'reflective', 'AGES[5]'),
    ('pessimistic', 'cynical', 'AGES[3]'),
    ('cynical', 'resentful', 'AGES[5]'),
    ('conformist', 'traditional', 'AGES[5]'),
    ('rebellious', 'nonconformist', 'AGES[5]'),
    ('insecure', 'self-doubting', 'AGES[5]'),
    ('stubborn', 'unyielding', 'AGES[3]'),
    ('uncritical', 'naive', 'AGES[3]'),
    ('distracted', 'disorganized', 'AGES[3]'),
    ('manipulative', 'deceptive', 'AGES[5]'),
    ('confrontational', 'aggressive', 'AGES[5]'),
    ('workaholic', 'obsessive', 'AGES[5]'),
    ('indecisive', 'hesitant', 'AGES[5]'),
    ('materialistic', 'greedy', 'AGES[5]'),
    ('judgmental', 'critical', 'AGES[5]'),
    ('hedonistic', 'self-indulgent', 'AGES[5]'),
    ('cynical', 'jaded', 'AGES[6]'),
    ('regretful', 'remorseful', 'AGES[6]'),
    ('bitter', 'resentful', 'AGES[6]'),
    ('disengaged', 'detached', 'AGES[6]'),
    ('controlling', 'manipulative', 'AGES[6]'),
    ('resentful', 'vindictive', 'AGES[6]'),
    ('mentoring', 'guiding', 'AGES[6]'),
    ('philanthropic', 'altruistic', 'AGES[6]'),
    ('inspiring', 'visionary', 'AGES[6]'),
    ('reflective', 'introspective', 'AGES[6]'),
    ('private', 'reserved', 'AGES[6]'),
    ('traditional', 'conservative', 'AGES[6]'),
    ('adaptable', 'easy-going', 'AGES[1]'),
    ('engaging', 'sociable', 'AGES[2]'),
    ('hopeful', 'joyful', 'AGES[3]'),
    ('self-aware', 'confident', 'AGES[4]'),
    ('goal-oriented', 'AGES[4]', 'ambitious', 'AGES[5]'),
    ('generous', 'compassionate', 'AGES[6]'),
    ('pragmatic', 'neutral', 'AGES[4]'),
    ('mellow', 'balanced', 'AGES[3]'),
    ('reflective', 'philosophical', 'AGES[5]'),
    ('authentic', 'principled', 'AGES[5]'),
]

TRAIT_SYNERGIES = [
    (('curious', 'inquisitive'), 'enhances learning speed for knowledge-seeking skills'),
    (('cheerful', 'optimistic'), 'boosts creativity-related skill gains'),
    (('friendly', 'empathetic'), 'improves social relationships and diplomacy'),
    (('diligent', 'dedicated'), 'increases productivity and work efficiency'),
    (('creative', 'innovative'), 'enhances problem-solving and critical thinking'),
    (('shy', 'reserved'), 'reduces social anxiety and improves self-confidence'),
    (('moody', 'passionate'), 'increases emotional intensity and creativity'),
    (('anxious', 'sensitive'), 'improves emotional intelligence and empathy'),
    (('pessimistic', 'cynical'), 'increases critical thinking and skepticism'),
    (('conformist', 'traditional'), 'improves social standing and reputation'),
    (('rebellious', 'nonconformist'), 'increases independence and self-reliance'),
    (('insecure', 'self-doubting'), 'improves self-awareness and personal growth'),
    (('stubborn', 'unyielding'), 'increases determination and perseverance'),
    (('uncritical', 'naive'), 'improves open-mindedness and adaptability'),
    (('distracted', 'disorganized'), 'reduces procrastination and improves time management'),
    (('manipulative', 'deceptive'), 'increases persuasion and negotiation skills'),
    (('confrontational', 'aggressive'), 'increases assertiveness and conflict resolution skills'),
    (('workaholic', 'obsessive'), 'increases productivity and work efficiency'),
    (('indecisive', 'hesitant'), 'improves decision-making and risk-taking'),
    (('materialistic', 'greedy'), 'increases wealth and material possessions'),
    (('judgmental', 'critical'), 'increases critical thinking and discernment'),
    (('hedonistic', 'self-indulgent'), 'increases pleasure and enjoyment'),
    (('cynical', 'jaded'), 'increases skepticism and critical thinking'),
    (('regretful', 'remorseful'), 'improves self-awareness and personal growth'),
    (('bitter', 'resentful'), 'increases emotional intensity and motivation'),
    (('disengaged', 'detached'), 'reduces emotional attachment and increases independence'),
    (('controlling', 'manipulative'), 'increases persuasion and negotiation skills'),
    (('resentful', 'vindictive'), 'increases motivation and drive'),
    (('mentoring', 'guiding'), 'improves leadership and teaching skills'),
    (('philanthropic', 'altruistic'), 'increases generosity and kindness'),
    (('inspiring', 'visionary'), 'increases charisma and leadership skills'),
    (('reflective', 'introspective'), 'improves self-awareness and personal growth'),
    (('private', 'reserved'), 'reduces social anxiety and improves self-confidence'),
    (('traditional', 'conservative'), 'improves social standing and reputation'),
    (('adaptable', 'easy-going'), 'enhances flexibility and stress management'),
    (('engaging', 'sociable'), 'boosts charisma and social influence'),
    (('hopeful', 'joyful'), 'increases resilience and positivity'),
    (('self-aware', 'confident'), 'enhances personal growth and self-acceptance'),
    (('goal-oriented', 'ambitious'), 'increases focus and achievement'),
    (('generous', 'compassionate'), 'strengthens community bonds and support'),
    (('pragmatic', 'flexible'), 'improves problem-solving and adaptability'),
    (('mellow', 'balanced'), 'enhances emotional stability and calmness'),
    (('reflective', 'philosophical'), 'deepens understanding and wisdom'),
    (('authentic', 'principled'), 'promotes integrity and trustworthiness'),
]

skills = {
    'food'
}
print(TRAITS[0[0[0]]])