from enum import Enum, auto
from unittest import TestCase


class LanguageCode(Enum):
    EnglishLegacy = auto()
    Afar = auto()
    Abkhazian = auto()
    Afrikaans = auto()
    Amharic = auto()
    Arabic = auto()
    Assamese = auto()
    Aymara = auto()
    Azerbaijani = auto()
    Bashkir = auto()
    Byelorussian = auto()
    Bulgarian = auto()
    Bihari = auto()
    Bislama = auto()
    Bengali = auto()
    Tibetan = auto()
    Breton = auto()
    Catalan = auto()
    Corsican = auto()
    Czech = auto()
    Welsh = auto()
    Danish = auto()
    German = auto()
    Bhutani = auto()
    Greek = auto()
    English = auto()
    Esperanto = auto()
    Spanish = auto()
    Estonian = auto()
    Basque = auto()
    Persian = auto()
    Finnish = auto()
    Fiji = auto()
    Faeroese = auto()
    French = auto()
    Frisian = auto()
    Irish = auto()
    ScotsGaelic = auto()
    Galician = auto()
    Guarani = auto()
    Gijarati = auto()
    Hausa = auto()
    Hindi = auto()
    Croatian = auto()
    Hungarian = auto()
    Armenian = auto()
    Interlingua = auto()
    Interlingue = auto()
    Inupiak = auto()
    Indonesian = auto()
    Icelandic = auto()
    Italian = auto()
    Hebrew = auto()
    Japanese = auto()
    Yiddish = auto()
    Javanese = auto()
    Georgian = auto()
    Kazakh = auto()
    Greenlandic = auto()
    Cambodian = auto()
    Kannada = auto()
    Korean = auto()
    Kashmiri = auto()
    Kurdish = auto()
    Kirghiz = auto()
    Latin = auto()
    Lingala = auto()
    Laothian = auto()
    Lithuanian = auto()
    Latvian = auto()
    Malagasy = auto()
    Maori = auto()
    Macedonian = auto()
    Malayalam = auto()
    Mongolian = auto()
    Moldavian = auto()
    Marathi = auto()
    Malay = auto()
    Maltese = auto()
    Burmese = auto()
    Nauru = auto()
    Nepali = auto()
    Dutch = auto()
    Norwegian = auto()
    Occitan = auto()
    Oromo = auto()
    Oriya = auto()
    Punjabi = auto()
    Polish = auto()
    Pashto = auto()
    Portuguese = auto()
    Quechua = auto()
    RhaetoRomance = auto()
    Kirundi = auto()
    Romanian = auto()
    Russian = auto()
    Kinyarwanda = auto()
    Sanskrit = auto()
    Sindhi = auto()
    Sangro = auto()
    SerboCroatian = auto()
    Singhalese = auto()
    Slovak = auto()
    Slovenian = auto()
    Samoan = auto()
    Shona = auto()
    Somali = auto()
    Albanian = auto()
    Serbian = auto()
    Siswati = auto()
    Sesotho = auto()
    Sudanese = auto()
    Swedish = auto()
    Swahili = auto()
    Tamil = auto()
    Tegulu = auto()
    Tajik = auto()
    Thai = auto()
    Tigrinya = auto()
    Turkmen = auto()
    Tagalog = auto()
    Setswana = auto()
    Tonga = auto()
    Turkish = auto()
    Tsonga = auto()
    Tatar = auto()
    Twi = auto()
    Ukrainian = auto()
    Urda = auto()
    Uzbek = auto()
    Vietnamese = auto()
    Volapuk = auto()
    Wolof = auto()
    Xhosa = auto()
    Yoruba = auto()
    Chinese = auto()
    Zulu = auto()


