"use strict";function e(e){return e&&"object"==typeof e&&"default"in e?e.default:e}var n=e(require("path")),t=e(require("fs")),o=e(require("hjson")),r=e(require("urllib")),i=e(require("@alicloud/mpserverless-node-sdk")),s=e(require("module"));const c=Object.prototype.toString;function l(e,n,{parseSource:t,parseClientIP:o,parseClientUserAgent:r,parseSpaceInfo:i,parseFunctionName:s}={}){e||(e={}),e.clientInfo||(e.clientInfo={});const l=e.clientInfo;return l.SOURCE=t(e,n),l.CLIENTIP=o(e,n)||"",l.CLIENTUA=r(e,n)||"",l.SPACEINFO=i(e,n)||"",l.FUNCTION_NAME=s(e,n)||"",function(e,n){const t=e.clientInfo,o=e.headers;o&&(t.CLIENTIP||(t.CLIENTIP=o["x-real-ip"]),t.CLIENTUA||(t.CLIENTUA=o["user-agent"]));t.DEVICEID||(t.DEVICEID=e.uniCloudDeviceId);if(t&&"[object Object]"===c.call(t))for(const e in t)Object.hasOwnProperty.call(t,e)&&!n[e]&&(n[e]=t[e]);delete e.uniCloudDeviceId,delete e.clientInfo,delete e.uniCloudClientInfo}(e,n),e}const u={};var a=async(e,n,t)=>{l(e,n,t),function(e,n){global.__ctx__=n,global.__args__=e}(e,n),delete process.env.accessKeyID,delete process.env.accessKeySecret,delete process.env.securityToken,n=Object.assign({},n),t.initUniCloud(),function(){const e=require("path"),n=e.resolve(__dirname,"./@common_modules");let t;try{t=require(e.resolve(__dirname,"package.json"))}catch(e){}if(!t||!t.extensions)return;const o=Object.keys(t.extensions);if(o.length)throw new Error("当前云函数用到了扩展能力暂不支持本地调试，请上传到云端调试");o.forEach(t=>{const o=u[t]||t;require(e.resolve(n,o))})}();const o=global.uniCloudDebug.functionEntry;return require(o).main(e,n)};const d=require("./@dcloudio/serverless/lib/aliyun/uni-cloud");function p(e,n){return"client"}function f(e,n){return global.uniCloudDebug.clientIP||"127.0.0.1"}function g(e,n){return{spaceId:global.__space_id__,provider:"aliyun"}}function m(e,n){return global.uniCloudDebug.userAgent||"HBuilderX"}function C(e,n){return global.uniCloudDebug.functionName}function h(e){if(global.uniCloud=new d({context:e}),global.uniCloud.isLocal=!0,global.uniCloudDebug.isServe){const e=require("./local").callFunction;global.uniCloud.callFunction=e}}async function y(e,{uniCloudSecret:n}={}){return a(e.args,e,{parseSource:p,parseClientIP:f,parseClientUserAgent:m,parseSpaceInfo:g,parseFunctionName:C,initUniCloud:h})}y.toString=function(){return""},process.env.UNICLOUD_DEBUGGER_PATH=process.env.UNICLOUD_DEBUGGER_PATH||n.resolve(__dirname,"../");const v=process.env.UNICLOUD_DEBUGGER_PATH,E=n.resolve(v,"share/index"),{parseJson:_,getType:I,getRealWorkspace:b,getCloudfunctionPathList:D,getFunctionEntry:N,getCommonModulePath:S,getActionPath:x,isModuleEncrypted:O,isFileEncrypted:P,JsonRpcClient:j}=require(E),U=n.resolve(v,"internal-functions");t.readdirSync(U).filter(e=>t.statSync(n.resolve(U,e)).isDirectory());const w=[];class F extends Error{constructor(e){super(e.message),this.errMsg=e.message||"",this.code=e.code,Object.defineProperties(this,{message:{get(){return`errCode: ${e.code||""} | errMsg: `+this.errMsg},set(e){this.errMsg=e}}})}}const T=module.constructor.length>1?module.constructor:s,q=T._resolveFilename,A=[{regexp:/.*uniCloud(?:.*?)\/cloudfunctions\/common\/(.*)\//i,type:"common"},{regexp:/.*uniCloud(?:.*?)\/cloudfunctions\/uni-clientDB-actions\/(.*)/i,type:"clientDBAction"},{regexp:/.*uniCloud(?:.*?)\/database\/validateFunction\/(.*)/i,type:"validateFunction"},{regexp:/.*uniCloud(?:.*?)\/cloudfunctions\/(.*)\//i,type:"function"},{regexp:/.*unicloud\/internal-functions\/common\/(.*)\//i,type:"inernalCommon"},{regexp:/.*unicloud\/internal-functions\/(.*)\//i,type:"inernalFunction"}];function L(e,n){const t=e.match(n.regexp);if(t)return{modulePath:t[0],moduleName:t[1],type:n.type}}function k(e){let o;try{o=t.statSync(e)}catch(e){}if(!o)return;if(o.isFile()||o.isSymbolicLink())return e;const r=Object.keys(T._extensions);if(o.isDirectory()){const o=n.resolve(e,"package.json"),i=t.existsSync(o)&&require(o),s=i&&i.main;if(s)return n.resolve(e,s);for(let o=0;o<r.length;o++){const i=r[o],s=n.resolve(e,"index."+i);if(t.existsSync(s))return s}}}const R=process.argv[2],B=process.argv[3],M=process.argv[4],G=n.resolve(B,R);if(global.uniCloudDebug={functionName:R,functionPath:B,functionEntry:G,userAgent:"HBuilderX",clientIP:"127.0.0.1"},process.noDeprecation=!0,O(G))throw new F({code:"FUNCTION_ENCRYPTED",message:"此云函数已加密，不可本地运行"});function H(e){return new Promise((n,t)=>{setTimeout(()=>{n()},e)})}(e=>{T._resolveFilename=function(o,r,i,s){function c(){return q.call(T,o,r,i,s)}const l=o.split("/"),u=l.shift();if(u.startsWith(".")||!r.filename)return c();const a=l.join("/");if(e.indexOf(u)>-1)throw new F({code:"MODULE_ENCRYPTED",message:u+"模块已加密，不支持本地运行"});const d=function(e){e=e.replace(/\\/g,"/");for(let n=0;n<A.length;n++){const t=L(e,A[n]);if(t)return t}}(r.filename);if(!d)return c();const{modulePath:p,moduleName:f,type:g}=d;if("clientDBAction"===g||"validateFunction"===g||"inernalFunction"===g&&"DCloud-clientDB"===f){const{realWorkspace:e,provider:o}=global.uniCloudDebug;let r=["uni-id","uni-config-center"].indexOf(u)>-1;const i=S(e,o,u),s=n.resolve(i,"package.json"),l=t.existsSync(s)&&require(s);if(r=r||l.includeInClientDB,!r)return c();const a=k(i);return a||c()}const m=n.resolve(p,"package.json"),C=t.existsSync(m)&&require(m),h=C&&C.dependencies;if(!h)return c();let y=h[u];if(!y||!y.startsWith("file:"))return c();y=y.replace("file:","");let v=n.resolve(p,y);a&&(v=n.resolve(v,a));const E=k(v);return E||c()}})((e=>{const o=function e(o){const r=[];try{const{dependencies:i}=JSON.parse(t.readFileSync(n.resolve(o,"package.json")));if(!i)return[];Object.keys(i).filter(e=>0===i[e].indexOf("file:")).map(t=>{const s=n.resolve(o,i[t].replace("file:",""));r.push({moduleName:t,modulePath:s}),r.push(...e(s))})}catch(e){}return r}(e);return 0===o.length||(function(e){const n={};for(let t=0;t<e.length;t++){const{moduleName:o,modulePath:r}=e[t];n[o]||(n[o]=new Set),n[o].add(r)}let t=!1;const o=[];if(Object.keys(n).forEach(e=>{n[e].size>1&&(t=!0,console.error(`公共模块[${e}]只能存在一个，请从下面候选中删除不使用的公共模块：`),n[e].forEach(e=>{console.error(e)}),o.push(e))}),t)throw new Error(`公共模块[${o.join("、")}]只能存在一个，删除不使用的公共模块后再试`)}(o),o.forEach(({moduleName:e,modulePath:n})=>{w.indexOf(e)>-1||O(n)&&w.push(e)})),w})(G)),async function(){let e;try{e=M||t.readFileSync(n.resolve(G,R+".param.json")).toString().replace("\r\n","\n").replace("\r","\n")}catch(n){e="{}"}const s=o.parse(e);try{const e=await async function(e,{uniCloudSecret:n}={}){const t={};let o;try{o=n||JSON.parse(process.env.UNICLOUD_SECRET)}catch(e){throw new Error("未能获取本地调试所需参数，请稍后再试")}return global.__space_id__=o.spaceId,t.mpserverless=new i({endpoint:"https://api.bspapp.com",logger:console,timeout:1e4,...o}),t.logger=console,t.httpclient=r.create(),t.args=e,t.env={},await y(t,{uniCloudSecret:o})}(s);console.log(`云函数[${R}]执行结果:`,e),await H(200),setTimeout(()=>{process.exit(0)},100)}catch(e){if("jql-runner"===process.env.CALL_BY)return{code:e.code||"INTERNAL_ERROR",message:e.message||"jql执行出错",detail:e.stack};console.error(e),await H(300),process.exit(1)}}();
