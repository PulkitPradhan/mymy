// for (let i = 1; i <= 5; i++) {
//     console.log(i);
// }

// for(let i=1; i<=5; i++){
//     console.log("i is " + i)
// }
// for(let i=6; i<=10; i++){
//     console.log("i is " + i)
// }

// console.log(10=="10")
// console.log(10==="10")

// let arr1=[1,2,3,4,]
// let arr2=arr1.map(num => num**2)
// console.log(arr2)

// function greet(nm,main){
//     console.log("Good Morning " + nm)
//     main()
// }
// greet("user",function(){
//     console.log("callback executed")
// })

// let nums = [1, 2, 3, 4];

// // map: doubles values
// let mapped = nums.map(n => n * 2); // [2, 4, 6, 8]
// // filter: keeps evens
// let filtered = nums.filter(n => n % 2 === 0); // [2, 4]

let marks=[1,2,3,4,5,]
sm+=0
for (let i of marks){
    sm+=i;
    let status = (m >= 40) ? "Pass" : "Fail";
    console.log(`Mark: ${m}, Status: ${status}`);
}
console.log("Average: " + (sum / marks.length));