INDEX_TO_LANGUAGE_CODE_MAP = [
    LanguageCode.EnglishLegacy,
    LanguageCode.Afar,
    LanguageCode.Abkhazian,
    LanguageCode.Afrikaans,
    LanguageCode.Amharic,
    LanguageCode.Arabic,
    LanguageCode.Assamese,
    LanguageCode.Aymara,
    LanguageCode.Azerbaijani,
    LanguageCode.Bashkir,
    LanguageCode.Byelorussian,
    LanguageCode.Bulgarian,
    LanguageCode.Bihari,
    LanguageCode.Bislama,
    LanguageCode.Bengali,
    LanguageCode.Tibetan,
    LanguageCode.Breton,
    LanguageCode.Catalan,
    LanguageCode.Corsican,
    LanguageCode.Czech,
    LanguageCode.Welsh,
    LanguageCode.Danish,
    LanguageCode.German,
    LanguageCode.Bhutani,
    LanguageCode.Greek,
    LanguageCode.English,
    LanguageCode.Esperanto,
    LanguageCode.Spanish,
    LanguageCode.Estonian,
    LanguageCode.Basque,
    LanguageCode.Persian,
    LanguageCode.Finnish,
    LanguageCode.Fiji,
    LanguageCode.Faeroese,
    LanguageCode.French,
    LanguageCode.Frisian,
    LanguageCode.Irish,
    LanguageCode.ScotsGaelic,
    LanguageCode.Galician,
    LanguageCode.Guarani,
    LanguageCode.Gijarati,
    LanguageCode.Hausa,
    LanguageCode.Hindi,
    LanguageCode.Croatian,
    LanguageCode.Hungarian,
    LanguageCode.Armenian,
    LanguageCode.Interlingua,
    LanguageCode.Interlingue,
    LanguageCode.Inupiak,
    LanguageCode.Indonesian,
    LanguageCode.Icelandic,
    LanguageCode.Italian,
    LanguageCode.Hebrew,
    LanguageCode.Japanese,
    LanguageCode.Yiddish,
    LanguageCode.Javanese,
    LanguageCode.Georgian,
    LanguageCode.Kazakh,
    LanguageCode.Greenlandic,
    LanguageCode.Cambodian,
    LanguageCode.Kannada,
    LanguageCode.Korean,
    LanguageCode.Kashmiri,
    LanguageCode.Kurdish,
    LanguageCode.Kirghiz,
    LanguageCode.Latin,
    LanguageCode.Lingala,
    LanguageCode.Laothian,
    LanguageCode.Lithuanian,
    LanguageCode.Latvian,
    LanguageCode.Malagasy,
    LanguageCode.Maori,
    LanguageCode.Macedonian,
    LanguageCode.Malayalam,
    LanguageCode.Mongolian,
    LanguageCode.Moldavian,
    LanguageCode.Marathi,
    LanguageCode.Malay,
    LanguageCode.Maltese,
    LanguageCode.Burmese,
    LanguageCode.Nauru,
    LanguageCode.Nepali,
    LanguageCode.Dutch,
    LanguageCode.Norwegian,
    LanguageCode.Occitan,
    LanguageCode.Oromo,
    LanguageCode.Oriya,
    LanguageCode.Punjabi,
    LanguageCode.Polish,
    LanguageCode.Pashto,
    LanguageCode.Portuguese,
    LanguageCode.Quechua,
    LanguageCode.RhaetoRomance,
    LanguageCode.Kirundi,
    LanguageCode.Romanian,
    LanguageCode.Russian,
    LanguageCode.Kinyarwanda,
    LanguageCode.Sanskrit,
    LanguageCode.Sindhi,
    LanguageCode.Sangro,
    LanguageCode.SerboCroatian,
    LanguageCode.Singhalese,
    LanguageCode.Slovak,
    LanguageCode.Slovenian,
    LanguageCode.Samoan,
    LanguageCode.Shona,
    LanguageCode.Somali,
    LanguageCode.Albanian,
    LanguageCode.Serbian,
    LanguageCode.Siswati,
    LanguageCode.Sesotho,
    LanguageCode.Sudanese,
    LanguageCode.Swedish,
    LanguageCode.Swahili,
    LanguageCode.Tamil,
    LanguageCode.Tegulu,
    LanguageCode.Tajik,
    LanguageCode.Thai,
    LanguageCode.Tigrinya,
    LanguageCode.Turkmen,
    LanguageCode.Tagalog,
    LanguageCode.Setswana,
    LanguageCode.Tonga,
    LanguageCode.Turkish,
    LanguageCode.Tsonga,
    LanguageCode.Tatar,
    LanguageCode.Twi,
    LanguageCode.Ukrainian,
    LanguageCode.Urda,
    LanguageCode.Uzbek,
    LanguageCode.Vietnamese,
    LanguageCode.Volapuk,
    LanguageCode.Wolof,
    LanguageCode.Xhosa,
    LanguageCode.Yoruba,
    LanguageCode.Chinese,
    LanguageCode.Zulu,
]


