import enum
import unittest
import typing as tp


class LanguageCode(enum.Enum):
    English = enum.auto()
    Afar = enum.auto()
    Abkhazian = enum.auto()
    Afrikaans = enum.auto()
    Amharic = enum.auto()
    Arabic = enum.auto()
    Assamese = enum.auto()
    Aymara = enum.auto()
    Azerbaijani = enum.auto()
    Bashkir = enum.auto()
    Byelorussian = enum.auto()
    Bulgarian = enum.auto()
    Bihari = enum.auto()
    Bislama = enum.auto()
    Bengali = enum.auto()
    Tibetan = enum.auto()
    Breton = enum.auto()
    Catalan = enum.auto()
    Corsican = enum.auto()
    Czech = enum.auto()
    Welsh = enum.auto()
    Danish = enum.auto()
    German = enum.auto()
    Bhutani = enum.auto()
    Greek = enum.auto()
    Esperanto = enum.auto()
    Spanish = enum.auto()
    Estonian = enum.auto()
    Basque = enum.auto()
    Persian = enum.auto()
    Finnish = enum.auto()
    Fiji = enum.auto()
    Faeroese = enum.auto()
    French = enum.auto()
    Frisian = enum.auto()
    Irish = enum.auto()
    ScotsGaelic = enum.auto()
    Galician = enum.auto()
    Guarani = enum.auto()
    Gijarati = enum.auto()
    Hausa = enum.auto()
    Hindi = enum.auto()
    Croatian = enum.auto()
    Hungarian = enum.auto()
    Armenian = enum.auto()
    Interlingua = enum.auto()
    Interlingue = enum.auto()
    Inupiak = enum.auto()
    Indonesian = enum.auto()
    Icelandic = enum.auto()
    Italian = enum.auto()
    Hebrew = enum.auto()
    Japanese = enum.auto()
    Yiddish = enum.auto()
    Javanese = enum.auto()
    Georgian = enum.auto()
    Kazakh = enum.auto()
    Greenlandic = enum.auto()
    Cambodian = enum.auto()
    Kannada = enum.auto()
    Korean = enum.auto()
    Kashmiri = enum.auto()
    Kurdish = enum.auto()
    Kirghiz = enum.auto()
    Latin = enum.auto()
    Lingala = enum.auto()
    Laothian = enum.auto()
    Lithuanian = enum.auto()
    Latvian = enum.auto()
    Malagasy = enum.auto()
    Maori = enum.auto()
    Macedonian = enum.auto()
    Malayalam = enum.auto()
    Mongolian = enum.auto()
    Moldavian = enum.auto()
    Marathi = enum.auto()
    Malay = enum.auto()
    Maltese = enum.auto()
    Burmese = enum.auto()
    Nauru = enum.auto()
    Nepali = enum.auto()
    Dutch = enum.auto()
    Norwegian = enum.auto()
    Occitan = enum.auto()
    Oromo = enum.auto()
    Oriya = enum.auto()
    Punjabi = enum.auto()
    Polish = enum.auto()
    Pashto = enum.auto()
    Portuguese = enum.auto()
    Quechua = enum.auto()
    RhaetoRomance = enum.auto()
    Kirundi = enum.auto()
    Romanian = enum.auto()
    Russian = enum.auto()
    Kinyarwanda = enum.auto()
    Sanskrit = enum.auto()
    Sindhi = enum.auto()
    Sangro = enum.auto()
    SerboCroatian = enum.auto()
    Singhalese = enum.auto()
    Slovak = enum.auto()
    Slovenian = enum.auto()
    Samoan = enum.auto()
    Shona = enum.auto()
    Somali = enum.auto()
    Albanian = enum.auto()
    Serbian = enum.auto()
    Siswati = enum.auto()
    Sesotho = enum.auto()
    Sudanese = enum.auto()
    Swedish = enum.auto()
    Swahili = enum.auto()
    Tamil = enum.auto()
    Tegulu = enum.auto()
    Tajik = enum.auto()
    Thai = enum.auto()
    Tigrinya = enum.auto()
    Turkmen = enum.auto()
    Tagalog = enum.auto()
    Setswana = enum.auto()
    Tonga = enum.auto()
    Turkish = enum.auto()
    Tsonga = enum.auto()
    Tatar = enum.auto()
    Twi = enum.auto()
    Ukrainian = enum.auto()
    Urda = enum.auto()
    Uzbek = enum.auto()
    Vietnamese = enum.auto()
    Volapuk = enum.auto()
    Wolof = enum.auto()
    Xhosa = enum.auto()
    Yoruba = enum.auto()
    Chinese = enum.auto()
    Zulu = enum.auto()


