var hx = require("hbuilderx");
var fs = require("fs")
var os = require("os")

function compile(data) {
	let result = new Promise((resolve, reject) => {
		hx.request("MainHostPublish.compile", data).then((param) => {
			resolve(param);
		}, reject);
	});

	return result;
}

function getFormItems(formData, ssr, spaceFolder) {
	let  publishPath = os.tmpdir();
	publishPath = publishPath + "/publish_uni.json";
	let website;
	let domain;
	let projectId = spaceFolder.id;
	let  path = os.tmpdir();
	path = path + "/publish_uni.json";
	if( projectId &&  fs.existsSync(path))
	{
	  let readData = fs.readFileSync(path);
	  let jsonData = JSON.parse(readData);
	  let projectIdData = jsonData[''+projectId+''];
	  if(projectIdData)
	  {
		  website = projectIdData.website;
		  domain = projectIdData.domain
	  }
	}
	
	let forms = {
		title: "H5发行",
		hideSubTitile: true,
		width: 600,
		height: formData.webHostingCheckBox ? 480 : 200,
		formItems: [{
			type: "input",
			name: "websiteTitle",
			label: "网站标题",
			placeholder: "输入网站标题",
			value:formData.websiteTitle?formData.websiteTitle:website
		},
		{
			type: "input",
			name: "websiteDomain",
			label: "网站域名",
			placeholder: "输入网站域名",
			value: formData.websiteDomain?formData.websiteDomain:domain,
		},
		{
			type: "checkBox",
			name: "ssrCheckBox",
			label: "以SSR方式发行 <a href='https://uniapp.dcloud.net.cn/ssr?id=distribute'>帮助</a>",
			value: formData.ssrCheckBox,
			isHidden: !ssr
		},
		{
			type: "checkBox",
			name: "webHostingCheckBox",
			label: "将编译后的资源部署到前端网页托管",
			value: formData.webHostingCheckBox
		},
		{
			type: "spaceList",
			name: "selectSpaceList",
			isHidden: !formData.webHostingCheckBox,
			projectId: spaceFolder.id
		}
		].map((item) => {
			if (item && !item.isHidden) {
				return item;
			}
		})
	};
	
	return forms;
}

