const path=require("path"),http=require("http"),os=require("os"),{handleMsg:handleMsg}=require("./message"),{parseBody:parseBody,getLogger:getLogger,ErrorWithCode:ErrorWithCode,getRealWorkspace:getRealWorkspace,initHxConfig:initHxConfig}=require("./utils"),localPath=process.env.UNICLOUD_DEBUGGER_PATH,{JsonRpcClient:JsonRpcClient}=require(path.resolve(localPath,"share/bridge")),jsonRpcClient=new JsonRpcClient({bridgeProcess:process});function deleteCache(){let e=[path.resolve(process.env.WORKSPACE_FOLDER),path.resolve(process.env.UNICLOUD_DEBUGGER_PATH,"internal-functions")];const s=getRealWorkspace();s&&e.push(path.resolve(s)),e=e.map((e=>e.toLowerCase())),Object.keys(require.cache).forEach((s=>{e.some((e=>s.toLowerCase().indexOf(e.toLowerCase())>-1))&&delete require.cache[s]}))}const server=http.createServer((async(e,s)=>{const r={req:e,res:s,method:e.method,status(e){return s.statusCode=e,this},send(e){return s.end(JSON.stringify(e)),this},throw:(e,s)=>{throw new ErrorWithCode({code:s||"SYSTEM_ERROR",message:e||"未知错误"})},hxConfig:null,servePath:__dirname,jsonRpcClient:jsonRpcClient};if(s.setHeader("Content-Type","application/json;charset=UTF-8"),s.setHeader("Access-Control-Allow-Origin","*"),s.setHeader("Access-Control-Allow-Headers",e.headers["access-control-request-headers"]||"Origin, X-Requested-With, Content-Type, Accept"),"POST"===r.method)r.data=await parseBody(e);else if("OPTIONS"===r.method)return void r.status(200).send({});deleteCache();const t=e.url.split("/"),o=t[1],n=t[2];if(!o||!n)return void r.status(404).send({code:"NOT_FOUND",message:"访问地址不正确"});let a;r.controller=o,r.service=n;try{a=require("./controller/"+o)}catch(e){return void r.status(404).send({code:"NOT_FOUND",message:"访问地址不正确"})}initHxConfig(r),r.logger=getLogger(r);const c=new a;c.ctx=r;try{const e=await c.exec();r.status(200).send(e)}catch(e){r.status("NOT_FOUND"===e.code?404:500).send({code:e.code||"SYSTEM_ERROR",message:e.message||"调试服务内部错误"})}}));function isRunning(e){try{return process.kill(e,0)}catch(e){return"EPERM"===e.code}}server.listen(process.env.SERVE_PORT,"0.0.0.0"),server.on("listening",(()=>{const e=os.networkInterfaces();let s=[];Object.keys(e).forEach((r=>{s=s.concat(e[r])}));const r=s.filter((e=>"IPv4"===e.family)).sort(((e,s)=>"127.0.0.1"===e.address?-1:1)).map((e=>e.address));if(0===r.length)throw new Error("未能获取局域网地址，本地调试服务不可用");const t=server.address().port;process.send&&process.send({action:"server/start",data:{address:r,servePort:t,debugPort:process.debugPort}})})),server.on("error",(e=>{"EADDRINUSE"===e.code&&process.send({action:"server/error",data:{code:e.code,message:e.message,detail:{servePort:e.port}}})})),handleMsg(),process.on("uncaughtException",(e=>{console.error(e)}));const uniCloudPluginPid=parseInt(process.env.UNICLOUD_PLUGIN_PID);uniCloudPluginPid&&setInterval((()=>{isRunning(uniCloudPluginPid)||process.exit(1)}),3e3);