index_to_language_code_map = [
    LanguageCode.English,
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


language_code_to_name_map = {
    LanguageCode.English: "english",
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


language_code_to_index_map = {
    LanguageCode.English: 0,
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
    # LanguageCode.English: 25 Removed, because normal value is 0. 25 is for backward compat
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

name_to_language_code_map = {
    "english": LanguageCode.English,
    "afar": LanguageCode.Afar,
    "abkhazian": LanguageCode.Abkhazian,
    "afrikaans": LanguageCode.Afrikaans,
    "amharic": LanguageCode.Amharic,
    "arabic": LanguageCode.Arabic,
    "assamese": LanguageCode.Assamese,
    "aymara": LanguageCode.Aymara,
    "azerbaijani": LanguageCode.Azerbaijani,
    "bashkir": LanguageCode.Bashkir,
    "byelorussian": LanguageCode.Byelorussian,
    "bulgarian": LanguageCode.Bulgarian,
    "bihari": LanguageCode.Bihari,
    "bislama": LanguageCode.Bislama,
    "bengali": LanguageCode.Bengali,
    "tibetan": LanguageCode.Tibetan,
    "breton": LanguageCode.Breton,
    "catalan": LanguageCode.Catalan,
    "corsican": LanguageCode.Corsican,
    "czech": LanguageCode.Czech,
    "welsh": LanguageCode.Welsh,
    "danish": LanguageCode.Danish,
    "german": LanguageCode.German,
    "bhutani": LanguageCode.Bhutani,
    "greek": LanguageCode.Greek,
    "esperanto": LanguageCode.Esperanto,
    "spanish": LanguageCode.Spanish,
    "estonian": LanguageCode.Estonian,
    "basque": LanguageCode.Basque,
    "persian": LanguageCode.Persian,
    "finnish": LanguageCode.Finnish,
    "fiji": LanguageCode.Fiji,
    "faeroese": LanguageCode.Faeroese,
    "french": LanguageCode.French,
    "frisian": LanguageCode.Frisian,
    "irish": LanguageCode.Irish,
    "scotsgaelic": LanguageCode.ScotsGaelic,
    "galician": LanguageCode.Galician,
    "guarani": LanguageCode.Guarani,
    "gijarati": LanguageCode.Gijarati,
    "hausa": LanguageCode.Hausa,
    "hindi": LanguageCode.Hindi,
    "croatian": LanguageCode.Croatian,
    "hungarian": LanguageCode.Hungarian,
    "armenian": LanguageCode.Armenian,
    "interlingua": LanguageCode.Interlingua,
    "interlingue": LanguageCode.Interlingue,
    "inupiak": LanguageCode.Inupiak,
    "indonesian": LanguageCode.Indonesian,
    "icelandic": LanguageCode.Icelandic,
    "italian": LanguageCode.Italian,
    "hebrew": LanguageCode.Hebrew,
    "japanese": LanguageCode.Japanese,
    "yiddish": LanguageCode.Yiddish,
    "javanese": LanguageCode.Javanese,
    "georgian": LanguageCode.Georgian,
    "kazakh": LanguageCode.Kazakh,
    "greenlandic": LanguageCode.Greenlandic,
    "cambodian": LanguageCode.Cambodian,
    "kannada": LanguageCode.Kannada,
    "korean": LanguageCode.Korean,
    "kashmiri": LanguageCode.Kashmiri,
    "kurdish": LanguageCode.Kurdish,
    "kirghiz": LanguageCode.Kirghiz,
    "latin": LanguageCode.Latin,
    "lingala": LanguageCode.Lingala,
    "laothian": LanguageCode.Laothian,
    "lithuanian": LanguageCode.Lithuanian,
    "latvian": LanguageCode.Latvian,
    "malagasy": LanguageCode.Malagasy,
    "maori": LanguageCode.Maori,
    "macedonian": LanguageCode.Macedonian,
    "malayalam": LanguageCode.Malayalam,
    "mongolian": LanguageCode.Mongolian,
    "moldavian": LanguageCode.Moldavian,
    "marathi": LanguageCode.Marathi,
    "malay": LanguageCode.Malay,
    "maltese": LanguageCode.Maltese,
    "burmese": LanguageCode.Burmese,
    "nauru": LanguageCode.Nauru,
    "nepali": LanguageCode.Nepali,
    "dutch": LanguageCode.Dutch,
    "norwegian": LanguageCode.Norwegian,
    "occitan": LanguageCode.Occitan,
    "oromo": LanguageCode.Oromo,
    "oriya": LanguageCode.Oriya,
    "punjabi": LanguageCode.Punjabi,
    "polish": LanguageCode.Polish,
    "pashto": LanguageCode.Pashto,
    "portuguese": LanguageCode.Portuguese,
    "quechua": LanguageCode.Quechua,
    "rhaetoromance": LanguageCode.RhaetoRomance,
    "kirundi": LanguageCode.Kirundi,
    "romanian": LanguageCode.Romanian,
    "russian": LanguageCode.Russian,
    "kinyarwanda": LanguageCode.Kinyarwanda,
    "sanskrit": LanguageCode.Sanskrit,
    "sindhi": LanguageCode.Sindhi,
    "sangro": LanguageCode.Sangro,
    "serbocroatian": LanguageCode.SerboCroatian,
    "singhalese": LanguageCode.Singhalese,
    "slovak": LanguageCode.Slovak,
    "slovenian": LanguageCode.Slovenian,
    "samoan": LanguageCode.Samoan,
    "shona": LanguageCode.Shona,
    "somali": LanguageCode.Somali,
    "albanian": LanguageCode.Albanian,
    "serbian": LanguageCode.Serbian,
    "siswati": LanguageCode.Siswati,
    "sesotho": LanguageCode.Sesotho,
    "sudanese": LanguageCode.Sudanese,
    "swedish": LanguageCode.Swedish,
    "swahili": LanguageCode.Swahili,
    "tamil": LanguageCode.Tamil,
    "tegulu": LanguageCode.Tegulu,
    "tajik": LanguageCode.Tajik,
    "thai": LanguageCode.Thai,
    "tigrinya": LanguageCode.Tigrinya,
    "turkmen": LanguageCode.Turkmen,
    "tagalog": LanguageCode.Tagalog,
    "setswana": LanguageCode.Setswana,
    "tonga": LanguageCode.Tonga,
    "turkish": LanguageCode.Turkish,
    "tsonga": LanguageCode.Tsonga,
    "tatar": LanguageCode.Tatar,
    "twi": LanguageCode.Twi,
    "ukrainian": LanguageCode.Ukrainian,
    "urda": LanguageCode.Urda,
    "uzbek": LanguageCode.Uzbek,
    "vietnamese": LanguageCode.Vietnamese,
    "volapuk": LanguageCode.Volapuk,
    "wolof": LanguageCode.Wolof,
    "xhosa": LanguageCode.Xhosa,
    "yoruba": LanguageCode.Yoruba,
    "chinese": LanguageCode.Chinese,
    "zulu": LanguageCode.Zulu,
}


def str_to_language_code(name: str) -> tp.Optional[LanguageCode]:
    lc_name = name.lower()
    return name_to_language_code_map.get(lc_name)


def language_code_to_str(lc: LanguageCode) -> str:
    return language_code_to_name_map.get(lc)


def language_code_to_index(lc: LanguageCode) -> int:
    return language_code_to_index_map.get(lc)


def index_to_language_code(index: int) -> tp.Optional[LanguageCode]:
    if index < 0 or index > len(index_to_language_code_map):
        return None
    return index_to_language_code_map[index]


class TestLanguageCodes(unittest.TestCase):
    def test_from_index(self):
        self.assertEqual(index_to_language_code(135), LanguageCode.Chinese)
        self.assertEqual(index_to_language_code(0), LanguageCode.English)
        self.assertEqual(index_to_language_code(25), LanguageCode.English)

    def test_to_index(self):
        self.assertEqual(language_code_to_index(LanguageCode.Chinese), 135)
        self.assertEqual(language_code_to_index(LanguageCode.English), 0)

    def test_to_str(self):
        self.assertEqual(language_code_to_str(LanguageCode.Uzbek), "uzbek")

    def test_from_str(self):
        self.assertEqual(str_to_language_code("uzbek"), LanguageCode.Uzbek)


if __name__ == "__main__":
    unittest.main()
