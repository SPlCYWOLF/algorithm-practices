// const ns = [2, 7, 11, 15]
// const t = 9

// function twoSum(nums, target) {
//   const numToIndex = new Map();
//   // console.log(numToIndex);

//   for (let i = 0; i < nums.length; i++) {
//     const num = nums[i];

//     const complement = target - num;
//     const complementIndex = numToIndex.get(complement);
//     // console.log(num, complement, numToIndex, complementIndex);

//     if (complementIndex != null) {
//       return [complementIndex, i];
//     }

//     numToIndex.set(num, i);
//     // console.log(numToIndex);

//   }

//   throw new Error('invalid input: no match found');
// }

// console.log(twoSum(ns, t));




for(var i = 0; i<5; i++) {
  
  setTimeout(() => {
    console.log(i)
  }, 10)

}