LANGUAGE_CODE_TO_NAME_MAP = {
    LanguageCode.EnglishLegacy: "legacy_english",
    LanguageCode.Afar: "afar",
    LanguageCode.Abkhazian: "abkhazian",
    LanguageCode.Afrikaans: "afrikaans",
    LanguageCode.Amharic: "amharic",
    LanguageCode.Arabic: "arabic",
    LanguageCode.Assamese: "assamese",
    LanguageCode.Aymara: "aymara",
    LanguageCode.Azerbaijani: "azerbaijani",
    LanguageCode.Bashkir: "bashkir",
    LanguageCode.Byelorussian: "byelorussian",
    LanguageCode.Bulgarian: "bulgarian",
    LanguageCode.Bihari: "bihari",
    LanguageCode.Bislama: "bislama",
    LanguageCode.Bengali: "bengali",
    LanguageCode.Tibetan: "tibetan",
    LanguageCode.Breton: "breton",
    LanguageCode.Catalan: "catalan",
    LanguageCode.Corsican: "corsican",
    LanguageCode.Czech: "czech",
    LanguageCode.Welsh: "welsh",
    LanguageCode.Danish: "danish",
    LanguageCode.German: "german",
    LanguageCode.Bhutani: "bhutani",
    LanguageCode.Greek: "greek",
    LanguageCode.English: "english",
    LanguageCode.Esperanto: "esperanto",
    LanguageCode.Spanish: "spanish",
    LanguageCode.Estonian: "estonian",
    LanguageCode.Basque: "basque",
    LanguageCode.Persian: "persian",
    LanguageCode.Finnish: "finnish",
    LanguageCode.Fiji: "fiji",
    LanguageCode.Faeroese: "faeroese",
    LanguageCode.French: "french",
    LanguageCode.Frisian: "frisian",
    LanguageCode.Irish: "irish",
    LanguageCode.ScotsGaelic: "scotsgaelic",
    LanguageCode.Galician: "galician",
    LanguageCode.Guarani: "guarani",
    LanguageCode.Gijarati: "gijarati",
    LanguageCode.Hausa: "hausa",
    LanguageCode.Hindi: "hindi",
    LanguageCode.Croatian: "croatian",
    LanguageCode.Hungarian: "hungarian",
    LanguageCode.Armenian: "armenian",
    LanguageCode.Interlingua: "interlingua",
    LanguageCode.Interlingue: "interlingue",
    LanguageCode.Inupiak: "inupiak",
    LanguageCode.Indonesian: "indonesian",
    LanguageCode.Icelandic: "icelandic",
    LanguageCode.Italian: "italian",
    LanguageCode.Hebrew: "hebrew",
    LanguageCode.Japanese: "japanese",
    LanguageCode.Yiddish: "yiddish",
    LanguageCode.Javanese: "javanese",
    LanguageCode.Georgian: "georgian",
    LanguageCode.Kazakh: "kazakh",
    LanguageCode.Greenlandic: "greenlandic",
    LanguageCode.Cambodian: "cambodian",
    LanguageCode.Kannada: "kannada",
    LanguageCode.Korean: "korean",
    LanguageCode.Kashmiri: "kashmiri",
    LanguageCode.Kurdish: "kurdish",
    LanguageCode.Kirghiz: "kirghiz",
    LanguageCode.Latin: "latin",
    LanguageCode.Lingala: "lingala",
    LanguageCode.Laothian: "laothian",
    LanguageCode.Lithuanian: "lithuanian",
    LanguageCode.Latvian: "latvian",
    LanguageCode.Malagasy: "malagasy",
    LanguageCode.Maori: "maori",
    LanguageCode.Macedonian: "macedonian",
    LanguageCode.Malayalam: "malayalam",
    LanguageCode.Mongolian: "mongolian",
    LanguageCode.Moldavian: "moldavian",
    LanguageCode.Marathi: "marathi",
    LanguageCode.Malay: "malay",
    LanguageCode.Maltese: "maltese",
    LanguageCode.Burmese: "burmese",
    LanguageCode.Nauru: "nauru",
    LanguageCode.Nepali: "nepali",
    LanguageCode.Dutch: "dutch",
    LanguageCode.Norwegian: "norwegian",
    LanguageCode.Occitan: "occitan",
    LanguageCode.Oromo: "oromo",
    LanguageCode.Oriya: "oriya",
    LanguageCode.Punjabi: "punjabi",
    LanguageCode.Polish: "polish",
    LanguageCode.Pashto: "pashto",
    LanguageCode.Portuguese: "portuguese",
    LanguageCode.Quechua: "quechua",
    LanguageCode.RhaetoRomance: "rhaetoromance",
    LanguageCode.Kirundi: "kirundi",
    LanguageCode.Romanian: "romanian",
    LanguageCode.Russian: "russian",
    LanguageCode.Kinyarwanda: "kinyarwanda",
    LanguageCode.Sanskrit: "sanskrit",
    LanguageCode.Sindhi: "sindhi",
    LanguageCode.Sangro: "sangro",
    LanguageCode.SerboCroatian: "serbocroatian",
    LanguageCode.Singhalese: "singhalese",
    LanguageCode.Slovak: "slovak",
    LanguageCode.Slovenian: "slovenian",
    LanguageCode.Samoan: "samoan",
    LanguageCode.Shona: "shona",
    LanguageCode.Somali: "somali",
    LanguageCode.Albanian: "albanian",
    LanguageCode.Serbian: "serbian",
    LanguageCode.Siswati: "siswati",
    LanguageCode.Sesotho: "sesotho",
    LanguageCode.Sudanese: "sudanese",
    LanguageCode.Swedish: "swedish",
    LanguageCode.Swahili: "swahili",
    LanguageCode.Tamil: "tamil",
    LanguageCode.Tegulu: "tegulu",
    LanguageCode.Tajik: "tajik",
    LanguageCode.Thai: "thai",
    LanguageCode.Tigrinya: "tigrinya",
    LanguageCode.Turkmen: "turkmen",
    LanguageCode.Tagalog: "tagalog",
    LanguageCode.Setswana: "setswana",
    LanguageCode.Tonga: "tonga",
    LanguageCode.Turkish: "turkish",
    LanguageCode.Tsonga: "tsonga",
    LanguageCode.Tatar: "tatar",
    LanguageCode.Twi: "twi",
    LanguageCode.Ukrainian: "ukrainian",
    LanguageCode.Urda: "urda",
    LanguageCode.Uzbek: "uzbek",
    LanguageCode.Vietnamese: "vietnamese",
    LanguageCode.Volapuk: "volapuk",
    LanguageCode.Wolof: "wolof",
    LanguageCode.Xhosa: "xhosa",
    LanguageCode.Yoruba: "yoruba",
    LanguageCode.Chinese: "chinese",
    LanguageCode.Zulu: "zulu",
}

