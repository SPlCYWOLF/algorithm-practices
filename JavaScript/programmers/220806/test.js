// 문제 1
// function sum(list) {
//   const s = list.reduce((acc, val) => {
//       return acc + val
//   })

//   return s
// }

// function finder(nums) {
//   let arr_nums = Array.from(nums.toString()).map(Number);
//   const result_num = sum(arr_nums)

//   return result_num
// }

// function solution(n) {
//   let target = n
//   let answer = 0
//   let i = n.toString().length
//   while (i > 1) {  // 자연수의 자릿수가 1보다 클 경우 각 자릿수를 더하는 과정
//       answer = finder(target)
//       i = answer.toString().length
//       target = answer
//       console.log(i)
//       console.log(target)
//   }

//   return answer;
// }

// const n = 456789

// solution(n)





// 문제 2
function checkSign(signs) {
  if (signs[0] > 0 && signs[1] > 0) return 1
  if (signs[0] < 0 && signs[1] > 0) return 2
  if (signs[0] < 0 && signs[1] < 0) return 3
  if (signs[0] > 0 && signs[1] < 0) return 4
}

function findCoordinate(nums) {
  const slope = Math.round((nums[0] / nums[1])*100000) / 100000;
  const sign = checkSign(nums)
  return [slope, sign];
}


let sack = new Map();



const balloons = [[2, 2], [7, 7], [1, 4], [4, 1], [-1, -4]];

for (let balloon of balloons) {
  let coordinate = findCoordinate(balloon);

  if (sack.has(coordinate)) {
    console.log(false);
  } else {
    sack.set(coordinate);
  };
}
console.log(sack);
console.log(sack.size);

// 왜 Map Object에서 has 메서드로 중복 array 키값 여부를 확인 불가능 할까






// 문제 3

// const r = 5
// const c = 4

// //         좌 하 우 상 -> 좌 상 우 하
// const dr = [0, 1, 0, -1, 0, -1, 0, 1]
// const dc = [-1, 0, 1, 0, -1, 0, 1, 0]


// function createArray() {  // 2차원 array 생성함수
//   const f = Array(r).fill().map(() => Array(c).fill(0));
//   return f
// }

// let field = createArray();

// let i = 0
// let j = c - 1
// let num = 2
// let k = 0
// field[i][j] = 1

// while (num <= r * c) {

//   if (k == 8) {
//     k = 0
//   }

//   let nr = i + dr[k]
//   let nc = j + dc[k]


//   if (k === 3 || k === 7) {   // 4번째 '상' 7번째 '하' 는 한칸씩만
//     field[nr][nc] = num
//     i = nr
//     j = nc
//     nr = nr + dr[k]
//     nc = nc + dc[k]
//     num += 1
//     k += 1
//     continue
//   }
  
//   while (true) {
    
//     if (nr < 0 || nr >= r || nc < 0 || nc >= c) break
//     if (field[nr][nc] !== 0) break
//     if (num > r * c) break

//     field[nr][nc] = num
//     i = nr
//     j = nc
//     nr = nr + dr[k]
//     nc = nc + dc[k]
//     num += 1
//   }

//   k += 1
// }

// for (f of field) {
//   console.log(f);
// }