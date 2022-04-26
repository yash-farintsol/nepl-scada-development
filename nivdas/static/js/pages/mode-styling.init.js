var count

$('#vertical-menu-btn').on('click', function() {
    if (document.getElementsByTagName("BODY")[0].getAttribute('data-sidebar-size') == 'sm') {
        document.getElementById('menu-div').style.width = '68px'
    }
    else {
        document.getElementById('menu-div').style.width = '88px'
    }
})

function themeToggle() {
    let element = document.body;
    if (count % 2 == 0) {
        element.setAttribute("data-layout-mode", "light");
        element.setAttribute("data-sidebar", "light");
    }
    else {
        element.setAttribute("data-layout-mode", "dark");
        element.setAttribute("data-sidebar", "dark");
    }
    count++
    localStorage.setItem("Count", count)
    console.log('count : ', count)
}

$(document).ready(function(){
    if (localStorage.Count) {
        count = localStorage.Count;
    }
    else {
        count = 0
        localStorage.setItem("Count", count)
    }
    let element = document.body;

    if (!element.hasAttribute("data-layout-mode")) {
        var att = document.createAttribute("data-layout-mode");
        element.setAttributeNode(att);
        att = document.createAttribute("data-sidebar");
        element.setAttributeNode(att);
    }

    if (count % 2 == 0) {
        element.setAttribute("data-layout-mode", "light");
        element.setAttribute("data-sidebar", "light");
    }
    else {
        element.setAttribute("data-layout-mode", "dark");
        element.setAttribute("data-sidebar", "dark");
    }
});


// $(document).ready(function(){
//     if (document.cookie.indexOf('theme') == -1) {
//         document.cookie = "theme=light";
//         console.log('theme = light')
//     }

//     let element = document.body;
//     if (!element.hasAttribute("data-layout-mode")) {
//         var att = document.createAttribute("data-layout-mode");
//         element.setAttributeNode(att);
//         att = document.createAttribute("data-sidebar");
//         element.setAttributeNode(att);
//     }
//     if (getCookie("theme") == "dark") {
//         element.setAttribute("data-layout-mode", "dark");
//         element.setAttribute("data-sidebar", "dark");
//         document.cookie = "theme=dark";
//         console.log('1readyl', getCookie("theme"))
//     }
//     else {
//         element.setAttribute("data-layout-mode", "light");
//         element.setAttribute("data-sidebar", "light");
//         document.cookie = "theme=light";
//         console.log('1readyd', getCookie("theme"))
//     }
// });

// function themeToggle() {
//     console.log('theme')
//     let element = document.body;
//     if (getCookie("theme") == "dark") {
//         element.setAttribute("data-layout-mode", "light");
//         element.setAttribute("data-sidebar", "light");
//         document.cookie = "theme=light";
//         console.log('readyl', getCookie("theme"))
//     }
//     else {
//         element.setAttribute("data-layout-mode", "dark");
//         element.setAttribute("data-sidebar", "dark");
//         document.cookie = "theme=dark";
//         console.log('readyd', getCookie("theme"))
//     }
// }








// function getCookie(cname) {
//     let name = cname + "=";
//     let ca = document.cookie.split(';');
//     for(let i = 0; i < ca.length; i++) {
//         let c = ca[i];
//         while (c.charAt(0) == ' ') {
//         c = c.substring(1);
//         }
//         if (c.indexOf(name) == 0) {
//         return c.substring(name.length, c.length);
//         }
//     }
//     return "";
// }

// $(document).ready(function(){
//     if (document.cookie.indexOf('theme') == -1) {
//         document.cookie = "theme=light";
//         console.log('theme = light')
//     }

//     let element = document.body;
//     if (!element.hasAttribute("data-layout-mode")) {
//         var att = document.createAttribute("data-layout-mode");
//         element.setAttributeNode(att);
//         att = document.createAttribute("data-sidebar");
//         element.setAttributeNode(att);
//     }
//     if (getCookie("theme") == "light") {
//         element.setAttribute("data-layout-mode", "light");
//         element.setAttribute("data-sidebar", "light");
//     }
//     else {
//         element.setAttribute("data-layout-mode", "dark");
//         element.setAttribute("data-sidebar", "dark");
//     }
// });

// function themeToggle() {
//     console.log('theme')
//     let element = document.body;
//     if (getCookie("theme") == "dark") {
//         element.setAttribute("data-layout-mode", "light");
//         element.setAttribute("data-sidebar", "light");
//         document.cookie = "theme=light";
//     }
//     else {
//         element.setAttribute("data-layout-mode", "dark");
//         element.setAttribute("data-sidebar", "dark");
//         document.cookie = "theme=dark";
//     }
// }










// function setCookie(name,value) {
//     var expires = "";
//     var date = new Date();
//     date.setTime(date.getTime() + (60*60*3000));
//     expires = "; expires=" + date.toUTCString();
//     document.cookie = name + "=" + (value || "")  + expires + "; path=/";
// }

// function getCookie(name) {
//     var nameEQ = name + "=";
//     var ca = document.cookie.split(';');
//     // the following code allows multiple cookie values and splits them apart
//     for(var i=0;i < ca.length;i++) {
//         var c = ca[i];
//         while (c.charAt(0)==' ') c = c.substring(1,c.length);
//         if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
//     }
//     return null;
// }

// function enableDarkMode() {
//     var element = document.body;
//     element.setAttribute("data-layout-mode", "dark");
//     element.setAttribute("data-sidebar", "dark");
//     setCookie('darkMode',"1");
// }

// function disableDarkMode() {
//     var element = document.body;
//     element.setAttribute("data-layout-mode", "light");
//     element.setAttribute("data-sidebar", "light");
//     setCookie('darkMode',"0");
// }

// // function themeToggle() {
// //     var colour = document.body.getAttribute('data-layout-mode')
// //     if(colour == "dark") {
// //         disableDarkMode();
// //     }
// //     else {
// //         enableDarkMode();
// //     }
// // };

// document.addEventListener("DOMContentLoaded", function(){
//     let element = document.body;
//     if (!element.hasAttribute("data-layout-mode")) {
//         var att = document.createAttribute("data-layout-mode");
//         element.setAttributeNode(att);
//         att = document.createAttribute("data-sidebar");
//         element.setAttributeNode(att);
//         console.log('attr created')
//     }
//     var darkMode = getCookie('darkMode');
//     if (darkMode == "1") {
//         enableDarkMode();
//     } else {
//         disableDarkMode();
//     }
// });