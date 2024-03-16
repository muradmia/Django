
// function name(name) {
//     if(true){
//         var x = "hello";

//     }
// }


// const test = "world";
// const name = `hello ${test}`;
// console.log(name);


// const num = [1,2,3,4,5,6,7,8,9,10,11];
// const newarray = ["murad","sadia","parvej",...num]
// console.log(newarray);
// console.log(Math.max(...num));

// function test(){
//     return "hello world";
// }

// const result = test();
// console.log(result);

//arrow function
// const test2 = ()=>{
//     console.log("yes booss");
//     return "bro"
// };
// console.log(test2());

// const hello = (a) =>{
//     return a;
// }
// console.log(hello(6));
const num = [1,2,3,4,5,6,7,8,9,10,11];
const [a,vb,c] = num;
// console.log(a);

const obj ={
    name :"Murad",
    age : 7,
    friends : "yes",
    status : "single",
};

const {age,friends,status} = obj;
console.log(age);


const test = [
    {  name :"Murad",
    age : 7,
    friends : "yes",
    status : "single",
    },
    {
        name :"Sadia",
        age : 11,
        friends : "yes",
        status : "Marrid",
    },
    {
        name :"tanvir",
        age : 17,
        friends : ["murad","saida","niti",{
            name :"hey",
        }],
        status : "Couple",
    }
];

console.log(test[2].friends[3].name);
