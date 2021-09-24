
const cloud = require('wx-server-sdk')
 
cloud.init()
// 通过云函数简化对于用户信息的读取

// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()  // 获取信息
  return {  // 放回用户相关的四个信息
    event,
    openid: wxContext.OPENID,
    appid: wxContext.APPID,
    unionid: wxContext.UNIONID,
  }
}