
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
// const num = [1,2,3,4,5,6,7,8,9,10,11];
// const [a,vb,c] = num;
// console.log(a);

// const obj ={
//     name :"Murad",
//     age : 7,
//     friends : "yes",
//     status : "single",
// };

// const {age,friends,status} = obj;
// console.log(age);


// const test = [
//     {  name :"Murad",
//     age : 7,
//     friends : "yes",
//     status : "single",
//     },
//     {
//         name :"Sadia",
//         age : 11,
//         friends : "yes",
//         status : "Marrid",
//     },
//     {
//         name :"tanvir",
//         age : 17,
//         friends : ["murad","saida","niti",{
//             name :"hey",
//         }],
//         status : "Couple",
//     }
// ];

// console.log(test[2].friends[3].name);

// const num3 = [1,2,3];
// const squre = num3.map(x => x*x);
// console.log(squre);
//map-filter-find
// const product = [
//     { name : 'xiomi',id : 1,price : 500,color : "gole"},
//     { name : 'apple',id : 2,price : 500,color : "blue"},
//     { name : 'vivo',id : 3,price : 500,color : "gole"},
//     { name : 'lenovo',id : 3,price : 500,color : "green"},
// ]

// const result = product.filter(x => x.id == 1);

// const result1 = product.find(x => x.id == 1);
// console.log(result1);



//for each
// const productcontainer = document.getElementById("product-container");
// const result3 = product.forEach((product)=>{
//     console.log(product);
//     const h1 = document.createElement("h1");
//     h1.innerText = product.name;
//     productcontainer.appendChild(h1);
// });

// const item = () =>{
//     const result1 = product.find(x => x.id == 1);
//     const h1 = document.createElement("h1");
//     h1.innerText = result1.name;
//     productcontainer.appendChild(h1);
// }

//api


// fetch("https://fakestoreapi.com/products/")
// .then(res=>res.json())
// .then((data)=>{
//     console.log(data[1].id);
// })
// .catch((err)=>{
//     console.log(err);
// })

// fetch("https://fakestoreapi.com/products")
// .then(res=>res.json())
// .then((data=>{
//     console.log(data[0]);
// }))
// .catch((err) =>{
//     console.log(err);
// })


//
// console.log(1);
// console.log(2);
// console.log(3);
// console.log(4);
// name(5);
// console.log(6);
// console.log(7);
// console.log(8);
// console.log(9);


// const name = (x) =>{
//     console.log(x);
//     settimeout (() => console.log(x))
// }

// function name(x){
//     console.log(x);
//     settimeout (() => console.log(x))
// }

//promise and async, await
// const getdata = new Promise(function (resolve,reject){
//     return reject("data not found");
// });

// getdata
//     .then(data=>console.log(data))
//     .catch((err)=> console.log(err))


const loaddata = async() =>{
    try{
        
        const response = await fetch("https://fakestoreapi.com/products");
        const data = await response.json();
        console.log(data[0].id);
        const productcontainer = document.getElementById("product-container");
        const h1 = createElement("h1");
        h1.innerText = data[0].id;
        productcontainer.appendChild(h1);
        
    }catch{
        (err)=>{
            console.log(err);
        }
    }
};

const loaddata1 = async() =>{
    try {
        const responce = await fetch("https://fakestoreapi.com/products");
        const data = await responce.json();
        console.log(data[1].title);
    } catch{
        (err)=>{
            console.log(err);
        }
    }
}
loaddata();




