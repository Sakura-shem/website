window.onload=function(){
                
    var prev=document.getElementById ("prev");
    var next=document.getElementById("next");
    //alert("prev");
    var img=document.getElementById("imge");
    var but=document.getElementById("buttons").getElementsByTagName("span");
    var first=document.getElementById("first");
    var last=document.getElementById("last");
     var imgArr=["images/1.jpg" , "images/2.jpg" , "images/3.jpg" , "images/4.jpg" , "images/5.jpg"]

    var index=0;
    var i=0
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
    
            var i=0;
            but[0].onclick=function(){
                but[i].className="";
                i=0;
                but[i].className="on";
                index=0;
                img.src=imgArr[index];
            }
            but[1].onclick=function(){
                but[i].className="";
                i=1;
                but[i].className="on";
                index=1;
                img.src=imgArr[index];
            }
            but[2].onclick=function(){
                but[i].className="";
                i=2;
                but[i].className="on";
                index=2;
                img.src=imgArr[index];
            }
            but[3].onclick=function(){
                but[i].className="";
                i=3;
                but[i].className="on";
                index=3;
                img.src=imgArr[index];
            }
            but[4].onclick=function(){
                but[i].className="";
                i=4;
                but[i].className="on";
                index=4;
                img.src=imgArr[index];
            }
     
    



}
