// pages/showMap/showMap.js
const app = getApp()
const db=wx.cloud.database()

Page({
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
  changeTab(e) {
    this.setData({
      tab: e.detail.current
    })
  },

  loadThrones(e) {
    // let tempThrone=[]
    db.collection('myThrones').where({
      'isWorking': true,
    }).get().then(res=>{
      this.setData({
        'throneList': res.data
      })
    }).catch(err=>{
      console.error(err)
    })
    console.log("load!")
  },
  readThrones(e) {
    let tempThrone=[]
    let obj = this.data.throneList
    for(let i in this.data.throneList){
      console.log(obj[i])
      let temp=obj[i]
      tempThrone.push({
        id: temp.num,
        // name: temp.name,
        title: temp.name,
        latitude : temp.geo.latitude,
        longitude: temp.geo.longitude,
        iconPath: "../../images/git.png",
        width: 30,
        height: 30,
    })
  }
  this.setData({
    thrones: tempThrone,
  })
  console.log(tempThrone)
  },


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
    this.mapCtx = wx.createMapContext('myMap')
  },

  mapUpload(e){
    //this.loadThrones()
  },

  getCenterLocation: function (e) {
    this.loadThrones()
    this.readThrones()
    console.log(this.data.throneList)
    this.mapCtx.getCenterLocation({
      success: function(res){
        console.log(res.longitude)
        console.log(res.latitude)
        wx.showToast({
          title: 'longitude:'+res.longitude+','+'latitude:'+res.latitude,
          icon:'none',
        })
      }
    })
  },
})