LANGUAGE_CODE_TO_INDEX_MAP = {
    LanguageCode.EnglishLegacy: 0,  # 0 is also english, but it's reserved for EEPROM
    LanguageCode.Afar: 1,
    LanguageCode.Abkhazian: 2,
    LanguageCode.Afrikaans: 3,
    LanguageCode.Amharic: 4,
    LanguageCode.Arabic: 5,
    LanguageCode.Assamese: 6,
    LanguageCode.Aymara: 7,
    LanguageCode.Azerbaijani: 8,
    LanguageCode.Bashkir: 9,
    LanguageCode.Byelorussian: 10,
    LanguageCode.Bulgarian: 11,
    LanguageCode.Bihari: 12,
    LanguageCode.Bislama: 13,
    LanguageCode.Bengali: 14,
    LanguageCode.Tibetan: 15,
    LanguageCode.Breton: 16,
    LanguageCode.Catalan: 17,
    LanguageCode.Corsican: 18,
    LanguageCode.Czech: 19,
    LanguageCode.Welsh: 20,
    LanguageCode.Danish: 21,
    LanguageCode.German: 22,
    LanguageCode.Bhutani: 23,
    LanguageCode.Greek: 24,
    LanguageCode.English: 25,
    LanguageCode.Esperanto: 26,
    LanguageCode.Spanish: 27,
    LanguageCode.Estonian: 28,
    LanguageCode.Basque: 29,
    LanguageCode.Persian: 30,
    LanguageCode.Finnish: 31,
    LanguageCode.Fiji: 32,
    LanguageCode.Faeroese: 33,
    LanguageCode.French: 34,
    LanguageCode.Frisian: 35,
    LanguageCode.Irish: 36,
    LanguageCode.ScotsGaelic: 37,
    LanguageCode.Galician: 38,
    LanguageCode.Guarani: 39,
    LanguageCode.Gijarati: 40,
    LanguageCode.Hausa: 41,
    LanguageCode.Hindi: 42,
    LanguageCode.Croatian: 43,
    LanguageCode.Hungarian: 44,
    LanguageCode.Armenian: 45,
    LanguageCode.Interlingua: 46,
    LanguageCode.Interlingue: 47,
    LanguageCode.Inupiak: 48,
    LanguageCode.Indonesian: 49,
    LanguageCode.Icelandic: 50,
    LanguageCode.Italian: 51,
    LanguageCode.Hebrew: 52,
    LanguageCode.Japanese: 53,
    LanguageCode.Yiddish: 54,
    LanguageCode.Javanese: 55,
    LanguageCode.Georgian: 56,
    LanguageCode.Kazakh: 57,
    LanguageCode.Greenlandic: 58,
    LanguageCode.Cambodian: 59,
    LanguageCode.Kannada: 60,
    LanguageCode.Korean: 61,
    LanguageCode.Kashmiri: 62,
    LanguageCode.Kurdish: 63,
    LanguageCode.Kirghiz: 64,
    LanguageCode.Latin: 65,
    LanguageCode.Lingala: 66,
    LanguageCode.Laothian: 67,
    LanguageCode.Lithuanian: 68,
    LanguageCode.Latvian: 69,
    LanguageCode.Malagasy: 70,
    LanguageCode.Maori: 71,
    LanguageCode.Macedonian: 72,
    LanguageCode.Malayalam: 73,
    LanguageCode.Mongolian: 74,
    LanguageCode.Moldavian: 75,
    LanguageCode.Marathi: 76,
    LanguageCode.Malay: 77,
    LanguageCode.Maltese: 78,
    LanguageCode.Burmese: 79,
    LanguageCode.Nauru: 80,
    LanguageCode.Nepali: 81,
    LanguageCode.Dutch: 82,
    LanguageCode.Norwegian: 83,
    LanguageCode.Occitan: 84,
    LanguageCode.Oromo: 85,
    LanguageCode.Oriya: 86,
    LanguageCode.Punjabi: 87,
    LanguageCode.Polish: 88,
    LanguageCode.Pashto: 89,
    LanguageCode.Portuguese: 90,
    LanguageCode.Quechua: 91,
    LanguageCode.RhaetoRomance: 92,
    LanguageCode.Kirundi: 93,
    LanguageCode.Romanian: 94,
    LanguageCode.Russian: 95,
    LanguageCode.Kinyarwanda: 96,
    LanguageCode.Sanskrit: 97,
    LanguageCode.Sindhi: 98,
    LanguageCode.Sangro: 99,
    LanguageCode.SerboCroatian: 100,
    LanguageCode.Singhalese: 101,
    LanguageCode.Slovak: 102,
    LanguageCode.Slovenian: 103,
    LanguageCode.Samoan: 104,
    LanguageCode.Shona: 105,
    LanguageCode.Somali: 106,
    LanguageCode.Albanian: 107,
    LanguageCode.Serbian: 108,
    LanguageCode.Siswati: 109,
    LanguageCode.Sesotho: 110,
    LanguageCode.Sudanese: 111,
    LanguageCode.Swedish: 112,
    LanguageCode.Swahili: 113,
    LanguageCode.Tamil: 114,
    LanguageCode.Tegulu: 115,
    LanguageCode.Tajik: 116,
    LanguageCode.Thai: 117,
    LanguageCode.Tigrinya: 118,
    LanguageCode.Turkmen: 119,
    LanguageCode.Tagalog: 120,
    LanguageCode.Setswana: 121,
    LanguageCode.Tonga: 122,
    LanguageCode.Turkish: 123,
    LanguageCode.Tsonga: 124,
    LanguageCode.Tatar: 125,
    LanguageCode.Twi: 126,
    LanguageCode.Ukrainian: 127,
    LanguageCode.Urda: 128,
    LanguageCode.Uzbek: 129,
    LanguageCode.Vietnamese: 130,
    LanguageCode.Volapuk: 131,
    LanguageCode.Wolof: 132,
    LanguageCode.Xhosa: 133,
    LanguageCode.Yoruba: 134,
    LanguageCode.Chinese: 135,
    LanguageCode.Zulu: 136,
}

