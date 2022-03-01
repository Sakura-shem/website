const glide = new Glide(".glide", {keyboard:false});
const captionsEL = document.querySelectorAll(".glide__slide");
glide.mount();

// Swiper 初始化
var mySwiper = new Swiper ('.swiper-container',{
    initialSlide:0,
    mousewheel:true,
    loop:true,
    direction:"vertical",
    pagination:{
        el:".swiper-pagination",
    }
})      

// 导航栏
const highLight = document.querySelector(".highLight");
function selectChange(index = glide.index){
    if(index == 0){
        highLight.style.left = "0.1rem";
        highLight.style.width = "1rem";
    }
    else if (index == 1){
        highLight.style.left = "1.13rem";
        highLight.style.width = "1rem";
    }
    else{
        highLight.style.left = "2.2rem";
        highLight.style.width = "1.1rem";
    }
}
// 导航栏跳转 + 状态提示
function TurnHome(){
    glide.go("=0")
    // 开Home, 关其他
    selectChange()
}
function TurnBlogs(){
    glide.go("=1")
    selectChange()
}
function TurnProjects(){
    glide.go("=2")
    selectChange()
}

// 底部按钮和界面切换
var cardBtn = document.querySelector(".card-buttons").getElementsByTagName("button");
var cardHeader = document.querySelector(".card-header");
var cardSection = document.querySelectorAll(".card-section")
cardBtn = Array.from(cardBtn);
function cardChange(btn){
    // 按钮状态 全取消激活
    cardBtn.forEach((btn) => {
        // console.log(btn);
        if (btn.classList.contains("is-active")){
            btn.classList.remove("is-active");
        }
    })
    // 界面状态 全取消激活
    cardSection.forEach((sec) => {
        if (sec.classList.contains("is-active")){
            sec.classList.remove("is-active");
        }
    })
    // 根据 btn 激活 header + 界面
    if (! btn.classList.contains("aboutBtn")){
        cardHeader.classList.add("is-active");
        if (btn.classList.contains("experienceBtn")){
            cardSection[1].classList.add("is-active");
        }
        else{
            cardSection[2].classList.add("is-active");
        }
    }
    else{
        console.log(cardHeader);
        cardHeader.classList.remove("is-active");
        cardSection[0].classList.add("is-active");
    }
    // 激活对应按钮
    btn.classList.add("is-active");


}




// 音乐控制
var myAudio = document.getElementById('sound');

var Music_Play = document.querySelectorAll(".Music_Play");
var Music_Pause = document.querySelectorAll(".Music_Pause");
var Music_Play_Control = document.querySelectorAll(".play-pause-button");
var albumName = document.querySelectorAll(".album-name");
var trackName = document.querySelectorAll(".track-name");
var albumArt = document.querySelectorAll(".album-art");
var playerTrack = document.querySelectorAll(".playerTrack");

Music_Play_Control.forEach((btn) => {
    btn.addEventListener('click', Control);
})

// Logo 控制
var Logo = document.getElementById('Logo');

function Control() {
    console.log(albumName.textContent);
    if(myAudio.paused){
        myAudio.play();

        Logo.setAttribute("type", "rotate");
        albumName.forEach((btn) => {
            btn.textContent = "SKBLJS"
        });
        trackName.forEach((btn) => {
            btn.textContent = "DJ--SKBLJS"
        });
        // scale
        // 隐藏 pause
        Music_Pause.forEach((btn) => {
            btn.style.display = 'block';
        });
        Music_Play.forEach((btn) => {
            btn.style.display = 'none';
        });
        albumArt.forEach((btn) => {
            btn.style.bottom = '0.55rem';
        });
        playerTrack.forEach((btn) => {
            console.log(btn);
            btn.classList.add("active");
        });
    }else{
        albumName.forEach((btn) => {
            btn.textContent = ""
        });
        trackName.forEach((btn) => {
            btn.textContent = ""
        });
        Logo.setAttribute("type", "scale");
        myAudio.pause();
        Music_Pause.forEach((btn) => {
            btn.style.display = 'none';
        });
        Music_Play.forEach((btn) => {
            btn.style.display = 'block';
        });
        albumArt.forEach((btn) => {
            console.log(btn.style.bottom);
            btn.style.bottom = '0.3rem';
        });
        playerTrack.forEach((btn) => {
            btn.classList.remove("active");
        });
    }
}
// 进度条
// var sArea = document.querySelectorAll(".s-area");
// playerTrack.forEach((btn) => {
//     btn.mousemove(function (event) {
//         showHover(event);
//     });
//     btn.mouseout(hideHover);
//     btn.on("click", playFromClickedPos);
// });

// BLOGS search bar
function search_submit(e){
    var evt = window.event || e;
    var inputbox = document.getElementById('search-input');
    var inputvalue = inputbox.value.split("--")
    if(evt.keyCode == 13){
        // 回车事件
        alert(inputvalue[0].trim());
        if (inputvalue[1].trim() == "gg")
            window.open("https://www.google.com/search?q=" + inputvalue);
    }
}
// 登录
// 用户事件
const userInfo = document.getElementById("userInfo");

// 注册/登录动画
const signinBtn = document.getElementById("signin");
const signupBtn = document.getElementById("signup");
const firstFrom = document.getElementById("signup_form");
const secFrom = document.getElementById("signin_form");
const Logger = document.querySelector(".Log")
const closeLogFormBtn01 = document.getElementById("closeLogFormBtn01")
const closeLogFormBtn02 = document.getElementById("closeLogFormBtn02")

signinBtn.addEventListener("click", ()=>{
    Logger.classList.remove("Log_active")
    // 关闭按钮变成白色
    closeLogFormBtn01.style.color = "whitesmoke";
    closeLogFormBtn02.style.color = "whitesmoke";
})

signupBtn.addEventListener("click", ()=>{
    Logger.classList.add("Log_active")
    closeLogFormBtn01.style.color = "black";
    closeLogFormBtn02.style.color = "black";
})
firstFrom.addEventListener("submit", (e)=>e.preventDefault())
secFrom.addEventListener("submit", (e)=>e.preventDefault())

// 关闭 
closeLogFormBtn02.addEventListener("click", ()=>{
    logForm.style.opacity = 0;
    logForm.style["pointer-events"] = "none";
})
closeLogFormBtn01.addEventListener("click", ()=>{
    logForm.style.opacity = 0;
    logForm.style["pointer-events"] = "none";
})



//      ; /*阻止元素的点击事件*/
// user-select: none; /*用户是否可以选择文本*/

// 弹出效果
function myblur () {
    var layout = document.querySelectorAll(".layout")[0];
    console.log("55");
    layout.style["filter"] = "blur(2px)";
    layout.style["pointer-events"] = "none";
    layout.style["user-select"] = "none";
    var popup = document.getElementById("popup"); // 同上
    popup.classList.toggle("active"); // 同上
}
function myclear () {
    var layout = document.querySelectorAll(".layout")[0];
    console.log("55");
    layout.style["filter"] = "blur(0px)";
    layout.style["pointer-events"] = "all";
    layout.style["user-select"] = "all";
    var popup = document.getElementById("popup"); // 同上
    popup.classList.toggle("active"); // 同上
}