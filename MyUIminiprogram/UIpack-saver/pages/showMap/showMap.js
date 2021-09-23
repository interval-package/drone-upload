// pages/showMap/showMap.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    latitude: 28.219611,
    longitude: 112.919452,
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

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
})