NAME_TO_LANGUAGE_CODE_MAP = {
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.EnglishLegacy]: LanguageCode.EnglishLegacy,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Afar]: LanguageCode.Afar,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Abkhazian]: LanguageCode.Abkhazian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Afrikaans]: LanguageCode.Afrikaans,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Amharic]: LanguageCode.Amharic,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Arabic]: LanguageCode.Arabic,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Assamese]: LanguageCode.Assamese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Aymara]: LanguageCode.Aymara,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Azerbaijani]: LanguageCode.Azerbaijani,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bashkir]: LanguageCode.Bashkir,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Byelorussian]: LanguageCode.Byelorussian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bulgarian]: LanguageCode.Bulgarian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bihari]: LanguageCode.Bihari,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bislama]: LanguageCode.Bislama,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bengali]: LanguageCode.Bengali,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tibetan]: LanguageCode.Tibetan,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Breton]: LanguageCode.Breton,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Catalan]: LanguageCode.Catalan,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Corsican]: LanguageCode.Corsican,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Czech]: LanguageCode.Czech,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Welsh]: LanguageCode.Welsh,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Danish]: LanguageCode.Danish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.German]: LanguageCode.German,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Bhutani]: LanguageCode.Bhutani,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Greek]: LanguageCode.Greek,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.English]: LanguageCode.English,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Esperanto]: LanguageCode.Esperanto,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Spanish]: LanguageCode.Spanish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Estonian]: LanguageCode.Estonian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Basque]: LanguageCode.Basque,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Persian]: LanguageCode.Persian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Finnish]: LanguageCode.Finnish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Fiji]: LanguageCode.Fiji,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Faeroese]: LanguageCode.Faeroese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.French]: LanguageCode.French,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Frisian]: LanguageCode.Frisian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Irish]: LanguageCode.Irish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.ScotsGaelic]: LanguageCode.ScotsGaelic,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Galician]: LanguageCode.Galician,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Guarani]: LanguageCode.Guarani,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Gijarati]: LanguageCode.Gijarati,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Hausa]: LanguageCode.Hausa,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Hindi]: LanguageCode.Hindi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Croatian]: LanguageCode.Croatian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Hungarian]: LanguageCode.Hungarian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Armenian]: LanguageCode.Armenian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Interlingua]: LanguageCode.Interlingua,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Interlingue]: LanguageCode.Interlingue,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Inupiak]: LanguageCode.Inupiak,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Indonesian]: LanguageCode.Indonesian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Icelandic]: LanguageCode.Icelandic,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Italian]: LanguageCode.Italian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Hebrew]: LanguageCode.Hebrew,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Japanese]: LanguageCode.Japanese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Yiddish]: LanguageCode.Yiddish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Javanese]: LanguageCode.Javanese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Georgian]: LanguageCode.Georgian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kazakh]: LanguageCode.Kazakh,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Greenlandic]: LanguageCode.Greenlandic,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Cambodian]: LanguageCode.Cambodian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kannada]: LanguageCode.Kannada,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Korean]: LanguageCode.Korean,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kashmiri]: LanguageCode.Kashmiri,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kurdish]: LanguageCode.Kurdish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kirghiz]: LanguageCode.Kirghiz,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Latin]: LanguageCode.Latin,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Lingala]: LanguageCode.Lingala,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Laothian]: LanguageCode.Laothian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Lithuanian]: LanguageCode.Lithuanian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Latvian]: LanguageCode.Latvian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Malagasy]: LanguageCode.Malagasy,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Maori]: LanguageCode.Maori,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Macedonian]: LanguageCode.Macedonian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Malayalam]: LanguageCode.Malayalam,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Mongolian]: LanguageCode.Mongolian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Moldavian]: LanguageCode.Moldavian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Marathi]: LanguageCode.Marathi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Malay]: LanguageCode.Malay,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Maltese]: LanguageCode.Maltese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Burmese]: LanguageCode.Burmese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Nauru]: LanguageCode.Nauru,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Nepali]: LanguageCode.Nepali,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Dutch]: LanguageCode.Dutch,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Norwegian]: LanguageCode.Norwegian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Occitan]: LanguageCode.Occitan,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Oromo]: LanguageCode.Oromo,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Oriya]: LanguageCode.Oriya,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Punjabi]: LanguageCode.Punjabi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Polish]: LanguageCode.Polish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Pashto]: LanguageCode.Pashto,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Portuguese]: LanguageCode.Portuguese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Quechua]: LanguageCode.Quechua,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.RhaetoRomance]: LanguageCode.RhaetoRomance,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kirundi]: LanguageCode.Kirundi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Romanian]: LanguageCode.Romanian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Russian]: LanguageCode.Russian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Kinyarwanda]: LanguageCode.Kinyarwanda,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Sanskrit]: LanguageCode.Sanskrit,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Sindhi]: LanguageCode.Sindhi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Sangro]: LanguageCode.Sangro,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.SerboCroatian]: LanguageCode.SerboCroatian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Singhalese]: LanguageCode.Singhalese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Slovak]: LanguageCode.Slovak,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Slovenian]: LanguageCode.Slovenian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Samoan]: LanguageCode.Samoan,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Shona]: LanguageCode.Shona,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Somali]: LanguageCode.Somali,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Albanian]: LanguageCode.Albanian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Serbian]: LanguageCode.Serbian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Siswati]: LanguageCode.Siswati,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Sesotho]: LanguageCode.Sesotho,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Sudanese]: LanguageCode.Sudanese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Swedish]: LanguageCode.Swedish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Swahili]: LanguageCode.Swahili,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tamil]: LanguageCode.Tamil,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tegulu]: LanguageCode.Tegulu,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tajik]: LanguageCode.Tajik,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Thai]: LanguageCode.Thai,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tigrinya]: LanguageCode.Tigrinya,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Turkmen]: LanguageCode.Turkmen,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tagalog]: LanguageCode.Tagalog,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Setswana]: LanguageCode.Setswana,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tonga]: LanguageCode.Tonga,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Turkish]: LanguageCode.Turkish,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tsonga]: LanguageCode.Tsonga,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Tatar]: LanguageCode.Tatar,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Twi]: LanguageCode.Twi,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Ukrainian]: LanguageCode.Ukrainian,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Urda]: LanguageCode.Urda,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Uzbek]: LanguageCode.Uzbek,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Vietnamese]: LanguageCode.Vietnamese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Volapuk]: LanguageCode.Volapuk,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Wolof]: LanguageCode.Wolof,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Xhosa]: LanguageCode.Xhosa,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Yoruba]: LanguageCode.Yoruba,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Chinese]: LanguageCode.Chinese,
    LANGUAGE_CODE_TO_NAME_MAP[LanguageCode.Zulu]: LanguageCode.Zulu,
}