function getDomainItems(formData) {
	let itemsArray = [];
	for (var i = 0; i < formData.length; i++) {
		var column = [{
			"label": formData[i].domain
		}];
		itemsArray.push({
			"columns": column
		});
	}

	let forms = {
		title: "选择一个自定义域名",
		width: 480,
		height: 320,
		formItems: [{
			type: "list",
			title: "",
			name: "domainList",
			columnStretches: [1, 2],
			items: itemsArray
		}]
	};
	return forms;
}
//该方法将在插件激活的时候调用
function activate(context) {
	//let disposable = hx.commands.registerCommand('project.action.app.publish.weapp2', () => {
	hx.workspace.registerWorkspaceFolderLauncher("uniapp:publish:h5", (params) => {
		let spaceFolder = params.workspaceFolder;
		let ssr = spaceFolder.vueVersion == 3 ? true : false;
		let customId = params.args.customId;
		let funcitonPath;
		let bindSpace;
		
		let h5website;
		let projectId = spaceFolder.id;
		let  path = os.tmpdir();
		path = path + "/publish_uni.json";
		if( projectId &&  fs.existsSync(path))
		{
		  let readData = fs.readFileSync(path);
		  let jsonData = JSON.parse(readData);
		  let projectIdData = jsonData[''+projectId+''];
		  if(projectIdData)
		  {
			  h5website = projectIdData.website;
		  }
		}
		let form = hx.window.showFormDialog({
			submitButtonText: "发行(&P)",
			cancelButtonText: "取消(&C)",
			validate: async function (formData) {
				if (!formData.websiteTitle) {
					this.showError("网站标题不能为空");
					return false;
				}
				if (formData.ssrCheckBox && formData.webHostingCheckBox) {
					var existsfuncResult = await hx.unicloud.unimodulesExistsModule(spaceFolder,
						"uni-ssr");
					funcitonPath = existsfuncResult.funcitonPath;
					if (false == existsfuncResult.exist) {
						var result = await hx.window.showMessageBox({
							type: 'Info',
							title: '选择SSR发行部署依赖uni_modules插件uni-ssr,请先安装该插件',
							text: '',
							buttons: ['安装', '取消']
						});
						if (result == "安装") {
							var extension = hx.extensions.getExtension("uni_modules");
							if (extension) {
								extension.installDeps({
									fsPath: spaceFolder.uri.fsPath,
									deps: ["uni-ssr"]
								});
							} else {
								console.error("can't resolve extension:", extensionId);
							}
						}
						this.showError("");
						return false;
					}

					var bindspaceResult = await hx.unicloud.getProjectBindSpace(spaceFolder);
					if (bindspaceResult.code == 0) {
						bindSpace = bindspaceResult.space;
						let bindSpaceid = bindSpace.spaceId;
						if (formData.webHostingCheckBox && (bindSpaceid == '' || bindSpaceid ==
							null || bindSpaceid == undefined)) {
							this.showError("当前项目没有绑定服务空间,请先绑定服务空间");
							return false;
						}
					} else {
						this.showError("当前项目没有绑定服务空间,请先绑定服务空间");
						return false;
					}
				}

				let selectSpaceList = formData.selectSpaceList;
				let spaceid;
				if (selectSpaceList) {
					spaceid = selectSpaceList.spaceId;
				}

				if (formData.webHostingCheckBox && (spaceid == '' || spaceid == null || spaceid ==
					undefined)) {
					this.showError("请选择一个服务空间");
					return false;
				}

				if (formData.webHostingCheckBox && formData.selectSpaceList.isOpenHostingService ==
					false) {
					this.showError("服务空间未开通前端网页托管");
					return false;
				}

				this.showError("");
				return true;
			},
			onChanged: function (field, value, formData) {
				if (field == 'webHostingCheckBox') {
					this.updateForm(getFormItems(formData, ssr, spaceFolder));
				}
				return true;
			},
			...getFormItems({
				"websiteTitle": h5website?h5website:spaceFolder.name,
				"ssrCheckBox": false,
				"webHostingCheckBox": false,
			}, ssr, spaceFolder)
		});

		form.then(async (res) => {
			let issuessr = false;
			if (res.ssrCheckBox == true) {
				issuessr = true;
			}
			let webHosting = false;
			if (res.webHostingCheckBox) {
				webHosting = true;
			}
			
			let result = await hx.unicloud.getExistsUnicloudAndBindSpace({workspaceFolder:spaceFolder});
				
			if( result && result.code == 0 && true == result.unicloud )
			{
				if(!result.spaceId)
				{
					let okText = "确定(&O)";
					let cancelText = "取消(&C)"
					let buttons = [];
					buttons.push(okText);
					buttons.push(cancelText);
					let continueOperation = "当前项目没有绑定服务空间,确定要继续操作?";
					let messageBoxresult = await hx.window.showMessageBox({
						type: 'question',
						title: '',
						text: continueOperation,
						buttons: buttons
					});
					if(messageBoxresult != okText)
					{
						return;
					}
				}
			}
			let outputChannel = hx.window.createOutputChannel("HBuilder");
			let selectdomain;
			if (issuessr && webHosting && res.selectSpaceList) {
				let provider;
				if (res.selectSpaceList.spaceType == 1) {
					provider = "aliyun";
				}
				else if (res.selectSpaceList.spaceType == 2) {
					provider = "tcb";
				}
				let requesResult = await hx.http.request({
					url: "https://ide.liuyingyong.cn/serverless/host/domain-list",
					method: "post",
					serviceOptions: {
						serviceRequest: true,
						body: {
							provider: provider,
							spaceId: res.selectSpaceList.spaceId
						},
					}
				});
				
				if (requesResult.service.code == 1001) {
					domains = requesResult.service.body.domains;
				}
				else {
					if (requesResult.service.httpStatusCode == 200) {
						outputChannel.appendLine(requesResult.service.body.description);
					}
					else {
						outputChannel.appendLine(requesResult.error);
					}
					return;
				}

				if (domains.length == 1) {
					selectdomain = domains[0].domain;
				} else if (domains.length < 1) {
					outputChannel.appendLine({
						line: "当前服务空间的前端网页托管未绑定自定义域名,请绑定域名后再试",
						level: "warning"
					});
					return;
				} else {
					let domainform = await hx.window.showFormDialog({
						submitButtonText: "确定(&S)",
						cancelButtonText: "取消(&C)",
						validate: function (formData) {
							return true;
						},
						onChanged: function (field, value, formData) { },
						...getDomainItems(domains),
					});
					if (domainform.domainList < 0) {
						outputChannel.appendLine("请选择域名");
						return;
					}
					selectdomain = domains[domainform.domainList].domain;
				}
			}

			if(res.websiteTitle || res.websiteDomain)
			{
				let website = res.websiteTitle;
				let domain;
				if(res.website)
					website= res.websiteTitle;
				if(res.websiteDomain)
					domain= res.websiteDomain;
					
				let projectId = spaceFolder.id;
				let  path = os.tmpdir();
				path = path + "/publish_uni.json";
				if(projectId)
				{
					let jsonData;
					if( projectId &&  fs.existsSync(path))
					{
					  let readData = fs.readFileSync(path);
					  jsonData = JSON.parse(readData);
					}
				
					if(!jsonData)
					{
						jsonData = {id:""};
					}
					
					let json = {website:website,domain:domain};
					//jsonData.put(projectId,json);
					jsonData[''+projectId+'']  = json;
					
					let data = JSON.stringify(jsonData,null,'\t');;
					fs.writeFileSync(path,data);
				}
			}

			let compileResult = await compile({
				workspaceFolder: spaceFolder,
				issuessr: issuessr,
				domain: selectdomain,
				type: 'h5',
				customId:customId,
				websiteTitle:res.websiteTitle,
				websiteDomain:res.websiteDomain
			});
			if (compileResult.code == 0 && webHosting) {
				//let outputChannel = hx.window.createOutputChannel("HBuilder");
				if (issuessr) {
					outputChannel.appendLine("开始部署编译后的h5到前端网页托管、云函数uni-ssr...");
				} else {
					outputChannel.appendLine("开始部署编译后的h5到前端网页托管...");
				}
				let buildServerPath = compileResult.buildServerPath;
				let webHostingresult = hx.unicloud.staticDeployFiles(spaceFolder,
					res.selectSpaceList,
					compileResult.buildClientPath,
					function each(params) { },
					function success(params) {
						if (issuessr) {
							if (buildServerPath.endsWith != '/') {
								buildServerPath = buildServerPath + "/";
							}
							var serverFuncitonPath = funcitonPath + "/server"
							let copyResult = hx.workspace.copyFileWithPrompt({
								src: hx.Uri.file(buildServerPath),
								dest: hx.Uri.file(serverFuncitonPath),
								rootPromptTips: '文件%1 已存在,是否替换',
								filePromptTips: '文件%1 已存在,是否替换',
								defaction: 'replace',
								showcomparebutton: false,
								filter: function (params) {
									return 0;
								},
								errorHandler: function (
									err) {
									return 0;
								}
							});
							copyResult.then(async (params) => {
								if (params == 0) {
									outputChannel.appendLine(
										"部署完成后,需要配置uni-ssr云函数的url化地址,具体参考:https://uniapp.dcloud.net.cn/uniCloud/http"
									)
									outputChannel.appendLine(
										"配置云函数uni-ssr地址后,访问配置的地址即可看到服务端渲染的页面"
									);
									await hx.unicloud.uploadCloudFuntion(
										spaceFolder, funcitonPath);
									outputChannel.appendLine("部署完成");
								}
							});
						} else {
							outputChannel.appendLine("部署完成");
						}
					}
				);
			}
		}).catch((info)=>
		{
			//console.log("info",info);
		});
	});
	//});
	// //订阅销毁钩子，插件禁用的时候，自动注销该command。
	//context.subscriptions.push(disposable)
}
//该方法将在插件禁用的时候调用（目前是在插件卸载的时候触发）
function deactivate() {

}
module.exports = {
	activate,
	deactivate
}
