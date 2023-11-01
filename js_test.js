
const hutao = document.getElementById('hutao')

const keqing = document.getElementById('keqing')

const gamyu = document.getElementById('gamyu')

const raiden = document.getElementById('raiden')

const p = document.getElementsByClassName('chat')


let number = 0
const pimg = ['호두', '에스더 각청', '에스더 감우', '에스더 라이덴쇼군']

let chat = [[], [], [], []]


hutao.addEventListener('click', function(){
    p[0].setAttribute('id', 'mytext1')
    hutao_hide.style.display = 'none'
    keqing_hide.style.display = 'none'
    gamyu_hide.style.display = 'none'
    raiden_hide.style.display = 'none'
    hutao_hide.style.display = 'block'
    number = 0
    console.log(number, '호두와의 채팅')
    scr()
})

keqing.addEventListener('click', function(){
    p[1].setAttribute('id', 'mytext2')
    hutao_hide.style.display = 'none'
    keqing_hide.style.display = 'none'
    gamyu_hide.style.display = 'none'
    raiden_hide.style.display = 'none'
    keqing_hide.style.display = 'block'
    number = 1
    console.log(number, '각청과의 채팅')
    scr()
})

gamyu.addEventListener('click', function(){
    p[2].setAttribute('id', 'mytext3')
    hutao_hide.style.display = 'none'
    keqing_hide.style.display = 'none'
    gamyu_hide.style.display = 'none'
    raiden_hide.style.display = 'none'
    gamyu_hide.style.display = 'block'
    number = 2
    console.log(number, '감우와의 채팅')
    scr()
})

raiden.addEventListener('click', function(){
    p[3].setAttribute('id', 'mytext4')
    hutao_hide.style.display = 'none'
    keqing_hide.style.display = 'none'
    gamyu_hide.style.display = 'none'
    raiden_hide.style.display = 'none'
    raiden_hide.style.display = 'block'
    number = 3
    console.log(number, '라이덴쇼군과의 채팅')
    scr()
})


const textarea = document.getElementById('text')
const button = document.getElementById('button')



// textarea에 텍스트 입력하고 이벤트를 줬을때 화면에 띄우는 함수
function send(){
const content = textarea.value.trim() // 텍스트 내용 복사
    
    textarea.value = '' // 채팅이 전송된 후 내용 제거

    if (content === '') { // 비어있으면 전송 실패
        console.log('공백이라서 고백실패')
        return
    }
    
    //채팅 내용 가져오기
    console.log(content)
    
    // 채팅 내용 전송
    const msg = document.createElement('div')
    msg.setAttribute('class', 'msg')
    const myimgdiv = document.createElement('div')
    myimgdiv.setAttribute('id', 'myimg')
    msg.appendChild(myimgdiv)
    const myimg = document.createElement('img')
    myimg.src = "images/" + pimg[number] + ".jpg"
    myimg.setAttribute('id', 'myimg')
    myimgdiv.appendChild(myimg)
    const myname = document.createElement('div')
    myname.setAttribute('id', 'myname')
    myname.append('나')
    msg.appendChild(myname)
    const mytext = document.createElement('div')
    mytext.setAttribute('id', 'mytext')
    msg.appendChild(mytext)
    const textNode = document.createTextNode(content)
    mytext.appendChild(textNode)
    
    p[number].append(msg)

    
    // 공백 생성
    const newTag = document.createElement('br') // 빈 br 태그 생성
    p[number].appendChild(newTag) // 생성된 br태그 채팅에 추가


    addLog()
}


button.addEventListener('click', () => {
    send()
})


textarea.addEventListener('keydown', function(event) {
    if(event.key === 'Enter') {
        send()
    }
})




// 스크롤바 자동으로 내려가게 하기
function scr() {
    p[number].isScrollBottom = true


    p[number].addEventListener("scroll", (event) =>{
        if(event.target.scrollHeight - event.target.scrollTop === event.target.clientHeight) {
            p[number].isScrollBottom = true
        } else {
            p[number].isScrollBottom = false
        }
    })
}


const addLog = () => {
    const smsg = textarea.value

    p[number].innerHTML += `${smsg}\r\n`

    if(p[number].isScrollBottom) {
        p[number].scrollTop = p[number].scrollHeight
    }
}

 