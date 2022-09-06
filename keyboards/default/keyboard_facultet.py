from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_bf = KeyboardButton('Биологический факульет 🍃')
button_gf = KeyboardButton('Географический факульет 🗺')
button_gef = KeyboardButton('Геологический факульет ⛏')
button_is = KeyboardButton('Институт искусств 🎭')
button_imo = KeyboardButton('Институт истории и международных отношений  🎫')
button_f = KeyboardButton('Институт физики 🔧')
button_fks = KeyboardButton('Институт физической культуры и спорта  🥇')
button_fj = KeyboardButton('Институт филологии и журналистики 📜')
button_hm = KeyboardButton('Институт химии  👨‍🔬')
button_mm = KeyboardButton('Механико-математический факультет 🍻')
button_sc = KeyboardButton('Социологический факультет  🌐')
button_ill = KeyboardButton('Факультет иностранных языков и лингводидактики 🌍')
button_knt = KeyboardButton('Факультет компьютерных наук и информационных технологий  🖥')
button_psih = KeyboardButton('Факультет психологии 🤔')
button_ppso = KeyboardButton('Факультет психолого-педагогического и специального образования  👩‍🏫')
button_fmmt = KeyboardButton('Факультет фундаментальной медицины и медицинских технологий 🏥')
button_fil = KeyboardButton('Философский факультет 🤓')
button_ec = KeyboardButton('Экономический факультет 📈')
button_jud = KeyboardButton('Юридический факультет  ⚖')

facs = [
    'Биологический факульет 🍃',
    'Географический факульет 🗺',
    'Геологический факульет ⛏',
    'Институт искусств 🎭',
    'Институт истории и международных отношений  🎫',
    'Институт физики 🔧',
    'Институт физической культуры и спорта  🥇',
    'Институт филологии и журналистики 📜',
    'Институт химии  👨‍🔬',
    'Механико-математический факультет 🍻',
    'Социологический факультет  🌐',
    'Факультет иностранных языков и лингводидактики 🌍',
    'Факультет компьютерных наук и информационных технологий  🖥',
    'Факультет психологии 🤔',
    'Факультет психолого-педагогического и специального образования  👩‍🏫',
    'Факультет фундаментальной медицины и медицинских технологий 🏥',
    'Философский факультет 🤓',
    'Экономический факультет 📈',
    'Юридический факультет  ⚖'
]

facultets_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_bf).add(button_gf).add(button_gef).add(button_is)\
    .add(button_imo).add(button_f).add(button_fks).add(button_fj).add(button_hm).add(button_mm).add(button_sc).add(button_ill)\
    .add(button_knt).add(button_psih).add(button_ppso).add(button_fmmt).add(button_fil).add(button_ec).add(button_jud)

