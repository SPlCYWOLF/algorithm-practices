const seoul = ["khan", "ken", "Kim", "wow", "hahahhdih"];

function solution(seoul) {
    var answer = seoul.indexOf("Kim");
    return `김서방은 ${answer}에 있다`;
}

console.log(solution(seoul));

