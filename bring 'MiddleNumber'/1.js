const a = "123456";
const stringLength = a.length;
const evenOrOdd = stringLength % 2;
const middleStrOdd = stringLength / 2;
const middleStrEven = middleStrOdd + 1;

function answer(a) {
    if(evenOrOdd === 0) {
        return a.substring(middleStrOdd - 1, middleStrEven);
    } else {
        return a.charAt(middleStrOdd);
    }
}

console.log(`middle letter is "${answer(a)}"`);
console.log(`string length is "${stringLength}"`);