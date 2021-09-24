// app.js
App({
  onLaunch() {
    if(!wx.cloud){
      console.error('za告诉你要用高版本库')
    }else{
      console.log('successfully launch')
      wx.cloud.init({
      env:"cloud1-2glpk6q07a55c33b",
      traceUser: false,
      })
    }

    wx.cloud.callFunction({
      name: 'getOpenid'
    }).then(res=> {
      wx.setStorage({
        key:'OPENID',
        data: res.result.openid
      })
      console.log(res.result.openid)
  }).catch(err=>{
    console.log(err)
  })
  },

})
