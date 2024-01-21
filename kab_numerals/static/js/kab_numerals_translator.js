class NumberToKab {
    ZERO = 'зыри';

    DIGITS = {
        1: 'зы',
        2: 'тIу',
        3: 'щы',
        4: 'плIы',
        5: 'тху',
        6: 'хы',
        7: 'блы',
        8: 'и',
        9: 'бгъу',
    }

    TEN_TO_NINETEEN = {
        0: 'пщIы',
        1: 'пщыкIуз',
        2: 'пщыкIутI',
        3: 'пщыкIущ',
        4: 'пщыкIуплI',
        5: 'пщыкIутху',
        6: 'пщыкIух',
        7: 'пщыкIубл',
        8: 'пщыкIуий',
        9: 'пщыкIубгъу',
    }

    TENS = {
        2: 'тIощI',
        3: 'щыщI',
        4: 'плIыщI',
        5: 'тхущI',
        6: 'хыщI',
        7: 'блыщI',
        8: 'ищI',
        9: 'бгъущI',
    }

    HUNDREDS = {
        1: 'щэ',
        2: 'щитI',
        3: 'щищ',
        4: 'щиплI',
        5: 'щитху',
        6: 'щих',
        7: 'щибл',
        8: 'щий',
        9: 'щибгъу',
    }

    THOUSANDS_AND_MILLIONS = {
        1: {
            0: '',
            1: 'мин',
            2: 'минитI',
            3: 'минищ',
            4: 'миниплI',
            5: 'минитху',
            6: 'миних',
            7: 'минибл',
            8: 'миний',
            9: 'минибгъу',
            10: 'минипщI',
            100: 'минищэ',
        },

        2: {
            0: '',
            1: 'мелуан',
            2: 'мелуанитI',
            3: 'мелуанищ',
            4: 'мелуаниплI',
            5: 'мелуанитху',
            6: 'мелуаних',
            7: 'мелуанибл',
            8: 'мелуаний',
            9: 'мелуанибгъу',
            10: 'мелуанипщI',
            100: 'мелуанищэ',
        },
    }

    prefixes = {
        0: '',
        1: 'мин',
        2: 'мелуан',
    }

    constructor(number) {
        this.number = number;
    }

    translate() {
        if (this.number === '0') {
            return this.ZERO;
        }

        let result = this._translate_triad(this.number % 1000);

        let triads = this._split_for_triads();
        for (const key in triads) {
            if (triads[key] > 10 && triads[key] !== 100) {
                if (result) {
                    result = this.prefixes[key] + " " + this._translate_triad(triads[key]) + "рэ " + result;
                } else {
                    result = this.prefixes[key] + " " + this._translate_triad(triads[key]) + result;
                }
            } else {
                if (result) {
                    let suffix = "";
                    if (triads[key]) {
                        suffix = "рэ ";
                    }
                    result = this.THOUSANDS_AND_MILLIONS[key][triads[key]] + suffix + result;
                } else {
                    result = this.THOUSANDS_AND_MILLIONS[key][triads[key]];
                }
            }
        }
        return result;
    }

    _split_for_triads() {
        let result = {};
        let number = Math.floor(this.number / 1000);
        let index = 0;
        while (number > 0) {
            index += 1;
            result[index] = number % 1000;
            number = Math.floor(number / 1000);
        }
        return result;
    }

    _translate_triad(triad) {
        let result = "";
        let digit = triad % 10;

        if (digit > 0) {
            result = this.DIGITS[digit]
        }

        let ten = Math.floor(triad / 10) % 10;
        if (ten > 1) {
            let tens = this.TENS[ten];
            digit > 0 ? result = tens + 'рэ ' + result : result = tens + result;
        } else if (ten === 1) {
            result = this.TEN_TO_NINETEEN[digit]
        }

        triad = Math.floor(triad / 100);
        if (triad > 0) {
            let hundreds = this.HUNDREDS[triad];
            ten || digit ? result = hundreds + 'рэ ' + result : result = hundreds + result;
        }
        return result;
    }
}

let input = document.getElementById('id_number');

input.oninput = function () {
    let number = new NumberToKab(input.value);
    let output = document.getElementsByName('translation')[0];
    output.textContent = number.translate();
}
