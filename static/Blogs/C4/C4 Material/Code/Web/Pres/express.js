//引入express

const express=require('express');
const path=require('path');
//创建应用对象
const app=express();
//创建路由规则

app.use(express.static(path.join(__dirname,'public')));


app.get('/get',(request,response)=>{
    response.send('Hello Express');
});
//监听端口启动服务
app.listen(8000,()=>{
    console.log("服务已经启动，8000端口监听中。。。");
});