SHORT_NAME_TO_LANGUAGE_CODE_MAP = {
    # English Legacy is ignored, because user should not
    # use legacy english on new FRUs.
    # To support consistent FRU conversion to yaml and back to binary
    # binary to yaml conversion will use full names.
    "aa": LanguageCode.Afar,
    "ab": LanguageCode.Abkhazian,
    "af": LanguageCode.Afrikaans,
    "am": LanguageCode.Amharic,
    "ar": LanguageCode.Arabic,
    "as": LanguageCode.Assamese,
    "ay": LanguageCode.Aymara,
    "az": LanguageCode.Azerbaijani,
    "ba": LanguageCode.Bashkir,
    "be": LanguageCode.Byelorussian,
    "bg": LanguageCode.Bulgarian,
    "bh": LanguageCode.Bihari,
    "bi": LanguageCode.Bislama,
    "bn": LanguageCode.Bengali,
    "bo": LanguageCode.Tibetan,
    "br": LanguageCode.Breton,
    "ca": LanguageCode.Catalan,
    "co": LanguageCode.Corsican,
    "cs": LanguageCode.Czech,
    "cy": LanguageCode.Welsh,
    "da": LanguageCode.Danish,
    "de": LanguageCode.German,
    "dz": LanguageCode.Bhutani,
    "el": LanguageCode.Greek,
    "en": LanguageCode.English,
    "eo": LanguageCode.Esperanto,
    "es": LanguageCode.Spanish,
    "et": LanguageCode.Estonian,
    "eu": LanguageCode.Basque,
    "fa": LanguageCode.Persian,
    "fi": LanguageCode.Finnish,
    "fj": LanguageCode.Fiji,
    "fo": LanguageCode.Faeroese,
    "fr": LanguageCode.French,
    "fy": LanguageCode.Frisian,
    "ga": LanguageCode.Irish,
    "gd": LanguageCode.ScotsGaelic,
    "gl": LanguageCode.Galician,
    "gn": LanguageCode.Guarani,
    "gu": LanguageCode.Gijarati,
    "ha": LanguageCode.Hausa,
    "hi": LanguageCode.Hindi,
    "hr": LanguageCode.Croatian,
    "hu": LanguageCode.Hungarian,
    "hy": LanguageCode.Armenian,
    "ia": LanguageCode.Interlingua,
    "ie": LanguageCode.Interlingue,
    "ik": LanguageCode.Inupiak,
    "in": LanguageCode.Indonesian,
    "is": LanguageCode.Icelandic,
    "it": LanguageCode.Italian,
    "iw": LanguageCode.Hebrew,
    "ja": LanguageCode.Japanese,
    "ji": LanguageCode.Yiddish,
    "jw": LanguageCode.Javanese,
    "ka": LanguageCode.Georgian,
    "kk": LanguageCode.Kazakh,
    "kl": LanguageCode.Greenlandic,
    "km": LanguageCode.Cambodian,
    "kn": LanguageCode.Kannada,
    "ko": LanguageCode.Korean,
    "ks": LanguageCode.Kashmiri,
    "ku": LanguageCode.Kurdish,
    "ky": LanguageCode.Kirghiz,
    "la": LanguageCode.Latin,
    "ln": LanguageCode.Lingala,
    "lo": LanguageCode.Laothian,
    "lt": LanguageCode.Lithuanian,
    "lv": LanguageCode.Latvian,
    "mg": LanguageCode.Malagasy,
    "mi": LanguageCode.Maori,
    "mk": LanguageCode.Macedonian,
    "ml": LanguageCode.Malayalam,
    "mn": LanguageCode.Mongolian,
    "mo": LanguageCode.Moldavian,
    "mr": LanguageCode.Marathi,
    "ms": LanguageCode.Malay,
    "mt": LanguageCode.Maltese,
    "my": LanguageCode.Burmese,
    "na": LanguageCode.Nauru,
    "ne": LanguageCode.Nepali,
    "nl": LanguageCode.Dutch,
    "no": LanguageCode.Norwegian,
    "oc": LanguageCode.Occitan,
    "om": LanguageCode.Oromo,
    "or": LanguageCode.Oriya,
    "pa": LanguageCode.Punjabi,
    "pl": LanguageCode.Polish,
    "ps": LanguageCode.Pashto,
    "pt": LanguageCode.Portuguese,
    "qu": LanguageCode.Quechua,
    "rm": LanguageCode.RhaetoRomance,
    "rn": LanguageCode.Kirundi,
    "ro": LanguageCode.Romanian,
    "ru": LanguageCode.Russian,
    "rw": LanguageCode.Kinyarwanda,
    "sa": LanguageCode.Sanskrit,
    "sd": LanguageCode.Sindhi,
    "sg": LanguageCode.Sangro,
    "sh": LanguageCode.SerboCroatian,
    "si": LanguageCode.Singhalese,
    "sk": LanguageCode.Slovak,
    "sl": LanguageCode.Slovenian,
    "sm": LanguageCode.Samoan,
    "sn": LanguageCode.Shona,
    "so": LanguageCode.Somali,
    "sq": LanguageCode.Albanian,
    "sr": LanguageCode.Serbian,
    "ss": LanguageCode.Siswati,
    "st": LanguageCode.Sesotho,
    "su": LanguageCode.Sudanese,
    "sv": LanguageCode.Swedish,
    "sw": LanguageCode.Swahili,
    "ta": LanguageCode.Tamil,
    "te": LanguageCode.Tegulu,
    "tg": LanguageCode.Tajik,
    "th": LanguageCode.Thai,
    "ti": LanguageCode.Tigrinya,
    "tk": LanguageCode.Turkmen,
    "tl": LanguageCode.Tagalog,
    "tn": LanguageCode.Setswana,
    "to": LanguageCode.Tonga,
    "tr": LanguageCode.Turkish,
    "ts": LanguageCode.Tsonga,
    "tt": LanguageCode.Tatar,
    "tw": LanguageCode.Twi,
    "uk": LanguageCode.Ukrainian,
    "ur": LanguageCode.Urda,
    "uz": LanguageCode.Uzbek,
    "vi": LanguageCode.Vietnamese,
    "vo": LanguageCode.Volapuk,
    "wo": LanguageCode.Wolof,
    "xh": LanguageCode.Xhosa,
    "yo": LanguageCode.Yoruba,
    "zh": LanguageCode.Chinese,
    "zu": LanguageCode.Zulu,
}


