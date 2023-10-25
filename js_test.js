const btn1 = document.getElementById("one")
const btn2 = document.getElementById("two")
const btn3 = document.getElementById("three")

const handleClick = function(){
    console.log("저를 클릭하셨나요?")
}

btn2.addEventListener('click', handleClick)
btn2.addEventListener('click', function(){
    console.log("또 다른 핸들러가 추가 등록되었다!")
})