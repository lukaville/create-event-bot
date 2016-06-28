function contains(searchString, keyword) {
    return searchString.toLowerCase().indexOf(keyword.toLowerCase()) != -1;
}

function findKeyword(searchString) {
    for (var keyword in keywords) {
        var locales = keywords[keyword];
        for (var locale in locales) {
            var arr = locales[locale];
            for (var k in arr) {
                if (contains(searchString, arr[k])) {
                    return keyword;
                }
            }
        }
    }

    return "default";
}

function getImage(event) {
    var searchString = event.name;
    if (event.description) {
        searchString += event.description;
    }

    return findKeyword(searchString);
}

var keywords = {
    "repair": {
        "en": ["repair", "fridge repair", "handyman", "electrician", "diy"],
        "ru": ["ремонт", "ремонт холодильника", "мастер", "электрик", "самоделк"],
    },
    "violin": {
        "en": ["violin", "violins"],
        "ru": ["виолончель"]
    },
    "learninstrument": {
        "en": ["learn instrument", "piano", "singing", "music class", "choir practice", "flute", "orchestra", "oboe", "clarinet", "saxophone", "cornett", "trumpet", "contrabass", "cello", "trombone", "tuba", "music ensemble", "string quartett", "guitar lesson", "classical music", "choir"],
        "ru": ["музыкалка", "музыка", "пианино", "пение", "хор", "флейта", "оркестр", "гобой", "кларнет", "саксофон", "корнет", "труба", "контрабас", "виолончель", "тромбон", "музыкальный ансамбль", "струнный квартет", "гитар", "классическая музыка"]
    },
    "code": {
        "en": ["code", "learn to code", "coding time", "hackathon", "rails girls", "railsgirls", "hour of code", "codecademy", "computer science", "programming in python", "web programming", "programming in java", "web development", "python", "perl", "java", "android", "c++", "javascript", "frontend", "c#"],
        "ru": ["код", "программирование", "хакатон", "час кода", "программ"]
    },
    "art": {
        "en": ["art", "painting", "art workshop", "sketching workshop", "drawing workshop"],
        "ru": ["искусств", "рисов", "художеств"]
    },
    "concert": {
        "en": ["concert", "gig", "concerts", "gigs"],
        "ru": ["концерт"]
    },
    "hiking": {
        "en": ["hiking", "hike", "hikes"],
        "ru": ["ориентирован"]
    },
    "read": {
        "en": ["reading", "newspaper"],
        "ru": ["чтен", "газет"]
    },
    "bookclub": {
        "en": ["book club", "reading"],
        "ru": ["книжн", "книг", "чтец"]
    },
    "haircut": {
        "en": ["haircut", "hair"],
        "ru": ["парикмахерская", "волос", "салон красоты"]
    },
    "chinesenewyear": {
        "en": ["chinese new year", "chinese new years", "chinese new year's"],
        "ru": ["китайский новый год"]
    },
    "thanksgiving": {
        "en": ["thanksgiving"],
        "ru": ["день благодарения"]
    },
    "oilchange": {
        "en": ["oil change", "car service"],
        "ru": ["поменять масло", "авто-сервис"]
    },
    "badminton": {
        "en": ["badminton"],
        "ru": ["бадминтон"]
    },
    "tennis": {
        "en": ["tennis"],
        "ru": ["теннис"]
    },
    "skiing": {
        "en": ["skiing", "ski", "skis", "snowboarding", "snowshoeing", "snow shoe", "snow boarding"],
        "ru": ["лыжи", "лыж", "сноуборд"]
    },
    "golf": {
        "en": ["golf"],
        "ru": ["гольф"]
    },
    "breakfast": {
        "en": ["breakfast", "breakfasts", "brunch", "brunches"],
        "ru": ["завтрак"]
    },
    "drinks": {
        "en": ["cocktail", "drinks", "cocktails"],
        "ru": ["напитк", "коктейль", "бар"]
    },
    "basketball": {
        "en": ["basketball"],
        "ru": ["баскет"]
    },
    "cycling": {
        "en": ["bicycle", "cycling", "bike", "bicycles", "bikes", "biking"],
        "ru": ["велосипед", "байк"]
    },
    "xmasparty": {
        "en": ["christmas party", "xmas party", "x-mas party", "christmas eve party", "xmas eve party", "x-mas eve party"],
        "ru": ["рождественская вечеринка", "новогодняя вечеринка"]
    },
    "camping": {
        "en": ["camping"],
        "ru": ["поход", "лагерь"]
    },
    "dancing": {
        "en": ["dance", "dancing", "dances"],
        "ru": ["танц"]
    },
    "cinema": {
        "en": ["cinema", "movies"],
        "ru": ["кино"]
    },
    "learnlanguage": {
        "en": ["learn language", "french course", "german course", "english course", "french class", "german class", "english class", "practice french", "practice german", "practice english"],
        "ru": ["языков", "англ", "иностран"]
    },
    "beer": {
        "en": ["beer", "beers", "oktoberfest", "october fest", "octoberfest"],
        "ru": ["пиво", "пивн", "октоберфест", "октобер фест", "октябрьфест"]
    },
    "newyear": {
        "en": ["new year", "new year's", "new years"],
        "ru": ["новый год", "новогод"]
    },
    "pride": {
        "en": ["dyke march", "christopher street day", "gay parade", "gay pride", "gayglers", "gaygler", "lesbian march", "lesbian parade", "lesbian pride", "euro pride", "europride", "world pride", "worldpride"],
        "ru": ["гей-парад", "парад равенства", "лезбийский марш"]
    },
    "bbq": {
        "en": ["bbq", "barbecue", "barbeque"],
        "ru": ["барбекю", "гриль"]
    },
    "coffee": {
        "en": ["coffee", "coffees"],
        "ru": ["кофе", "кафетер"]
    },
    "reachout": {
        "en": ["reach out to", "write letter", "send invitations"],
        "ru": ["пришлаш", "разослат", "письм"]
    },
    "halloween": {
        "en": ["halloween", "helloween", "hallowe'en", "allhalloween", "all hallows' eve", "all saints' eve"],
        "ru": ["хэллоуин"]
    },
    "gym": {
        "en": ["gym", "workout", "workouts"],
        "ru": ["гимнаст", "качал", "трениров"]
    },
    "pingpong": {
        "en": ["ping pong", "table tennis", "ping-pong", "pingpong"],
        "ru": ["пинг-понг", "настольный теннис", "пингпонг", "пинг понг"]
    },
    "santa": {
        "en": ["santa claus", "father christmas"],
        "ru": ["санта клаус", "дед мороз"]
    },
    "lunch": {
        "en": ["lunch", "lunches", "luncheon"],
        "ru": ["ланч", "обед"]
    },
    "dentist": {
        "en": ["dentist", "dentistry", "dental"],
        "ru": ["стоматолог", "дантист", "зуб"]
    },
    "billiard": {
        "en": ["billiard"],
        "ru": ["бильярд"]
    },
    "baseball": {
        "en": ["baseball"],
        "ru": ["бейсбол"]
    },
    "manicure": {
        "en": ["manicure", "pedicure", "manicures", "pedicures"],
        "ru": ["маникюр", "педикюр"]
    },
    "yoga": {
        "en": ["yoga"],
        "ru": ["йога"]
    },
    "walk": {
        "en": ["going for a walk", "walking"],
        "ru": ["прогулка", "гулят"]
    },
    "wedding": {
        "en": ["wedding"],
        "ru": ["свадьб"]
    },
    "planmyday": {
        "en": ["plan week", "plan quarter", "plan day", "plan vacation", "week planning", "vacation planning"],
        "ru": ["планирование", "план"]
    },
    "soccer": {
        "en": ["soccer"],
        "ru": ["футбол"]
    },
    "sailing": {
        "en": ["sail", "sailing", "boat cruise", "sailboat"],
        "ru": ["катер", "лодка", "круиз", "парусн", "корабл"]
    },
    "xmasmeal": {
        "en": ["christmas dinner", "christmas lunch", "christmas brunch", "christmas luncheon", "xmas lunch", "xmas luncheon", "x-mas dinner", "x-mas lunch", "x-mas brunch", "x-mas luncheon", "christmas eve dinner", "christmas eve lunch", "christmas eve brunch", "christmas eve luncheon", "xmas eve dinner", "xmas eve lunch", "xmas eve brunch", "xmas eve luncheon", "x-mas eve dinner", "x-mas eve lunch", "x-mas eve brunch", "x-mas eve luncheon"],
        "ru": ["рождественский обед", "новогодний обед"]
    },
    "kayaking": {
        "en": ["kayaking"],
        "ru": ["каяк"]
    },
    "running": {
        "en": ["jog", "jogging", "running", "jogs", "runs"],
        "ru": ["бег", "пробеж"]
    },
    "graduation": {
        "en": ["graduation"],
        "ru": ["выпускн"]
    },
    "dinner": {
        "en": ["dinner", "dinners", "restaurant", "restaurants", "family meal"],
        "ru": ["обед", "ресторан", "кушат"]
    },
    "clean": {
        "en": ["cleaning", "clean the house", "clean the apartment", "clean house", "tidy up", "vacuum clean", "vacuum cleaning"],
        "ru": ["уборка", "чистка", "чист", "убир"]
    },
    "bowling": {
        "en": ["bowling"],
        "ru": ["боулинг"]
    },
    "xmas": {
        "en": ["christmas", "xmas", "x-mas"],
        "ru": ["рождество"]
    },
    "massage": {
        "en": ["massage", "back rub", "backrub", "massages"],
        "ru": ["массаж"]
    },
    "swimming": {
        "en": ["swim", "swimming", "swims"],
        "ru": ["плавание", "бассейн"]
    }
};