def str_to_language_code(name: str) -> LanguageCode | None:
    lc_name = name.lower()
    val = NAME_TO_LANGUAGE_CODE_MAP.get(lc_name)
    if val is not None:
        return val

    val = SHORT_NAME_TO_LANGUAGE_CODE_MAP.get(lc_name)
    if val is not None:
        return val

    raise ValueError(
        "Unknown language code '{}'. Available values: [{}]".format(
            lc_name,
            ", ".join(
                (
                    f"{LANGUAGE_CODE_TO_NAME_MAP[val]} ({short_name})"
                    for short_name, val in SHORT_NAME_TO_LANGUAGE_CODE_MAP.items()
                )
            ),
        )
    )


def language_code_to_str(lc: LanguageCode) -> str:
    return LANGUAGE_CODE_TO_NAME_MAP.get(lc)


def language_code_to_index(lc: LanguageCode) -> int:
    return LANGUAGE_CODE_TO_INDEX_MAP.get(lc)


def index_to_language_code(index: int) -> LanguageCode | None:
    if index < 0 or index > len(INDEX_TO_LANGUAGE_CODE_MAP):
        return None
    return INDEX_TO_LANGUAGE_CODE_MAP[index]


class TestLanguageCodes(TestCase):
    def test_from_index(self):
        self.assertEqual(index_to_language_code(135), LanguageCode.Chinese)
        self.assertEqual(index_to_language_code(0), LanguageCode.EnglishLegacy)
        self.assertEqual(index_to_language_code(25), LanguageCode.English)

    def test_to_index(self):
        self.assertEqual(language_code_to_index(LanguageCode.Chinese), 135)
        self.assertEqual(language_code_to_index(LanguageCode.English), 25)

    def test_to_str(self):
        self.assertEqual(language_code_to_str(LanguageCode.Uzbek), "uzbek")

    def test_from_str(self):
        self.assertEqual(str_to_language_code("uzbek"), LanguageCode.Uzbek)

    def test_from_str_short(self):
        self.assertEqual(str_to_language_code("en"), LanguageCode.English)
