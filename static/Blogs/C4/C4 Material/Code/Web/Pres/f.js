window.onload=function(){
                
    var prev=document.getElementById ("prev");
    var next=document.getElementById("next");
    //alert("prev");
    var img=document.getElementById("imge");
    var but=document.getElementById("buttons").getElementsByTagName("span");
    var first=document.getElementById("first");
    var last=document.getElementById("last");
    var path= "D:/Document/Creat/magic/Python/C4/Data/images/"
    var imgArr=[ path + "Pulse.jpg" , path + "Sound.jpg" , path + "Blink.jpg" , path + "Attention.jpg" , path + "Result.jpg"]
    var imgArra=[path + "Pulse.jpg" , path + "Pulse1.jpg"] 
    var imgArrb=[path +"Sound.jpg", path +"Sound1.jpg"]
    var imgArrc= [path + "Blink.jpg" , path +"Blink1.jpg"]
    var imgArrd=[path +"Attention.jpg" , path +"Attention1.jpg"]
    var imgArre=[path+"Result.jpg" , path + "Result1.jpg"]
    
    var mai=document.getElementById("mai");
    var vio=document.getElementById("vio");
    var eye=document.getElementById("eye");
    var bri=document.getElementById("bri");
    var tir=document.getElementById("tir");



    var index=0;
    var i=0;
    prev.onclick = function(){
        index--;
        if(index<0){
            index=4;
        }
         
         img.src=imgArr[index];
         but[i].className="";
         i--;
         if(i<0){
             i=4;
         }
        but[i].className="on"
    };

    next.onclick = function(){
        
         index++;
         if(index>4){
            index=0;
        }
          img.src=imgArr[index];
          but[i].className="";
          i++;
          if(i>4){
              i=0;
          }
         but[i].className="on"
    };

    first.onclick = function(){
        
        index=0;
         img.src=imgArr[index];
         but[i].className="";
         i=0;
        but[i].className="on"
   };

   last.onclick = function(){
        
    index=4; 
     img.src=imgArr[index];
     but[i].className="";
     i=4;
    but[i].className="on"
    };
    
    mai.onclick = function(){
        
        index=0;
         img.src=imgArr[index];
         but[i].className="";
         i=0;
        but[i].className="on"
   };

   vio.onclick = function(){
        
    index=1;
     img.src=imgArr[index];
     but[i].className="";
     i=1;
    but[i].className="on"
    };

    eye.onclick = function(){
        
        index=2;
         img.src=imgArr[index];
         but[i].className="";
         i=2;
        but[i].className="on"
   };

   bri.onclick = function(){
        
    index=3;
     img.src=imgArr[index];
     but[i].className="";
     i=3;
    but[i].className="on"
};

tir.onclick = function(){
        
    index=4;
     img.src=imgArr[index];
     but[i].className="";
     i=4;
    but[i].className="on"
};
var t=0;
setInterval(function(){
    // index++;
    // if(index>4){
    //     index=0;
    // }
    // img.src=imgArr[index];
    if(index==0){  
         t++;
         if(t>1){
            t=0;
         }
         img.src=imgArra[t];
    }
    if(index==1){  
        t++;
        if(t>1){
           t=0;
        }
        img.src=imgArrb[t];
   }
   if(index==2){  
    t++;
    if(t>1){
       t=0;
    }
    img.src=imgArrc[t];
}
if(index==3){  
    t++;
    if(t>1){
       t=0;
    }
    img.src=imgArrd[t];
}
     
},1000)
setInterval(function(){
if(index==4){  
    t++;
    if(t>1){
       t=0;
    }
    img.src=imgArre[t];
}
},3000)
}

            