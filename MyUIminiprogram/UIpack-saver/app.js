// app.js
App({
  onLaunch() {
    if(!wx.cloud){
      console.error('za告诉你要用高版本库')
    }else{
      console.log('successfully launch')
      wx.cloud.init({
      env:"	cloud1-2glpk6q07a55c33b",
      traceUser: true,
      })
    }
  },
})
