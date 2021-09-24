// pages/showMap/showMap.js
const app = getApp()
const db=wx.cloud.database()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    throneList: [],
    border: [],
    latitude: 28.219611,
    longitude: 112.919452,
    thrones: [
      // {
      //   id: 0,
      //   name: "temp.name",
      //   latitude: 28.219611,
      //   longitude: 112.919452,
      // }
    ],
    item: 0,
    tab: 0
  },

  changeItem(e) {
    this.setData({
      item: e.target.dataset.item
    })
  },

  // 太多东西了，有点搞不定

  changeTab(e) {
    this.setData({
      tab: e.detail.current
    })
  },

  loadThrones(e) {
    this.setData({
      'thrones': [],
    })
    db.collection('myThrones').where({
      'isWorking':true,
    }).get({
      success: function(res){
        this.setData({
          throneList: res.data
        })
        console.log(res.data)
        console.log("configuring the throne")
        for(let i=0;i < this.throneList.length;i++){
          let temp = this.throneList[i]
          this.thrones.push({
            id: temp.id,
            // name: temp.name,
            title: temp.name,
            latitude : temp.pos.getLatitudeE(),
            longitude: temp.pos.getLongtitudeE(),
          })
        }
      },
      fail: function(err){
        console.error('fail to fetch the database'+err)
      }
    })
    console.log("load!")
  },


  /**
   * 生命周期函数--监听页面加载
   */

  onLoad: function (options) {
    console.log("start to launch")
    this.loadThrones()
    db.collection('border').get().then(res=>{
      this.setData({
        border : res.data
      })
    }).catch(err=>{
      console.error('fail to fetch the database'+err)
    })
},

mapUpload(e){
  this.loadThrones()
}

})