#!/usr/bin/env node

// TODO 暂时处理安装目录包含特殊符号，导致 H5 预览资源加载失败的问题。
const matchSymbol = __dirname.match(/[()]/)
if (matchSymbol) {
    console.error(`编译失败：HBuilderX 安装目录不能包括 ${matchSymbol[0]} 等特殊字符`)
    process.exit(0)
}

const fs = require('fs')
const path = require('path')

const {
    error
} = require('@vue/cli-shared-utils')
const yargsParser = require('yargs-parser')
const argv = yargsParser(process.argv.slice(2))
process.env.UNI_INPUT_DIR = path.resolve(process.env.UNI_INPUT_DIR)
process.env.UNI_OUTPUT_DIR = path.resolve(process.env.UNI_OUTPUT_DIR)
if (process.env.UNI_SCRIPT) {
    const {
        initCustomScript
    } = require('@dcloudio/uni-cli-shared/lib/package')

    initCustomScript(process.env.UNI_SCRIPT, path.resolve(process.env.UNI_INPUT_DIR, 'package.json'))
}

const Service = require('@vue/cli-service')

const vueConfigJsPath = path.resolve(process.env.UNI_INPUT_DIR, 'vue.config.js')

if (fs.existsSync(vueConfigJsPath)) {
    process.env.VUE_CLI_SERVICE_CONFIG_PATH = vueConfigJsPath
}

// @vue/cli-service/lib/Service.js
const service = new Service(process.env.VUE_CLI_CONTEXT || process.cwd())

const args = {
    watch: process.env.NODE_ENV === 'development',
    minimize: process.env.UNI_MINIMIZE === 'true',
    clean: false
}
if (argv['auto-port']) {
    args['auto-port'] = argv['auto-port']
}
if (argv['auto-host']) {
    args['auto-host'] = argv['auto-host']
}
const platform = process.env.UNI_SUB_PLATFORM || process.env.UNI_PLATFORM
service.run((process.env.NODE_ENV === 'development' && platform === 'h5') ? 'uni-serve' : 'uni-build',
    args).catch(err => {
    if (err.message.includes('@dcloudio/uni-mp-lark/dist/uni.mp.esm.js')) {
        err = new Error('Vue3 项目暂不支持飞书小程序')
    }
    error(err)
    process.exit(1)
})
