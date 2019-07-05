/*global XRegExp*/
(function() {
    'use strict';

    var LATIN_MAP = {
        '脌': 'A', '脕': 'A', '脗': 'A', '脙': 'A', '脛': 'A', '脜': 'A', '脝': 'AE',
        '脟': 'C', '脠': 'E', '脡': 'E', '脢': 'E', '脣': 'E', '脤': 'I', '脥': 'I',
        '脦': 'I', '脧': 'I', '脨': 'D', '脩': 'N', '脪': 'O', '脫': 'O', '脭': 'O',
        '脮': 'O', '脰': 'O', '艕': 'O', '脴': 'O', '脵': 'U', '脷': 'U', '脹': 'U',
        '脺': 'U', '虐': 'U', '脻': 'Y', '脼': 'TH', '鸥': 'Y', '脽': 'ss', '脿': 'a',
        '谩': 'a', '芒': 'a', '茫': 'a', '盲': 'a', '氓': 'a', '忙': 'ae', '莽': 'c',
        '猫': 'e', '茅': 'e', '锚': 'e', '毛': 'e', '矛': 'i', '铆': 'i', '卯': 'i',
        '茂': 'i', '冒': 'd', '帽': 'n', '貌': 'o', '贸': 'o', '么': 'o', '玫': 'o',
        '枚': 'o', '艖': 'o', '酶': 'o', '霉': 'u', '煤': 'u', '没': 'u', '眉': 'u',
        '疟': 'u', '媒': 'y', '镁': 'th', '每': 'y'
    };
    var LATIN_SYMBOLS_MAP = {
        '漏': '(c)'
    };
    var GREEK_MAP = {
        '伪': 'a', '尾': 'b', '纬': 'g', '未': 'd', '蔚': 'e', '味': 'z', '畏': 'h',
        '胃': '8', '喂': 'i', '魏': 'k', '位': 'l', '渭': 'm', '谓': 'n', '尉': '3',
        '慰': 'o', '蟺': 'p', '蟻': 'r', '蟽': 's', '蟿': 't', '蠀': 'y', '蠁': 'f',
        '蠂': 'x', '蠄': 'ps', '蠅': 'w', '维': 'a', '苇': 'e', '委': 'i', '蠈': 'o',
        '蠉': 'y', '萎': 'h', '蠋': 'w', '蟼': 's', '蠆': 'i', '伟': 'y', '蠇': 'y',
        '螑': 'i', '螒': 'A', '螔': 'B', '螕': 'G', '螖': 'D', '螘': 'E', '螙': 'Z',
        '螚': 'H', '螛': '8', '螜': 'I', '螝': 'K', '螞': 'L', '螠': 'M', '螡': 'N',
        '螢': '3', '螣': 'O', '螤': 'P', '巍': 'R', '危': 'S', '韦': 'T', '违': 'Y',
        '桅': 'F', '围': 'X', '唯': 'PS', '惟': 'W', '螁': 'A', '螆': 'E', '螉': 'I',
        '螌': 'O', '螏': 'Y', '螇': 'H', '螐': 'W', '为': 'I', '潍': 'Y'
    };
    var TURKISH_MAP = {
        '艧': 's', '艦': 'S', '谋': 'i', '陌': 'I', '莽': 'c', '脟': 'C', '眉': 'u',
        '脺': 'U', '枚': 'o', '脰': 'O', '臒': 'g', '臑': 'G'
    };
    var ROMANIAN_MAP = {
        '膬': 'a', '卯': 'i', '葯': 's', '葲': 't', '芒': 'a',
        '膫': 'A', '脦': 'I', '葮': 'S', '葰': 'T', '脗': 'A'
    };
    var RUSSIAN_MAP = {
        '邪': 'a', '斜': 'b', '胁': 'v', '谐': 'g', '写': 'd', '械': 'e', '褢': 'yo',
        '卸': 'zh', '蟹': 'z', '懈': 'i', '泄': 'j', '泻': 'k', '谢': 'l', '屑': 'm',
        '薪': 'n', '芯': 'o', '锌': 'p', '褉': 'r', '褋': 's', '褌': 't', '褍': 'u',
        '褎': 'f', '褏': 'h', '褑': 'c', '褔': 'ch', '褕': 'sh', '褖': 'sh', '褗': '',
        '褘': 'y', '褜': '', '褝': 'e', '褞': 'yu', '褟': 'ya',
        '袗': 'A', '袘': 'B', '袙': 'V', '袚': 'G', '袛': 'D', '袝': 'E', '衼': 'Yo',
        '袞': 'Zh', '袟': 'Z', '袠': 'I', '袡': 'J', '袣': 'K', '袥': 'L', '袦': 'M',
        '袧': 'N', '袨': 'O', '袩': 'P', '袪': 'R', '小': 'S', '孝': 'T', '校': 'U',
        '肖': 'F', '啸': 'H', '笑': 'C', '效': 'Ch', '楔': 'Sh', '些': 'Sh', '歇': '',
        '蝎': 'Y', '鞋': '', '协': 'E', '挟': 'Yu', '携': 'Ya'
    };
    var UKRAINIAN_MAP = {
        '袆': 'Ye', '袉': 'I', '袊': 'Yi', '覑': 'G', '褦': 'ye', '褨': 'i',
        '褩': 'yi', '覒': 'g'
    };
    var CZECH_MAP = {
        '膷': 'c', '膹': 'd', '臎': 'e', '艌': 'n', '艡': 'r', '拧': 's', '钮': 't',
        '暖': 'u', '啪': 'z', '膶': 'C', '膸': 'D', '臍': 'E', '艊': 'N', '艠': 'R',
        '艩': 'S', '扭': 'T', '女': 'U', '沤': 'Z'
    };
    var SLOVAK_MAP = {
        '谩': 'a', '盲': 'a', '膷': 'c', '膹': 'd', '茅': 'e', '铆': 'i', '木': 'l',
        '暮': 'l', '艌': 'n', '贸': 'o', '么': 'o', '艜': 'r', '拧': 's', '钮': 't',
        '煤': 'u', '媒': 'y', '啪': 'z',
        '脕': 'a', '脛': 'A', '膶': 'C', '膸': 'D', '脡': 'E', '脥': 'I', '慕': 'L',
        '墓': 'L', '艊': 'N', '脫': 'O', '脭': 'O', '艛': 'R', '艩': 'S', '扭': 'T',
        '脷': 'U', '脻': 'Y', '沤': 'Z'
    };
    var POLISH_MAP = {
        '膮': 'a', '膰': 'c', '臋': 'e', '艂': 'l', '艅': 'n', '贸': 'o', '艣': 's',
        '藕': 'z', '偶': 'z',
        '膭': 'A', '膯': 'C', '臉': 'E', '艁': 'L', '艃': 'N', '脫': 'O', '艢': 'S',
        '殴': 'Z', '呕': 'Z'
    };
    var LATVIAN_MAP = {
        '膩': 'a', '膷': 'c', '膿': 'e', '模': 'g', '墨': 'i', '姆': 'k', '募': 'l',
        '艈': 'n', '拧': 's', '奴': 'u', '啪': 'z',
        '膧': 'A', '膶': 'C', '膾': 'E', '蘑': 'G', '莫': 'I', '亩': 'K', '幕': 'L',
        '艆': 'N', '艩': 'S', '弄': 'U', '沤': 'Z'
    };
    var ARABIC_MAP = {
        '兀': 'a', '亘': 'b', '鬲': 't', '孬': 'th', '噩': 'g', '丨': 'h', '禺': 'kh', '丿': 'd',
        '匕': 'th', '乇': 'r', '夭': 'z', '爻': 's', '卮': 'sh', '氐': 's', '囟': 'd', '胤': 't',
        '馗': 'th', '毓': 'aa', '睾': 'gh', '賮': 'f', '賯': 'k', '賰': 'k', '賱': 'l', '賲': 'm',
        '賳': 'n', '賴': 'h', '賵': 'o', '賷': 'y'
    };
    var LITHUANIAN_MAP = {
        '膮': 'a', '膷': 'c', '臋': 'e', '臈': 'e', '寞': 'i', '拧': 's', '懦': 'u',
        '奴': 'u', '啪': 'z',
        '膭': 'A', '膶': 'C', '臉': 'E', '臇': 'E', '漠': 'I', '艩': 'S', '挪': 'U',
        '弄': 'U', '沤': 'Z'
    };
    var SERBIAN_MAP = {
        '褣': 'dj', '褬': 'j', '褭': 'lj', '褮': 'nj', '褯': 'c', '褵': 'dz',
        '膽': 'dj', '袀': 'Dj', '袌': 'j', '袎': 'Lj', '袏': 'Nj', '袐': 'C',
        '袕': 'Dz', '膼': 'Dj'
    };
    var AZERBAIJANI_MAP = {
        '莽': 'c', '蓹': 'e', '臒': 'g', '谋': 'i', '枚': 'o', '艧': 's', '眉': 'u',
        '脟': 'C', '茝': 'E', '臑': 'G', '陌': 'I', '脰': 'O', '艦': 'S', '脺': 'U'
    };
    // var GEORGIAN_MAP = {
    //     '醿�': 'a', '醿�': 'b', '醿�': 'g', '醿�': 'd', '醿�': 'e', '醿�': 'v', '醿�': 'z',
    //     '醿�': 't', '醿�': 'i', '醿�': 'k', '醿�': 'l', '醿�': 'm', '醿�': 'n', '醿�': 'o',
    //     '醿�': 'p', '醿�': 'j', '醿�': 'r', '醿�': 's', '醿�': 't', '醿�': 'u', '醿�': 'f',
    //     '醿�': 'q', '醿�': 'g', '醿�': 'y', '醿�': 'sh', '醿�': 'ch', '醿�': 'c', '醿�': 'dz',
    //     '醿�': 'w', '醿�': 'ch', '醿�': 'x', '醿�': 'j', '醿�': 'h'
    // };

    var ALL_DOWNCODE_MAPS = [
        LATIN_MAP,
        LATIN_SYMBOLS_MAP,
        GREEK_MAP,
        TURKISH_MAP,
        ROMANIAN_MAP,
        RUSSIAN_MAP,
        UKRAINIAN_MAP,
        CZECH_MAP,
        SLOVAK_MAP,
        POLISH_MAP,
        LATVIAN_MAP,
        ARABIC_MAP,
        LITHUANIAN_MAP,
        SERBIAN_MAP,
        AZERBAIJANI_MAP,
        GEORGIAN_MAP
    ];

    var Downcoder = {
        'Initialize': function() {
            if (Downcoder.map) {  // already made
                return;
            }
            Downcoder.map = {};
            Downcoder.chars = [];
            for (var i = 0; i < ALL_DOWNCODE_MAPS.length; i++) {
                var lookup = ALL_DOWNCODE_MAPS[i];
                for (var c in lookup) {
                    if (lookup.hasOwnProperty(c)) {
                        Downcoder.map[c] = lookup[c];
                    }
                }
            }
            for (var k in Downcoder.map) {
                if (Downcoder.map.hasOwnProperty(k)) {
                    Downcoder.chars.push(k);
                }
            }
            Downcoder.regex = new RegExp(Downcoder.chars.join('|'), 'g');
        }
    };

    function downcode(slug) {
        Downcoder.Initialize();
        return slug.replace(Downcoder.regex, function(m) {
            return Downcoder.map[m];
        });
    }


    function URLify(s, num_chars, allowUnicode) {
        // changes, e.g., "Petty theft" to "petty-theft"
        // remove all these words from the string before urlifying
        if (!allowUnicode) {
            s = downcode(s);
        }
        var hasUnicodeChars = /[^\u0000-\u007f]/.test(s);
        // Remove English words only if the string contains ASCII (English)
        // characters.
        if (!hasUnicodeChars) {
            var removeList = [
                "a", "an", "as", "at", "before", "but", "by", "for", "from",
                "is", "in", "into", "like", "of", "off", "on", "onto", "per",
                "since", "than", "the", "this", "that", "to", "up", "via",
                "with"
            ];
            var r = new RegExp('\\b(' + removeList.join('|') + ')\\b', 'gi');
            s = s.replace(r, '');
        }
        // if downcode doesn't hit, the char will be stripped here
        if (allowUnicode) {
            // Keep Unicode letters including both lowercase and uppercase
            // characters, whitespace, and dash; remove other characters.
            s = XRegExp.replace(s, XRegExp('[^-_\\p{L}\\p{N}\\s]', 'g'), '');
        } else {
            s = s.replace(/[^-\w\s]/g, '');  // remove unneeded chars
        }
        s = s.replace(/^\s+|\s+$/g, '');   // trim leading/trailing spaces
        s = s.replace(/[-\s]+/g, '-');     // convert spaces to hyphens
        s = s.substring(0, num_chars);     // trim to first num_chars chars
        s = s.replace(/-+$/g, '');         // trim any trailing hyphens
        return s.toLowerCase();            // convert to lowercase
    }
    window.URLify = URLify;
})();