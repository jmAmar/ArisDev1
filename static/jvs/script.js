/** script.js **/

/* OLD */
window.openPageOLD = function(href)
    {   document.querySelector("body").style.opacity = 0;       
        setTimeout(setLocation(href) , 1000);
    }

function setLocation(href)
{  window.location.href = href;
}

/* NEW */
window.openPageNEW = function(href)
    {   document.querySelector("body").style.opacity = 0;       
        setTimeout(function()
            { window.location.href = href; } , 1000);
    }

document.addEventListener("DOMContentLoaded", function(event)
    {   document.querySelector("body").style.opacity = 1;
        gotoConseilAdm();
    })

document.body.addEventListener("load", checkSession());
document.body.addEventListener("load", gotoAGO());
document.body.addEventListener("load", moveInfoVedette());
// document.getElementById("spnContraction").addEventListener("click", rotateSpan());


function openSection()
{   document.getElementById("sxnContent").style.opacity = 0;
    setTimeout(function()
        {   document.getElementById("sxnContent").style.opacity = 1; } , 1000);
}

function rotateSpan()
{   document.getElementById("spnContraction").style.transform = "rotateY("+90+"deg)";
    setTimeout(function()
        {   document.getElementById("spnContraction").style.transform = "rotateY("+0+"deg)";
        } , 1000);
}

function checkSession()
{   let nbConnexions = sessionStorage.getItem('nbConnexions');
    if(nbConnexions === null || nbConnexions === undefined)
    {   sessionStorage.setItem('nbConnexions', '1');
        rotateSpan();
        // moveInfoVedette();
    }
}

function gotoConseilAdm()
{   let anchor = document.getElementById('spnAnchor').textContent;
    if(anchor == "spnConseilAdm") { window.location.href = '#spnAnchor'; }
}

function gotoAGO()
{   var wdw = window.location.pathname;
    if(wdw == "/assembleesGales/") { document.location.href="/listAGO"; }
}

function moveInfoVedette()
{   if(window.location.pathname == "/index/")
    {   setTimeout(function()
        {   document.getElementById("infoVedette").style.opacity = 0;
        } , 0);
        setTimeout(function()
        {   document.getElementById("infoVedette").style.opacity = 1;
        } , 500);
        /*
        setTimeout(function()
        {   document.getElementById("infoVedette").style.transform = "scaleY(1.5)";
        } , 1000);
        setTimeout(function()
        {   document.getElementById("infoVedette").style.transform = "scaleY(1)";
        } , 1500);
        */
    }
}

/**/
