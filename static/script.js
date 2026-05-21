// timer
var sec=0; 
setInterval(function() {
sex++; var m=Math.floor(sec/60); var s= sec  % 60;
document.getElementById("TIMER").innerText= (m<10?"0"+m:m)+ ":" + (s<10?"0"+s:s);}, 1000);

// plus minus 
function adj(name, val) {
    var id= "inp_"+name.replace(/ /g, "_"); var inp= document.getElementById(id);
    var cur= parseInt(inp.value) || 0; inp.value=Math.max(0, cur+ val);}
var today= new Date();
var mm=today.getMonth()+1;
var dd=today.getDate();


var yy=today.getFullYear() ;
var examdate= document.getElementById("Examdate");
if(examdate) { 
        examdate.value=yy+"-"+(mm<10?"0"+mm:mm)+"-"+(dd<10?"0"+dd:dd) ;}
