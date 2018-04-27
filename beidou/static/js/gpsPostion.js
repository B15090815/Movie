;
(function($) {
	/*
    定位服务
    add  2015-03-19 by  程序员老顾
    博客地址：http://blog.sina.com.cn/guxuelong007
    @object config : {
            @Number width : 一次滚动宽度，默认为box里面第一个一级子元素宽度[如果子元素宽度不均匀则滚动效果会错乱]
            @Number size : 列表长度，默认为box里面所有一级子元素个数[如果size不等于一级子元素个数，则不支持循环滚动]
            @Boolean loop : 是否支持循环滚动 默认 true
            @Boolean auto : 是否自动滚动,支持自动滚动时必须支持循环滚动，否则设置无效,默认为true
            @Number auto_wait_time : 自动轮播一次时间间隔,默认为：3000ms
            @Function callback : 滚动完回调函数，参入一个参数当前滚动节点索引值
        }
*/

	// 坐标转换
	$.translate = function(point, type, callback) {
		var callbackName = $.createFunctionName();
		var xyUrl = "http://api.map.baidu.com/ag/coord/convert?from=" + type + "&to=4&x=" + point.lng + "&y=" + point.lat + "&callback=$.translate." + callbackName;
		// 动态创建script标签
		$.load_script(xyUrl);
		$.translate[callbackName] = function(xyResult) {
			delete $.translate[callbackName]; // 调用完需要删除改函数
			var point = new BMap.Point(xyResult.x, xyResult.y);
			callback && callback(point);
		}
	}

	/* 
	 * 公共方法（依次执行加载百度地图api、h5获取地理位置、转换百度经纬度、最后回调callback）
	 *
	 * $.gpsPosition(function(point){
	 *		// 地图展示
	 *		$.getDetailAddress('map', point);
	 *		// 获取详细地址
	 *		$.displayOnMap(function(address){alert(address)}, point);
	 *	});
	 *
	 */
	$.gpsPosition = function(callback) {
		$.loadBaiduMap(function() {
			$.geolocation(function(position) {
				// 获取到当前位置经纬度
				var lng = position.coords.longitude;
				var lat = position.coords.latitude;
				// 将原始的经纬度转化为百度地图的经纬度
				$.translate(new BMap.Point(lng, lat), 0, function(point) {
				 	callback(point);
				});
			});
		});
	};

	/* 
	 * 获取详细地址
	 * callback（回调函数,参数是address，可以返回address)
	 * point（回调函数参数,无需设置)
	 * 样例参考$.gpsPosition
	 */
	$.getDetailAddress = function(callback, point) {
		var gc = new BMap.Geocoder();
		//获取地址的数据地址
		gc.getLocation(point, function(rs) {
			var addComp = rs.addressComponents;
			address = addComp.province + addComp.city + addComp.district + addComp.street + addComp.streetNumber;
			callback && callback(address);
		});
	};


	/* 展示地图
	 *<div id="map"> 地图所在div的id=>mapId
	 * point（回调函数参数,无需设置)
	 * 样例参考$.gpsPosition
	 */
	$.displayOnMap = function(mapId, point) {
		var map = new BMap.Map(mapId);
		var marker = new BMap.Marker(point);
		map.addOverlay(marker);
		map.centerAndZoom(point, 20);
	};

	// 加载百度地图
	$.loadBaiduMap = function(callback) {
		var callbackName = $.createFunctionName();
		var xyUrl = "http://api.map.baidu.com/api?v=1.5&ak=093960115151785132d91041c3a8889a&callback=$.loadBaiduMap." + callbackName;
		// 动态创建script标签
		$.load_script(xyUrl);

		$.loadBaiduMap[callbackName] = function(xyResult) {
			delete $.loadBaiduMap[callbackName]; // 调用完需要删除改函数
			callback && callback();
		};
	};

	// 获取当前经纬度
	$.geolocation = function(callback) {
		 if (window.navigator.geolocation) {
			var options = {
				enableHighAccuracy: true,
			};
			window.navigator.geolocation.getCurrentPosition(
				function(data) {
					// 获取到当前位置经纬度
					callback(data);
				},
				function(error) {
					console.error(error);
				}, options);
		} else {
			console.error("浏览器不支持html5来获取地理位置信息");
		};
	};


})(Zepto);