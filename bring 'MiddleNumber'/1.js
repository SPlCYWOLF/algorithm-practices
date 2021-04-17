const a = "123456";
const stringLength = a.length;
const evenOrOdd = stringLength % 2;
const middleStrEven = (stringLength / 2) - 1;
const middleStrOdd = stringLength / 2;


function answer(a) {
    if(evenOrOdd === 0) {
        return [a.charAt(middleStrEven), a.charAt(middleStrOdd)];
    } else {
        return a.charAt(middleStrOdd);
    }
}



console.log(`middle letter is ${answer(a)}`);

console.log(`string length is ${stringLength}`);